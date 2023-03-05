import os
wer = ["apple", "banana", "cherry", "durian"]

with open("qwe3.txt", "w") as fi:
    for i in wer:
        fi.write(i + "\n")

rew= open("qwe3.txt", "r")
rew.read()