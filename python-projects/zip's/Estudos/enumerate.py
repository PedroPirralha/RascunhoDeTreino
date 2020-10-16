''''	Enumerate	
''' 
'''
list1 = ['one','two','tree','four','five','six']
list2 = [6, 7, 8, 9, 10]

for cont, li in enumerate(list1, 1):
	print(cont,li)
'''
list1 = ['one','two','tree','four','five','six','']
def mostrar_numeracao (lista):
	def len_lista():
		for c, li in enumerate(lista):
			print(len(lista[c ]), li)

	for cont,li in enumerate(lista,1):
		print(cont,li)
	print('\n \n')
	print('saiu do for')


mostrar_numeracao (list1)



print('\n')
print(list1[2],len(list1[2]))