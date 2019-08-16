# !usr/bin/python
# coding=utf-8

import logging
import modbus_air as airs
import modbus_water as waters
# import modbus_nh4 as nh4s
import time
import json
import paho.mqtt.publish as publish
import numpy as np
from config import SEND_TOKEN, TOPIC, HOST, PRE_START, COLLECT_NUMBER, COLLECT_STOP_TIME
import random

logging.basicConfig(level=logging.INFO,
                          format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s',
                          datefmt='%Y-%m-%d %H:%M:%S')


def send(Id, paylod):
    user = {"username": Id, "password": ''}
    logging.info(paylod)
    msg = json.dumps(paylod)
    try:
        publish.single(TOPIC, msg, 0, False, HOST, 1883, Id, auth=user)
    except OSError:
        logging.error("网络异常！")


def collectData():
    data = {'temp': [], 'hum': [], 'shine': [], 'watertemp': [], 'PH': [],  'Ox': [],'NH4':[]}
    for i in range(COLLECT_NUMBER):

        waterData = waters.water()
        airData = airs.air()
        # nh4Data = nh4s.nh4()
        nh4Data = random.uniform(0,3)

        # air sensor
        data['temp'].append(airData['temp'])
        data['hum'].append(airData['hum'])
        data['shine'].append(airData['shine'])

        # water sensor
        print(waterData)
        data['watertemp'].append(waterData['watertemp'])
        data['PH'].append(waterData['PH'])
        data['Ox'].append(waterData['Ox'])

        # NH4 sensor
        data['NH4'].append(nh4Data)
        
        time.sleep(COLLECT_STOP_TIME)

    for i in data.keys():
        data[i] = processData(data[i])

    return data


def processData(data=[]):
    # return to median
    data = np.median(data)

    return data


def sendData():
    send_data = collectData()

    try:
        send(SEND_TOKEN['PH'], {'PH': int(send_data['PH'])})
        send(SEND_TOKEN['NH4'], {'NH4': int(send_data['NH4'])})
        send(SEND_TOKEN['Shine'], {'shine': int(send_data['shine'])})
        send(SEND_TOKEN['Temperature'], {'temp': send_data['temp'], 'hum': send_data['hum']})
        send(SEND_TOKEN['WaterTemperature'], {'watertemp': send_data['watertemp']})
        send(SEND_TOKEN['Oxgen'], {'Ox': send_data['Ox']})

    except Exception as e:
        logging.error(e)
        return False

    return True



if __name__ == "__main__":

    time.sleep(PRE_START)
    try:
        while True:
            if sendData():

                logging.info("send success sensor data.")
                print("- - - - - - - - - - - - - - - - - - - --")
            else:
                logging.info('send faild sensor data!!!')
    except KeyboardInterrupt as e:
        logging.info("over")
