# Ethan Yates
# sandi.py
# 8-8-19

import json
class Sandhi:

	def __init__(self):
		rules = open("changes.json", "r")
		self.softening = json.load(rules)

	def affix(self, stem, ending, cl, parse):
		a = ending.split("-")
		b = a[0].replace("{", "")
		c = a[1].replace("}", "")
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
		# print(suffix)
		if stem[-1:] in "ǫęěaeiouьъ":
			stem = stem[:-1]
		if cl == "ova+":
			stem = stem[:-2] + "uj"
		if cl == "Ca+":
			f  = self.get_cons(stem)
			stem = stem[:-len(f)] + self.soften(f)
		if stem[-1:] == "j" and suffix[0] == "e":
			stem = stem[:-1]
		if cl in "i+ě+" and suffix == "0ǫ":
			f = self.get_cons(stem)
			stem = stem[:-len(f)] + self.soften(f)
		# print(stem)
		form = stem + suffix
		form = form.replace("0", "")
		return form

	def soften(self, cons):
		return self.softening[cons]

	def get_cons(self, stem):
		ends = "k-g-x-c-ʒ-sk-zg-t-d-s-z-st-zd-p-b-v-m-l-r-n-sn-zn-sl"
		if stem[-2:] in ends:
			return stem[-2:]
		elif stem[-1:] in ends:
			return stem[-1:]