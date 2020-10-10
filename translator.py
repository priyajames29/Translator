from translate import Translator

with open('./translator.txt', mode = 'r') as my_file:
	text = my_file.read()	
	print(text)
	t = Translator(to_lang="es")
	new_text = t.translate(text)
	print(new_text)


my_file.close()
