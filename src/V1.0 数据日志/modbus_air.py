import serial
import serial.tools.list_ports
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu


PORT = '/dev/ttyUSB0'


def air():
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
        data = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 9)  # slaveAddr funCode startAddr regNum
        json = {"hum": data[0] / 10, "tem": data[1] / 10, "shine": data[8]}
        return json
    except modbus_tk.modbus_rtu.ModbusInvalidResponseError as err:
        print(err)


