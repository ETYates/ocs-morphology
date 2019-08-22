# Old-Church-Slavonic-Morphology
Parser/Generator for OCS noun and verb forms.

The data and interpretation of Old Church Slavonic morphology
are taken from Horace G. Lunt's fundamental grammar. 

This is not yet developed enough for instructions on the program's full
range of uses. However, to test the output of the program, run lunt_test.py.

The output will appear as such:

{slyš-a+0-ǫ}

slyšati p1s slyšǫ
...

The information in brackets is the morphological analysis of each 
form. A dash marks the stem boundary, while a plus sign marks a 
morphmeme boundary. 

{slyš-a+0-ǫ}

The information alternating with the bracketed 
info is the surface form of each parse. 

slyšati p1s slyšǫ

These are the lemma, parse, and generated form, respectively.
The parse p1s means "present first singular."

Most of the inflexion work is done in inflector.py.
