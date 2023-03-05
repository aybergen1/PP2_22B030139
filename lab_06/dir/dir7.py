import os

qw =open("qqqqq.txt.txt", "r")
we =open("qqqqq.txt", "w")
for i in qw:
    we.write(str(i))
we =open("qqqqq.txt", "r")
we.read()