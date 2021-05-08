#Atividade 16, ver se um corredor está apto ou não para correr determinada maratona

tempo = int(input("Digite o tempo (em min) que o(a) corredor (a) correu alguma maratona : "))
idade = int(input("Digite a idade do(a) corredor (a): "))
sexo = input("Digite o sexo do(a) corredor (a): ")

if idade >= 18 and idade <=34:
	if sexo == 'm':
		if tempo<185:
			print("Avise ao corredor para fazer as malas , ele/ela conseguiu índice para Boston .")
		else:
			print("Que pena! Ele/ela não conseguiu índice dessa vez.")
	elif sexo == 'f':
		if tempo<210:
			print("Avise ao corredor para fazer as malas , ele/ela conseguiu índice para Boston .")
		else:
			print("Que pena! Ele/ela não conseguiu índice dessa vez.")
elif idade >= 35 and idade <=44:
	if sexo == 'm':
		if tempo<200:
			print("Avise ao corredor para fazer as malas , ele/ela conseguiu índice para Boston .")
		else:
			print("Que pena! Ele/ela não conseguiu índice dessa vez.")
	elif sexo == 'f':
		if tempo<230:
			print("Avise ao corredor para fazer as malas , ele/ela conseguiu índice para Boston .")
		else:
			print("Que pena! Ele/ela não conseguiu índice dessa vez.")
elif idade >= 45 and idade <=54:
	if sexo == 'm':
		if tempo<210:
			print("Avise ao corredor para fazer as malas , ele/ela conseguiu índice para Boston .")
		else:
			print("Que pena! Ele/ela não conseguiu índice dessa vez.")
	elif sexo == 'f':
		if tempo<240:
			print("Avise ao corredor para fazer as malas , ele/ela conseguiu índice para Boston .")
		else:
			print("Que pena! Ele/ela não conseguiu índice dessa vez.")
elif idade >= 55 and idade <=69:
	if sexo == 'm':
		if tempo<220:
			print("Avise ao corredor para fazer as malas , ele/ela conseguiu índice para Boston .")
		else:
			print("Que pena! Ele/ela não conseguiu índice dessa vez.")
	elif sexo == 'f':
		if tempo<260:
			print("Avise ao corredor para fazer as malas , ele/ela conseguiu índice para Boston .")
		else:
			print("Que pena! Ele/ela não conseguiu índice dessa vez.")
elif idade >= 70:
	if sexo == 'm':
		if tempo<240:
			print("Avise ao corredor para fazer as malas , ele/ela conseguiu índice para Boston .")
		else:
			print("Que pena! Ele/ela não conseguiu índice dessa vez.")
	elif sexo == 'f':
		if tempo<280:
			print("Avise ao corredor para fazer as malas , ele/ela conseguiu índice para Boston .")
		else:
			print("Que pena! Ele/ela não conseguiu índice dessa vez.")




