import os
wer = ["apple", "banana", "cherry", "durian"]

with open("qqqqq1.txt", "w") as fi:
    for i in wer:
        fi.write(i + "\n")

rew= open("qqqqq1.txt", "r")
rew.read()