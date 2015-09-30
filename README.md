# PortPy
PortPy interpreta códigos Python escritos em português, para estudantes de programação, assim como Portugol.
Aceita as palavras mais comuns. Funciona com Python 2 e 3.

* Como instalar
```
$ python setup.py install
```

Essa instalação vai adicionar o codec portpy e o executável portpy

* Como executar

- Opção 1: Usar executável
```
$ portpy exemplo.py
```

Opcionalmente, pode-se definir a lingua:
```
$ portpy pt exemplo.py
```

Quando o executável é usado, não é necessário definir codec do arquivo (opção 2)

- Opção 2: Definir codec
Ao definir o codec como portpy no topo do arquivo, basta executar o python
```python
# coding: portpy
# ou
# coding: portpy-pt
...
[resto do exemplo.py]
```

```
python exemplo.py
```

Ao definir o codec no arquivo, é possível importá-lo normalmente em outros arquivos python.

