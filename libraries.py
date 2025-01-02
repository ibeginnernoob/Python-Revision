from random import choice
from sys import argv,exit

import cowsay

coin=choice(["heads","tails"])

print(coin)

if len(argv)<2 :
    exit("Too few arguments!")

for arg in argv[1:]:
    print("Hello,",arg)

cowsay.trex("Hello world!")