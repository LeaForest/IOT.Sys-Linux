# !usr/bin/python
# coding=utf-8
import modbus_air as airs
import modbus_water as waters
import time
import json
import paho.mqtt.publish as publish

host = "139.224.9.212"
topic = "v1/devices/me/telemetry"


def send_date(Id, paylod):
    user = {"username": Id, "password": ''}
    msg = json.dumps(paylod)
    try:
        publish.single(topic, msg, 0, False, host, 1883, Id, auth=user)
    except OSError:
        print("网络异常！")


def data():
    waterData = waters.water()
    airData = airs.air()

    Temperature = {"tem": airData['tem'], "hum": airData['hum']}
    Shine = {"shine": airData['shine']}
    Oxgen = {"Ox": waterData['Ox']}
    Watertem = {"watertem": waterData['watertem']}
    ph = {"PH": waterData['PH']}

    send_date("gZ3WdSDpdAMSNEv5k1tg", Temperature)
    send_date("pGF1laSMmGWqHrDYvDqe", Shine)
    send_date("PDBtf0uyYq5aFe851621", Oxgen)
    send_date("ll80AFd8Ljov8g3HnS07", Watertem)
    send_date("JvLyXrtSIiX9pS9EZbwp", ph)


if __name__ == "__main__":
    try:
        while 1:
            try:
                data()
                print("send")
                time.sleep(60)
            except Exception:
                print("数据异常")
                time.sleep(10)
    except KeyboardInterrupt:
        print("over")
