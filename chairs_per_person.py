f = open("reservations")
no_eat = {}

for reservation in f:
	name, number = reservation.split(",")
	try:
		chairs_per_person = round(50 / int(number))
	except:
		#print("Wabbit-{} can't eat here. ".format(name))
		no_eat[name] = number 
	print("{} will get {} chairs per person".format(name, chairs_per_person))

print(no_eat)