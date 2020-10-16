#função dentro de função#
'''
def hello (nome= 'Pedro'):
	print('Ola', nome)

	def tudobem():
		print('tudo bem')

	def comovoceesta():
		print('como voce esta')

	if nome == 'Pedro':
		return tudobem

	else:
		return comovoceesta

hello()
func = hello()
func()
-----------------------------------'''
def Ola():
	print('	Ola\n')

def outra(func):
	print('aqui dentro tem outa função ')
	func()
#outra(Ola)


def new_decorate(func):
	def funcao_interna():
		print('cod executado antes da função ')
		func()
		print('cod executado dps da função')

	return(funcao_interna)


def precisa_decorar ():
	print('essa função precisa de decorador')

#precisa_decorar = new_decorate(precisa_decorar)
#precisa_decorar()



def ola():
	print(' \n 	função\n')

ola()


def numero (num1, num2):
	print( num1 + num2 )

numero(1, 2)