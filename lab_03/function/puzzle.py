def solve(numheads, numlegs):
    x = int((numlegs - 2 * numheads) / 2)
    y = int(numheads - x)
    ans = f"{x} rabbits,{y} chickens"
    return ans
numheads = int(input("number heads:"))
numlegs = int(input("number legs:"))
print(solve(numheads,numlegs))