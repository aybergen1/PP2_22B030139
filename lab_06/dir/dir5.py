import os
wer = ["apple", "banana", "cherry", "durian"]

with open("qwe.txt", "w") as fi:
    for i in wer:
        fi.write(i + "\n")

rew= open("qwe.txt", "r")
rew.read()