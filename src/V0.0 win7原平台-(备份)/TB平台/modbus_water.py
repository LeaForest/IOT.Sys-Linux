import serial
import serial.tools.list_ports
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu


PORT = 'COM6'


def water():
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,
                                                    baudrate=9600,
                                                    bytesize=8,
                                                    parity='N',
                                                    stopbits=1,
                                                    xonxoff=0))

        master.set_timeout(5)
        master.set_verbose(True)

        # read 方法
        data = master.execute(8, cst.READ_HOLDING_REGISTERS, 0, 6)  # slaveAddr funCode startAddr regNum

        json = {"Ox": data[0] / 1000, "watertem": data[1] / 100, "PH": int(data[3] / 1000)}
        return json
    except modbus_tk.modbus_rtu.ModbusInvalidResponseError as err:
        print(err)



