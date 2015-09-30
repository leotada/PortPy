# coding: utf-8
import os, sys

from setuptools import setup
from setuptools.command.install import install as _install


def _post_install(install_lib):
    import shutil
    shutil.copy('portpy.pth', install_lib)

class install(_install):
    def run(self):
        self.path_file = 'portpy'
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Running post install task")

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = (
        "PortPy interpreta códigos Python escritos em português, "
        "para estudantes de programação, assim como Portugol. "
        "Aceita as palavras mais comuns. Funciona com Python 2 e 3.")


__version__ = "0.1.0"


setup(
    cmdclass={'install': install},
    name="PortPy",
    license="GPL3",
    version=__version__,
    download_url='git@github.com:leotada/PortPy.git',
    packages = ["portpy", "portpy.codec"],
    package_data = {
        'portpy': [
            'lang/*',
        ]
    },
    author = ("Leonardo Tada, Junior Tada, Ericson William, Joao Pimentel"),
    author_email='leonardo_tada@hotmail.com',
    url="https://github.com/leotada/PortPy",
    description="PortPy interpreta códigos Python escritos em português.",
    long_description=long_description,
    keywords='python string interpolation interpolate ruby codec',
    entry_points = {'console_scripts': ['portpy = portpy.portpy:main']},
)
