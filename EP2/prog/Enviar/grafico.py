import matplotlib.pyplot as plt
import math as m
#para o import rodar, tive que instalar o matplotlib no computador com alguns comandos

def myRange(inicio, fim, step, L = []): #função range com o step
    """Função que replica a função range nativa do python. Entretanto, ela possui o step.
    Por meio desse recurso, é possível definir um intervalo cada vez menor de delta x e gerar
    o gráfico com maior precisão."""
    if inicio<fim:
    	return myRange(inicio+step,fim,step,L+[inicio])
    else:
    	return L

def geraGrafico(func,inicio,fim,numf,step=0.02): #plota gráfico da função
    """Função utilizada para gerar o gráfico da função. Ela utiliza a biblioteca matplotlib
    para plotar o gŕáfico. Sendo chamada, ela salva o gráfico e exibe ele na tela."""
    y = list(map(func,myRange(inicio,fim,step)))
    fig, ax = plt.subplots()
    ax.plot(myRange(inicio,fim,step), y) 

    ax.set(xlabel='x', ylabel='y')
    if numf == 1:
        plt.title(r'$f(x) = sin^2(x) + 2sin^4(2x)$')
    elif numf ==2:
        plt.title(r'$f(x) = \frac{1}{1+(x−\pi)^2}$')
    elif numf ==3:
        plt.title(r'$f(x) = xe^{−x}$')
    ax.grid()
    fig.savefig("{}.png".format(numf))
    plt.show()

def graficoBarras(a,b,nomf,step=0.005,erro=0):
    """Essa função gera um gráfico de barras comparando a aproximação de cada método do valor
    exato da integral."""
    x = [1, 2] #2 Metodos
    y = [a,b]

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(x, y, color='#1F77B4')

    # ax.set_xlabel('Método', fontsize = 12)
    ax.set_ylabel('y', fontsize = 12)
    ax.set_title('Título', fontsize = 12)
    ax.set_axisbelow(True) 
    ax.yaxis.grid(True)

    plt.suptitle("Integral Definida" if erro ==0 else "Erro relativo")
    if nomf == "sen^2(x) + 2sen^4(2x)":
        plt.title(r'$sin^2(x) + 2sin^4(2x)$')
    elif nomf =="1/(1+[x−π]^2)":
        plt.title(r'$\frac{1}{1+(x−\pi)^2}$')
    elif nomf =="xe^{−x}":
        plt.title(r'$xe^{−x}$')

    ax.set_xticks(x)
    ax.set_xticklabels(('Regra dos Trapézios', 'Regra de Simpson'))

    plt.ylim(b-step, b+step) #valor limite do eixo y

    plt.savefig('graf.png',bbox_inches='tight') #salva o gráfico
    plt.show()



def g1(x,y1,y2,nomeFuncao):
    """Essa função plota um gráfico de linhas que mostra os valores retornados 
    pelos métodos tendendo ao valor exato da integral."""
    ###################################### Gráfico 1 ######################################
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y1, label='Regra dos Trapézios',lw=2, markersize=8, color='#9467BD', marker='D', markeredgecolor='#9467BD', markerfacecolor='#C9B3DE')
    ax.plot(x, y2, label='Regra de Simpson', lw=2, markersize=8, color='#1F77B4', marker='o', markeredgecolor='#1F77B4', markerfacecolor='#8FBBD9')
    #Legenda
    handles, labels = ax.get_legend_handles_labels()
    leg = ax.legend(handles, labels, bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
    
    ax.set(xlabel='Subintervalos', ylabel='Valor aproximado')
    plt.subplots_adjust(left=0.1, right=0.78, top=0.9, bottom=0.1) #Tive de inserir esse trecho de código para a legenda ficar dentro da imagem, ela estava cortando
    if nomeFuncao == "sen^2(x) + 2sen^4(2x)":
        plt.title(r'$sin^2(x) + 2sin^4(2x)$')
    elif nomeFuncao =="1/(1+[x−π]^2)":
        plt.title(r'$\frac{1}{1+(x−\pi)^2}$')
    elif nomeFuncao =="xe^{−x}":
        plt.title(r'$xe^{−x}$')
        
    ax.grid()
    
    plt.savefig('1.png',bbox_inches='tight') #salva o gráfico
    plt.show()

def g2(x,y1,y2,nomeFuncao,intDefinida): #Igual a g1, entretanto com o zoom aplicado e com uma linha horizontal verde no valor exato da integral, mostrando os valores retornados pelos métodos tendendo ao valor exato.
    """Essa função plota um gráfico de linhas que mostra os valores retornados 
    pelos métodos tendendo ao valor exato da integral. Ela apresenta uma linha verde que indica a integral definida
    e possui um zoom para que seja mais fácil notar a diferença dos dois métodos."""
    ###################################### Gráfico 2 ######################################
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y1, label='Regra dos Trapézios', lw=2, markersize=8, color='#9467BD', marker='D', markeredgecolor='#9467BD', markerfacecolor='#C9B3DE')
    ax.plot(x, y2, label='Regra de Simpson',    lw=2, markersize=8, color='#1F77B4', marker='o', markeredgecolor='#1F77B4', markerfacecolor='#8FBBD9')
    plt.axhline(y=intDefinida,label='Integral Definida', linestyle='-',lw=2, markersize=8, color='#099C38')
    
    #Legenda
    handles, labels = ax.get_legend_handles_labels()
    leg = ax.legend(handles, labels, bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
    
    ax.set(xlabel='Subintervalos', ylabel='Valor aproximado (zoom)')
    plt.subplots_adjust(left=0.1, right=0.78, top=0.9, bottom=0.1) #Tive de inserir esse trecho de código para a legenda ficar dentro da imagem, ela estava cortando
    
    if nomeFuncao == "sen^2(x) + 2sen^4(2x)":
        plt.title(r'$sin^2(x) + 2sin^4(2x)$')
    elif nomeFuncao =="1/(1+[x−π]^2)":
        plt.title(r'$\frac{1}{1+(x−\pi)^2}$')
    elif nomeFuncao =="xe^{−x}":
        plt.title(r'$xe^{−x}$')
    
    ax.grid()
    plt.xlim(6,50)
    
    plt.savefig('2.png',bbox_inches='tight') #salva o gráfico
    plt.show()
    #####################################################################################
    
def g3(x,y1,y2,nomeFuncao,intDefinida,f):
    """Essa função plota um gráfico de linhas que mostra os valores dos erros relativos a cada método
    e mostra eles tendendo a zero, à medida que o número de subintervalos se torna muito grande."""
    ###################################### Gráfico 3 ######################################

    erroRelativoT = list(map(lambda n: f(n,intDefinida),y1)) #Utilizei o map pois fica mais curto e simples de fazer
    erroRelativoS = list(map(lambda n: f(n,intDefinida),y2)) #Utilizei o map pois fica mais curto e simples de fazer

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, erroRelativoT, label='Regra dos Trapézios', lw=2, markersize=8, color='#9467BD', marker='D', markeredgecolor='#9467BD', markerfacecolor='#C9B3DE')
    ax.plot(x, erroRelativoS, label='Regra de Simpson',    lw=2, markersize=8, color='#1F77B4', marker='o', markeredgecolor='#1F77B4', markerfacecolor='#8FBBD9')
            
    #Legenda
    handles, labels = ax.get_legend_handles_labels()
    leg = ax.legend(handles, labels, bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
    
    ax.set(xlabel='Subintervalos', ylabel='Erro relativo')
    plt.subplots_adjust(left=0.1, right=0.78, top=0.9, bottom=0.1) #Tive de inserir esse trecho de código para a legenda ficar dentro da imagem, ela estava cortando
    
    if nomeFuncao == "sen^2(x) + 2sen^4(2x)":
        plt.title(r'$sin^2(x) + 2sin^4(2x)$')
    elif nomeFuncao =="1/(1+[x−π]^2)":
        plt.title(r'$\frac{1}{1+(x−\pi)^2}$')
    elif nomeFuncao =="xe^{−x}":
        plt.title(r'$xe^{−x}$')
    
    ax.grid()
    
    plt.savefig('3.png',bbox_inches='tight') #salva o gráfico
    plt.show()
    #####################################################################################
    
def g4(x,y1,y2,nomeFuncao,intDefinida,f):
    """Essa função plota um gráfico de linhas com o zoom aplicado em um ponto específico que mostra os valores dos erros relativos a cada método
    e mostra eles tendendo a zero, à medida que o número de subintervalos se torna muito grande."""
    ###################################### Gráfico 3 ######################################

    erroRelativoT = list(map(lambda n: f(n,intDefinida),y1)) #Utilizei o map pois fica mais curto e simples de fazer
    erroRelativoS = list(map(lambda n: f(n,intDefinida),y2)) #Utilizei o map pois fica mais curto e simples de fazer

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, erroRelativoT, label='Regra dos Trapézios', lw=2, markersize=8, color='#9467BD', marker='D', markeredgecolor='#9467BD', markerfacecolor='#C9B3DE')
    ax.plot(x, erroRelativoS, label='Regra de Simpson',    lw=2, markersize=8, color='#1F77B4', marker='o', markeredgecolor='#1F77B4', markerfacecolor='#8FBBD9')
            
    #Legenda
    handles, labels = ax.get_legend_handles_labels()
    leg = ax.legend(handles, labels, bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
    
    ax.set(xlabel='Subintervalos', ylabel='Erro relativo (zoom)')
    plt.subplots_adjust(left=0.1, right=0.78, top=0.9, bottom=0.1) #Tive de inserir esse trecho de código para a legenda ficar dentro da imagem, ela estava cortando
    
    if nomeFuncao == "sen^2(x) + 2sen^4(2x)":
        plt.title(r'$sin^2(x) + 2sin^4(2x)$')
    elif nomeFuncao =="1/(1+[x−π]^2)":
        plt.title(r'$\frac{1}{1+(x−\pi)^2}$')
    elif nomeFuncao =="xe^{−x}":
        plt.title(r'$xe^{−x}$')
    
    ax.grid()
    plt.xlim(6,50)
    
    
    plt.savefig('4.png',bbox_inches='tight') #salva o gráfico
    plt.show()
    #####################################################################################
    
def g5(x,y1,y2,nomeFuncao,intDefinida,f):
    """Essa função plota um gráfico de barras que indica o erro relativo de cada método. Como o erro relativo do método
    dos trapézios é maior, muitas vezes o erro relativo de Simpson nem aparece no gráfico, enquanto a regra dos trapézios
    já excedeu o gráfico."""
    ###################################### Gráfico 3 ######################################

    erroRelativoT = list(map(lambda n: f(n,intDefinida),y1)) #Utilizei o map pois fica mais curto e simples de fazer
    erroRelativoS = list(map(lambda n: f(n,intDefinida),y2)) #Utilizei o map pois fica mais curto e simples de fazer

    x = [1, 2] #2 Metodos
    y = [erroRelativoT[len(erroRelativoT)-1], erroRelativoS[len(erroRelativoS)-1]] #alguma dado de cada método

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(x, y, color='#1F77B4')

    # ax.set_xlabel('Método', fontsize = 12)
    ax.set_ylabel('Erro relativo', fontsize = 12)
    if nomeFuncao == "sen^2(x) + 2sen^4(2x)":
        plt.title(r'$sin^2(x) + 2sin^4(2x)$')
        plt.ylim(0, 0.000000000000001) #valor limite do eixo y
    elif nomeFuncao =="1/(1+[x−π]^2)":
        plt.title(r'$\frac{1}{1+(x−\pi)^2}$')
        plt.ylim(0, 0.0000001) #valor limite do eixo y
    elif nomeFuncao =="xe^{−x}":
        plt.title(r'$xe^{−x}$')
        plt.ylim(0, 0.00001) #valor limite do eixo y
    ax.set_axisbelow(True) 
    ax.yaxis.grid(True)

    ax.set_xticks(x)
    ax.set_xticklabels(('Regra dos Trapézios', 'Regra de Simpson'))

    plt.savefig('5.png',bbox_inches='tight') #salva o gráfico
    plt.show()
    #####################################################################################