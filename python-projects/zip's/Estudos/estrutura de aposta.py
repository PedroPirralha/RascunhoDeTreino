import random
def aposta(val_min, val_max):
	aposta_do_adver = []
	for c in range(val_min , val_max+1):
	    aposta_do_adver.append(c)
	aposta_adversario = random.choice(aposta_do_adver)
	return aposta_adversario


valor_min = 10	#int(input('digite o valor minimo da aposta :'))
valor_max = 20	#int(input('digite o valor maximo da aposta :'))

class meu_saldo(object):
	"""docstring for meu_saldo"""
	def __init__(self, minha_aposta, aposta_adversario, qm_ganhou):
		aposta = minha_aposta + aposta_adversario
		if qm_ganhou == 'player1':
			print(aposta)
		else:
			print(aposta - (aposta*2))



minha_aposta = 20
aposta_adversario = aposta(valor_min, valor_max)
qm_ganhou = 'player2'
primeira_aposta = meu_saldo(minha_aposta, aposta_adversario, qm_ganhou)
print('seu saldo é de :',meu_saldo)


print(aposta_adversario)



