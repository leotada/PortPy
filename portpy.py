import sys


dicionario = [
    ['False', 'Falso'], ['None', 'Nada'], ['True', 'Verdadeiro'],
    ['as', 'como'], ['assert', 'afirmar'], ['break', 'quebrar'],
    ['class', 'classe'], ['continue', 'continuar'], ['def', 'func'], ['del', 'excluir'],
    ['elif', 'senão se'], ['else', 'senão'], ['except', 'exceto'], ['finally', 'finalmente'],
    ['for ', 'para '], ['from ', 'de '], ['if ', 'se '], ['if(', 'se('], ['import', 'importar'], [' in ', ' em '],
    [' is ', ' é '], ['nonlocal', 'nãolocal'], [' not ', ' não '], [' or ', ' ou '], ['pass', 'passar'],
    ['raise', 'levantar'], ['return', 'retornar'], ['try', 'tentar'], ['while', 'enquanto'],
    ['with', 'com'], ['print', 'escrever', 'imprimir'], [' and ', ' e ']
    ]

with open(sys.argv[1], 'r') as arquivo:
    texto = arquivo.read()
    for keyword in dicionario:
        if len(keyword) <= 2:
            texto = texto.replace(keyword[1], keyword[0])
        else:  # se tiver mais de uma palavra
            for i in range(1, len(keyword)):
                texto = texto.replace(keyword[i], keyword[0])
    exec(texto)
