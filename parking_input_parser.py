import sys
from parking import Car, ParkingSystem

parking_sys = ParkingSystem()

def input_parser(command):
	'''
		Takes the commands one by one and parse it accordingly
	'''
	
	if len(command.strip()) > 0:
		command_split = command.split()
		
		main_command = command_split[0].strip().lower()
		
		if main_command == "create_parking_lot":
			parking_sys.create_parking_lots(int(command_split[1].strip()))
			
		elif main_command == "park":
			car = Car(command_split[1].strip(),command_split[3].strip())
			parking_sys.park_a_car(car);
			
		elif main_command == "slot_numbers_for_driver_of_age":
			parking_sys.get_slots_by_driver_age(command_split[1].strip());
			
		elif main_command == "leave":
			parking_sys.unpark_a_park(int(command_split[1].strip()))
			
		elif main_command == "vehicle_registration_number_for_driver_of_age":
			parking_sys.get_cars_by_driver_age(command_split[1].strip())
			
		elif main_command == "slot_number_for_car_with_number":
			parking_sys.get_slot_id_by_regno(command_split[1].strip())
			
		else:
			print ("Wrong command found, check the command file and retry..")


if len(sys.argv) < 2: # Command file missing
	print "Error in input format. Eg: python parking_input_parser.py <your_command_file.txt>"
else:
	command_file = sys.argv[-1]
	commands = open(command_file, 'r')
	Lines = commands.readlines()

	for line in Lines:
		input_parser(line)
