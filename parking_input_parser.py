import sys
from parking import Car, ParkingSystem

parking_sys = ParkingSystem()

def input_parser(command):
	print (command)
	if len(command.strip()) > 0:
		command_split = command.split()
		print(command_split)
		
		main_command = command_split[0].strip().lower()
		
		if main_command == "create_parking_lot":
			parking_sys.create_parking_lots(int(command_split[1].strip()))
			pass
			
		elif main_command == "park":
			pass
			
		elif main_command == "slot_numbers_for_driver_of_age":
			pass
			
		elif main_command == "leave":
			pass
			
		elif main_command == "vehicle_registration_number_for_driver_of_age":
			pass


if len(sys.argv) < 2:
	print "Error in input format. Eg: python parking_input_parser.py <your_command_file.txt>"
else:
	command_file = sys.argv[-1]
	commands = open(command_file, 'r')
	Lines = commands.readlines()

	for line in Lines:
		input_parser(line)
