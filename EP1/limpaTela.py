from os import system, name 

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 

def teste(i=1):
	limpaTela()
	print("######                                                   ")
	print("#     # ###### #    #       #    # # #    # #####   ####  ")
	print("#     # #      ##  ##       #    # # ##   # #    # #    # ")
	print("######  #####  # ## # ##### #    # # # #  # #    # #    # ")
	print("#     # #      #    #       #    # # #  # # #    # #    # ")
	print("#     # #      #    #        #  #  # #   ## #    # #    # ")
	print("######  ###### #    #         ##   # #    # #####   ####  ")  
	print("Iteracao: {}".format(i))                                                                   
	x = float(input("Digite um valor: "))
	if x > 0: 
		teste(i+1)

teste()