from tkinter import *

numero = [0]
nada = ""
label = ""
labels = []
a_int = 0
elementos = []
operacao = ""
numero1 = 0
numero2 = 0


def update():
    global label
    label = Label(root, text=a_int, font=("ubuntu", 30))
    labels.append(label)
    label.place(x=220, y=45)
    cebola()


def cebola():
    global a_int
    a = [str(integer) for integer in numero]
    a_string = "".join(a)
    a_int = int(a_string)
    print(a_int)


def veja():
    for label in labels:
        Label.destroy(label)


def reset():
    global numero
    global elementos
    numero = [0]
    elementos = []
    update()
    veja()
    update()


def zero():
    riptide = 0
    geral(riptide)


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


def igual():
    global operacao
    global elementos
    global a_int
    global numero

    elementos.insert(1, a_int)

    numero1 = elementos[0]
    numero2 = elementos[1]
    print(elementos)

    if operacao == "+":
        a_int = numero1 + numero2
    elif operacao == "-":
        a_int = numero1 - numero2
    elif operacao == "/":
        a_int = numero1 / numero2
    elif operacao == "*":
        a_int = numero1 * numero2

    elementos = []
    numero = [0]
    elementos.append(a_int)
    print("teste:", a_int)
    veja()
    update()


def geral(riptide):
    numero.append(riptide)
    print(numero)
    update()
    update()


def mundo():
    global operacao
    global a_int
    global numero
    global elementos

    elementos.append(a_int)
    numero = [0]
    a_int = 0
    print(elementos)

    veja()
    update()


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
    global labels
    ultimo = len(labels)
    
    numero = [0]
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

botao_excluir = Button(root, text="<-", font=("ubuntu", 30), command=apagar, width=2)
botao_excluir.place(x=10, y=100)

root.mainloop()
