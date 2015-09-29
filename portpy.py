import codecs
from sys import argv
from json import dumps, load
from os import path

DEFAULT_LANGUAGE_PATH = "lang"

class Serializable(object):

	def __init__(self):
		
		self.file = None
		
	def serialize(self, path, mode):	
		try:
			self.file = open(path, mode)
		except:
			raise FileNotFoundError()
		if self.file is not None:
			return self.file
			self.file.close()
			
class Data(Serializable):

	def __init__(self):
		Serializable.__init__(self)
		self.data = {}
		
	def __setitem__(self, key, value):
		self.data[key] = value
		
	def __getitem__(self, key):
		return self.data[key]
		
	def get_data(self):
		return self.data
		
	def write(self, path):
		self.serialize(path, "w").write(dumps(self.get_data()))
		
	def load(self, path):
		# AHHHHHHHHHHHHHHHHHHH, foda-se essa merda de encoding (Por enquanto).
		with codecs.open(path, "r", encoding="utf-8", errors="replace") as data: 
			self.data = load(data)
		
		return self.data

class Language(Data):
	
	def __init__(self, name):
		Data.__init__(self)
		self.name = name
		self.load(path.join(DEFAULT_LANGUAGE_PATH, self.name + ".txt"))

if __name__ == "__main__":

	if len(argv) > 1:
		lang_name = argv[1]
		script_path = argv[2]
		lang = Language(lang_name)
		with open(script_path, 'r') as _file:
			script = _file.read()
			for item in lang.data.items():
				if isinstance(item[1], list):
					for e in item[1]:
						script = script.replace(e, item[0])
				elif isinstance(item[1], str):
					script = script.replace(item[1], item[0])
		
		#Feio, muito feio. "Parsearei" melhor em breve.
		try:
			exec(script)
		except SyntaxError:
			try:
				exec(script.replace("elif if", "elif"))
			except SyntaxError:
				exec(script.replace("else if", "elif"))
		
	else:
		raise Exception("Please provide the name of the language file. If the file is cz.txt, for example, than type just 'cz'.")
