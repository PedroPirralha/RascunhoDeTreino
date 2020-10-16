
cod_acess = (999999, 999999, 9999999, 9999999)

key_acess1 = 0
key_acess2 = 0
key_acess3 = 0
key_acess4 = 0

while True:
	if key_acess1 == cod_acess[0]:
		key_acess1 == cod_acess[0]
		print(key_acess1)
		break
	else:
		key_acess1 +=1
		print(key_acess1)

while True:
	if key_acess2 == cod_acess[1]:
		key_acess2 = cod_acess[1]
		print(key_acess2)
		break
	else:
		key_acess2 +=1
while True:
	if key_acess3 == cod_acess[2]:
		key_acess3 = cod_acess[2]
		print(key_acess3)
		break
	else:
		key_acess3 += 1
while True:
	if key_acess4 == cod_acess[3]:
		key_acess3 = cod_acess[3]
		print(key_acess4)
		break
	else:
		key_acess4 += 1


key = key_acess1,key_acess2,key_acess3,key_acess4
dig_key = 110, 110, 110, 110
if dig_key == key:
	print('senha correta !!')
else:
	print('senha incorreta !!')

