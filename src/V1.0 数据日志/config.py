# -*- encoding: utf-8 -*-

import os

HOST = os.getenv("HOST", '139.224.9.212')

TOPIC = os.getenv("TOPIC", 'v1/devices/me/telemetry')

SEND_TOKEN = {
    "Temperature": os.getenv('TEMPERATURETOKEN', 'wjz9GX6nTA1MgWqLsJmw'),
    "Oxgen": os.getenv("OXGENTOKEN", 'xwzmPbIHdQ8YRVDb9oz7'),
    'WaterTemperature': os.getenv("WATERTEMPERATURETOKEN", 'zQ3Nb1F2aiu5veKmWaYk'),
    'PH': os.getenv('PHTOKEN', '6NeaPxwUaOhqxgs83n0g'),
    'NH4': os.getenv('NH4TOKEN', '3OVikswqi5ItKupsEXx6'),
    'Shine': os.getenv('SHINETOKEN', 'TdVJlNS4MvLRsgYU28K2')
}

# 预启动时间
PRE_START = int(os.getenv('PRE_START', 90))

COLLECT_NUMBER = int(os.getenv('COLLECT_NUMBER', 15))
COLLECT_STOP_TIME = int(os.getenv('COLLECT_STOP_TIME', 1))

