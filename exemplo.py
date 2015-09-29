

func ola(n):
    tentar:
        escrever('Olá mundo ' + str(n))
    exceto:
        passar
    finalmente:
        imprimir('fim')

contador = 0
enquanto contador < 50:
    escrever(contador)
    se contador < 3:
        escrever('menor')
    senao se contador < 10:
        escrever('medio')
    senao:
        quebrar
    contador += 1

para numero em range(3):
    ola(numero)

x = Nulo
se x mesmo que Nulo:
    x = Falso
senao:
    x = Verdadeiro
escrever(x)
