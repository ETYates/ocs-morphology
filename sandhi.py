# Ethan Yates
# sandi.py
# 8-8-19

import json
class Sandhi:

	def __init__(self):
		rules = open("changes.json", "r")
		self.softening = json.load(rules)

	def affix(self, stem, ending, cl, parse):
		suffix = self.__process_suffix(ending, cl)
		stem = self.__process_stem(stem, cl, suffix)
		form = stem + suffix
		form = form.replace("0", "")
		return form

	def get_cons(self, stem):
		ends = "kgxcʒskzgtdszstzdpbvmlrnsnznsl"
		if stem[-2:] in ends:
			return stem[-2:]
		elif stem[-1:] in ends:
			return stem[-1:]

	def __process_suffix(self, ending, cl):
		ending = ending[1:-1]
		a = ending.split("-")
		b = a[0]
		c = a[1]
		if "/" in b:
			b = b.split("/")
			d = b[0]
			# print(b)
			e = b[1]
			if cl in "ě+i+X-ě+":                
				suffix = e + c
				print(e + "-" + c + "}")
			else:
				suffix = d + c
				print(d + "-" + c + "}")
		else:
			suffix = b + c
			print(b + "-" + c + "}")
		return suffix

	def __process_stem(self, stem, cl, suffix):
		if stem[-1:] in "ǫęěaeiouьъ":
			stem = stem[:-1]
		if cl == "ova+":
			stem = stem[:-2] + "uj"
		if cl == "Ca+":
			f  = self.get_cons(stem)
			stem = stem[:-len(f)] + self.softening[f]
		if stem[-1:] == "j" and suffix[0] == "e":
			stem = stem[:-1]
		if cl in "i+ě+" and suffix == "0ǫ":
			f = self.get_cons(stem)
			stem = stem[:-len(f)] + self.softening[f]
		return stem