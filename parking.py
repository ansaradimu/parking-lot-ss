import heapq
from collections import defaultdict

class Car:
	def __init__(self,reg_num,driver_age):
		self.reg_num = reg_num
		self.driver_age = driver_age
		
		
class ParkingSystem:
	
	def __init__(self):
		self.available_slot_list = []
		
		self.slot_car_map = dict() # slot -> Car details
		self.age_car_map = defaultdict(list) # 
		self.age_slot_map = defaultdict(list) 
		
	def create_parking_lots(self,total_slots):
		
		for slot in range (1, total_slots+1):
			heapq.heappush(self.available_slot_list,slot)
		
	def get_cars_by_driver_age(self,driver_age):
		print ("Cars by age::",self.age_car_map[driver_age])
	
	def get_slot_id_by_regno(self,reg_num):
		slot_det = None
		for slot, car in self.slot_car_map.items():
			if car.reg_num == reg_num:
				slot_det=slot
				break
				
		print ("Slot::",slot_det)
		pass
		
	def get_slots_by_driver_age(self,driver_age):
		print ("Slots by age::",self.age_slot_map[driver_age])
		pass
		
	def park_a_car(self,car):
		if self.available_slot_list:
			available_slot = heapq.heappop(self.available_slot_list)
			print ("Available slot ::",available_slot)
			self.slot_car_map[available_slot] = car
			self.age_car_map[car.driver_age].append(car.reg_num)
			self.age_slot_map[car.driver_age].append(available_slot)
			
			#print ("Age -> Car",self.age_car_map)
			#print ("Age -> Slot",self.age_slot_map)
		else:
			print ("Sorry! Slots are full")
			
		pass
		
	def unpark_a_park(self,slot_num):
		if self.slot_car_map.has_key(slot_num):
			car_det = self.slot_car_map[slot_num]
			print ("Yes",car_det.reg_num)
			del self.slot_car_map[slot_num]
			self.age_car_map[car_det.driver_age].remove(car_det.reg_num)
			self.age_slot_map[car_det.driver_age].remove(slot_num)
			heapq.heappush(self.available_slot_list, slot_num)
		else:
			print ("No")
			
		
c1 = Car("3",25)
c2 = Car("2",25)
c3 = Car("1",26)

p1 = ParkingSystem()
p1.create_parking_lots(3)

p1.park_a_car(c1)
p1.park_a_car(c2)
p1.park_a_car(c3)

p1.get_slot_id_by_regno("3")
#p1.unpark_a_park(c2)

		
		

