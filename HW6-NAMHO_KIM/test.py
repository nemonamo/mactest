import random

temp = random.randrange(0,40)
humi = random.randrange(0,100)
bright = random.randrange(70,150)

result = str(temp)
result += ","
result += str(humi)
result += ","
result += str(bright)


print(result)