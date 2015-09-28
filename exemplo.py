
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
    senão se contador < 10:
        escrever('medio')
    senão:
        quebrar
    contador += 1

para numero em range(3):
    ola(numero)

x = Nada
se x é Nada:
    x = Falso
senão:
    x = Verdadeiro
escrever(x)
