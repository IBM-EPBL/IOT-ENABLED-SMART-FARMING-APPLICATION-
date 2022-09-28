from random import randint
def temperature():
	return randint(1,100)
def humidity():
    return randint(1,100)
random_temperature=temperature()
print("TEMPERATURE is:",random_temperature)
random_humidity=humidity()
print("HUMIDITY is:",random_humidity)
if random_temperature not in range(5,30):
    print("CAUTION! HIGH TEMPERATURE!!")
else:
    print("TEMPERATURE is NORMAL")
if random_humidity not in range(40,60):
    print("CAUTION! HUMIDITY IS HIGH!!")
else:
    print("HUMIDITY is NORMAL")
