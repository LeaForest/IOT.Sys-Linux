import serial
import serial.tools.list_ports
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu


PORT = 'COM9'


def nh4():
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,
                                                    baudrate=9600,
                                                    bytesize=8,
                                                    parity='N',
                                                    stopbits=1,
                                                    xonxoff=0))

        master.set_timeout(1)
        master.set_verbose(True)

        # read 方法
        data = master.execute(9, cst.READ_HOLDING_REGISTERS, 0, 1)  # slaveAddr funCode startAddr regNum
        json = {"NH4": round(data[0], 2)}
        return json
    except modbus_tk.modbus_rtu.ModbusInvalidResponseError as err:
        print(err)


