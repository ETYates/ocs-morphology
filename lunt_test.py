from inflector import Inflector

def main():
	inflexion = Inflector()
	paradigms = open("lunt_paradigms.txt", "r")
	inflexion.conjugate("prositi", "p")
	lexicon = []
	count = 0
	incorrect = 0
	for test in paradigms:
		test = test.split(" ")
		lemma = test[0]
		parse = test[1]
		form = test[2].rstrip("\n")
		"""
		if parse[0] == "p":
			generated = inflexion.generate(lemma, parse)
			if generated != form:
				print("lemma:", lemma)
				print("parse:", parse)
				print("form:", form)
				print("generated:", generated)
				print()
				incorrect += 1
			count += 1
		"""
		if lemma not in lexicon:
			lexicon.append(lemma)
	# print(str(incorrect) + "/" + str(count))

	for word in lexicon:
		inflexion.conjugate(word, "p")




		

main()
