import os
wer = ["apple", "banana", "cherry", "durian"]

with open("qqqqq.txt.txt", "w") as fi:
    for i in wer:
        fi.write(i + "\n")

rew= open("qqqqq.txt.txt", "r")
rew.read()