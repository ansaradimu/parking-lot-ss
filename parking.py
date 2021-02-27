import heapq
from collections import defaultdict

class Car:
	'''
		CAR class with 2 properties. Vehichle number (reg_num) and driver's age (driver_age)
	'''
	def __init__(self,reg_num,driver_age):
		self.reg_num = reg_num
		self.driver_age = driver_age
		
		
class ParkingSystem:
	
	'''
		ParkingSystem class. All the parking related activitis will be controlled from here
	'''
	
	def __init__(self):
		self.available_slot_list = []
		
		self.slot_car_map = dict() 
		self.age_car_map = defaultdict(list)
		self.age_slot_map = defaultdict(list) 
		
	def create_parking_lots(self,total_slots):
		
		for slot in range (1, total_slots+1):
			heapq.heappush(self.available_slot_list,slot)
			
		print("Created parking of {} slots".format(total_slots))
		
	def get_cars_by_driver_age(self,driver_age):
		if len(self.age_car_map[driver_age]) == 0:
			print ("None")
			return
		print (self.age_car_map[driver_age])
	
	def get_slot_id_by_regno(self,reg_num):
		slot_det = None
		for slot, car in self.slot_car_map.items():
			if car.reg_num == reg_num:
				slot_det=slot
				break
				
		print (slot_det)
		pass
		
	def get_slots_by_driver_age(self,driver_age):
		if (len(self.age_slot_map[driver_age]) == 0):
			print ("None")
			return
		print (self.age_slot_map[driver_age])
		
	def park_a_car(self,car):
		if self.available_slot_list:
			available_slot = heapq.heappop(self.available_slot_list)
			self.slot_car_map[available_slot] = car
			self.age_car_map[car.driver_age].append(car.reg_num)
			self.age_slot_map[car.driver_age].append(available_slot)
			print ("Car with vehicle registration number \"{}\" has been parked at slot number {}".format(car.reg_num,available_slot))
		else:
			print ("Sorry! Slots are full")
			
		pass
		
	def unpark_a_park(self,slot_num):
		if self.slot_car_map.has_key(slot_num):
			car_det = self.slot_car_map[slot_num]
			del self.slot_car_map[slot_num]
			self.age_car_map[car_det.driver_age].remove(car_det.reg_num)
			self.age_slot_map[car_det.driver_age].remove(slot_num)
			heapq.heappush(self.available_slot_list, slot_num)
			print ("Slot number {} vacated, the car with vehicle registration number \"{}\" left the space, the driver of the car was of age {}".format(slot_num,car_det.reg_num,car_det.driver_age))
		else:
			print ("Slot already vacant")
			
		

