# Ethan Yates
# inflector.py
# 8-7-2019

import json
from sandhi import Sandhi

class Inflector:

    def __init__(self):
        self.endings = open("desinences.json", "r", encoding="utf-8-sig")
        self.desinences = json.load(self.endings)
        self.stem_types = open("classifiers.json", "r", encoding="utf-8-sig")
        self.classifiers = json.load(self.stem_types)

    def generate(self, lemma, parse):
        stem = self.get_stem(lemma)
        c = self.classify(stem)
        san = Sandhi()
        if parse in self.desinences:
            ending = self.desinences[parse]
            form = san.affix(stem, ending, c, parse)
            print(lemma, parse, form)
            return form
        if parse not in self.desinences:
            return
    
    def conjugate(self, lemma, tenses):
        t = tenses
        p = "123"
        n = "sdp"

        for tense in t:
            for number in n:
                for person in p:
                    parse = tense + person + number
                    self.generate(lemma, parse)

    def get_stem(self, lemma):
        if lemma.endswith("ǫtъ"):
            stem = lemma[:-3]
        if lemma.endswith("ti"):
            stem = lemma[:-2]
        return stem

    def classify(self, stem):
        ctype = ""
        for c in self.classifiers:
            if type(self.classifiers[c]) is list:
                for d in self.classifiers[c]:
                    if stem.endswith(d):
                        ctype = c
            else:
                if stem.endswith(self.classifiers[c]):
                    ctype = c
        if stem[-1:] in "aeiouǫęěъь":
            print("{" + stem[:-1] + "-" + stem[-1:] + "+", end="")
        else:
            print("{" + stem + "+", end="")

        return ctype

