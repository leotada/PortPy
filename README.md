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
$ portpy -l pt exemplo.py
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

Nota: O codec foi feito com base no Interpy: https://github.com/syrusakbary/interpy


---------------
English version
---------------

# PortPy
PortPy interprets Python codes written in other languages (Portuguese in this case) for programming students.
Accepts the most common words. Works with Python 2 and 3.

* How to install
```
$ python setup.py install
```

This installation will add the portpy codec and the portpy executable

* How to run

- Option 1: Use the executable
```
$ portpy exemplo.py
```

Optionally, you can define the language:
```
$ portpy -l pt exemplo.py
```

When the executable is used, it is not necessary to define the file's codec (option 2)

- Opção 2: Define codec
When defining the codec as portpy at the top of the file, just run python
```python
# coding: portpy
# or
# coding: portpy-pt
...
[rest of example.py]
```

```
python example.py
```

When defining the codec in the file, it is possible to import it normally into other python files.

Note: The codec was made based on Interpy: https://github.com/syrusakbary/interpy
