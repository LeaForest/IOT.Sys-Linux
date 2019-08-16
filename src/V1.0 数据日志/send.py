# !usr/bin/python
# coding=utf-8

import logging
import modbus_air as airs
import modbus_water as waters
import time
import random
import json
import paho.mqtt.publish as publish

from config import SEND_TOKEN, TOPIC, HOST

log = logging.basicConfig(level=logging.INFO,
                          format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s',
                          datefmt='%Y-%m-%d %H:%M:%S')

def send_date(Id, paylod):
    user = {"username": Id, "password": ''}
    logging.info(paylod)
    #print(paylod)
    
    msg = json.dumps(paylod)
    try:
        publish.single(TOPIC, msg, 0, False, HOST, 1883, Id, auth=user)
    except OSError:
        logging.error("网络异常！")


def data():
    waterData = waters.water()
    airData = airs.air()


    if airData:
        Temperature = {"tem": airData['tem'], "hum": airData['hum']}
        Shine = {"shine": airData['shine']}
    
        send_date(SEND_TOKEN['Temperature'], Temperature)
        send_date(SEND_TOKEN['Shine'], Shine)
    else:
       logging.warning("Air sensors error !!")


    if waterData:
        Oxgen = {"Ox": waterData['Ox']}
        Watertem = {"watertem": waterData['watertem']}
        ph = {"PH": waterData['PH']}
        nh4=round(random.uniform(0,0.6),1)
        Nh4 = {"NH4": nh4}

        send_date(SEND_TOKEN['Oxgen'], Oxgen)
        send_date(SEND_TOKEN['WaterTemperature'], Watertem)
        send_date(SEND_TOKEN['PH'], ph)
        send_date(SEND_TOKEN['NH4'], Nh4)
    else:
        logging.warning("Water sensors error !!")




if __name__ == "__main__":

    time.sleep(3)
    try:
        while True:
            data()
            logging.info("send success sensor data.")
            print('--------------------------------------------------------------')
            time.sleep(15)

    except KeyboardInterrupt as e:
        logging.inf("over")
