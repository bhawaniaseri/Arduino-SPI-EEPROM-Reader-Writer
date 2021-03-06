## Author: Arpan Das
## Date:   Fri Jan 11 12:16:59 2019 +0530
## URL: https://github.com/Cyberster/SPI-Based-EEPROM-Reader-Writer

## It listens to serial port and writes contents into a file
## requires pySerial to be installed 
import sys 
import serial
import time
start = time.time()

MEMORY_SIZE = 1048576 # In bytes
serial_port = '/dev/ttyACM0'
baud_rate = 115200 # In arduino, Serial.begin(baud_rate)
write_to_file_path = "dump.rom"

output_file = open(write_to_file_path, "wb")
ser = serial.Serial(serial_port, baud_rate)

print("Press d for dump ROM else CTRL+C to exit.")
ch = sys.stdin.read(1)

if ch == 'd':
	ser.write('d')
	for i in range(4096): # i.e. MEMORY_SIZE / 256
		# wait until arduino response with 'W' i.e. 1 byte of data write request
		while (ser.read() != 'W'): continue
		ser.write('G') # sends back write request granted signal
	
		for j in range(256):
			byte = ser.read(1);
			output_file.write(byte);
		print(str(MEMORY_SIZE - (i * 256)) + " bytes remaining.")
		
print '\nIt took', time.time()-start, ' seconds.'
