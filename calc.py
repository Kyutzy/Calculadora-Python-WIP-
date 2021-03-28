#importação das bibliotecas
from tkinter import *

#inicialização das variáveis
numero = [0]
nada = ""
label = ""
labels = []
a_int = 0
elementos = []
operacao = ""
numero1 = 0
numero2 = 0


def update(): #essa função atualiza o "display da calculadora"
    global label
    label = Label(root, text=a_int, font=("ubuntu", 30)) #esse é o display da calculadora em si, ele pega o número processado e escreve na tela
    labels.append(label) #coloca o número que foi acrescentado na lista de números
    label.place(x=220, y=30) #coloca o display no lugar
    cebola() #chama a função de conversão para algo que eu possa usar


def cebola(): #essa função converte a lista numero em um número que eu possa usar
    global a_int #modifico o a_int global
    a = [str(integer) for integer in numero] #transformo cada inteiro da lista numero em uma string ex: [1,2,3] vira ["1", "2", "3"]
    a_string = "".join(a) #pego todas as strings da lista, junto elas em uma frase e transformo a lista em string ex: ["1", "2", "3"] vira "123"
    a_int = int(a_string) #pego a string e transformo em número ex "123" vira 123
    print(a_int) #imprimo no terminal o número


def veja(): #essa função limpa o "display"
    global labels #modifico a função global "labels"
    #print ("veja") #debug
    for label in labels: #para cada número no display faça
        Label.destroy(label) #limpe os números no display


def reset(): #essa função corresponde ao "C" calculadora
    global numero #mexa na variável global "numero"
    global elementos #mexa na variável global "elementos"
    numero = [0] #numero vira 0 exemplo [134] vira [0]
    elementos = [] #elementos vira uma lista vazia exemplo [321,432,0] vira []
    update() #chama a função de atualização para atualizar o a_int para 0
    veja() #limpa a tela
    update() #chama a função de atualização para escrever 0 na tela

# a partir daqui eu tenho as funções que definem os números na calculadora e são todas iguais, só o zero é relevante
def zero(): # essa função diz ao construtor da calculadora que o usuário pressionou o botão zero
    riptide = 0 #botão pressionado foi o zero
    geral(riptide) #leve o zero para o construtor


def um():
    riptide = 1
    geral(riptide)


def dois():
    riptide = 2
    geral(riptide)


def tres():
    riptide = 3
    geral(riptide)


def quatro():
    riptide = 4
    geral(riptide)


def cinco():
    riptide = 5
    geral(riptide)


def seis():
    riptide = 6
    geral(riptide)


def sete():
    riptide = 7
    geral(riptide)


def oito():
    riptide = 8
    geral(riptide)


def nove():
    riptide = 9
    geral(riptide)


def igual(): #essa função tem por objetivo definir os números e realizar os cálculos
    #alteração nas globais-------------------
    global operacao
    global elementos
    global a_int
    global numero
    #----------------------------------------
    
    elementos.insert(1, a_int) #coloca o segundo número digitado na segunda casa na lista elementos

    numero1 = elementos[0] #pega o primeiro valor da lista elementos e chama de numero1 ex: elementos = [132(numero1), 123]
    numero2 = elementos[1] #pega o segundo valor da lista elementos e chama de numero2 ex: elementos = [132(numero1), 123(numero2)]
    print(elementos)
    #realiza a operação de acordo com os botões pressionados pelo usuário
    if operacao == "+":
        a_int = numero1 + numero2
    elif operacao == "-":
        a_int = numero1 - numero2
    elif operacao == "/":
        if numero2 == 0:
            a_int = "Erro"
        else:
            a_int = numero1 / numero2
    elif operacao == "*":
        a_int = numero1 * numero2

    elementos = [] #zera a lista, de elementos ex: [123,321] vira []
    numero = [0] # zera o numero ex: [1,2,3] vira [0]
    elementos.append(a_int) #adiciona na lista de elementos o resultado da operação ex: [] vira [444]
    print("teste:", a_int) #imprime o resultado da operação
    veja() #limpa o display
    update() #adiciona o resultado na tela


def geral(riptide): #esse é o construtor, aqui o número é adicionado à lista para ser convertido pela função cebola
    numero.append(riptide) #adiciona um algarismo a lista de número ex: [0] depois que o usuário pressiona um número, a lista vira [0,n] e assim por diante 
    print(numero) #debug, imprime a lista de números
    update() #converte o número [1,2,3,4] para 1234
    update() #escreve o número no display


def mundo(): #essa é a função global dos cálculos, acho que o cérebro da calculadora
    global operacao # mudar a variável operação global
    global a_int # mudar a variável a_int global
    global numero # mudar a variável numero global
    global elementos # mudar a variável elementos global

    elementos.append(a_int) # adiciona o valor a sofrer alteração na lista de elementos
    numero = [0] # zera o número
    a_int = 0 # zera o resultado
    print(elementos) #escreve a lista de elementos no terminal 

    veja() # limpa o display
    update() # escreve zero no display
    

#a partir daqui tudo é relacionado a função mundo, é a definição da operação desejada
def soma():
    global operacao
    operacao = "+"
    mundo()


def subtracao():
    global operacao
    operacao = "-"
    mundo()


def divisao():
    global operacao
    operacao = "/"
    mundo()


def multiply():
    global operacao
    operacao = "*"
    mundo()


def apagar():
    global numero
    numero = [0]
    update()
    veja()
    update()


root = Tk()
root.geometry("500x600")
root.resizable(0, 0)
update()

botao0 = Button(root, text="0", font=("ubuntu", 30), command=zero)
botao0.place(x=200, y=400)

botao1 = Button(root, text="1", font=("ubuntu", 30), command=um)
botao1.place(x=100, y=100)

botao2 = Button(root, text="2", font=("ubuntu", 30), command=dois)
botao2.place(x=200, y=100)

botao3 = Button(root, text="3", font=("ubuntu", 30), command=tres)
botao3.place(x=300, y=100)

botao4 = Button(root, text="4", font=("ubuntu", 30), command=quatro)
botao4.place(x=100, y=200)

botao5 = Button(root, text="5", font=("ubuntu", 30), command=cinco)
botao5.place(x=200, y=200)

botao6 = Button(root, text="6", font=("ubuntu", 30), command=seis)
botao6.place(x=300, y=200)

botao7 = Button(root, text="7", font=("ubuntu", 30), command=sete)
botao7.place(x=100, y=300)

botao7 = Button(root, text="8", font=("ubuntu", 30), command=oito)
botao7.place(x=200, y=300)

botao8 = Button(root, text="9", font=("ubuntu", 30), command=nove)
botao8.place(x=300, y=300)

botaoc = Button(root, text="C", font=("ubuntu", 30), command=reset)
botaoc.place(x=100, y=400)

botao_igual = Button(root, text="=", font=("ubuntu", 30), command=igual)
botao_igual.place(x=300, y=400)

botao_soma = Button(root, text="+", font=("ubuntu", 30), command=soma,
                    width=2)
botao_soma.place(x=400, y=100)

botao_sub = Button(root, text="-", font=("ubuntu", 30), command=subtracao,
                   width=2)
botao_sub.place(x=400, y=200)

botao_multiply = Button(root, text="x", font=("ubuntu", 30), command=multiply,
                        width=2)
botao_multiply.place(x=400, y=300)

botao_divisao = Button(root, text="÷", font=("ubuntu", 30), command=divisao,
                       width=2)
botao_divisao.place(x=400, y=400)

botao_excluir = Button(
    root, text="<-", font=("ubuntu", 30), command=apagar, height=7)
botao_excluir.place(x=15, y=110)

root.mainloop()
