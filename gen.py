# generator for ascilang

# Here you can configure parameters
width=9
input = "badapple.txt"
delay = 0.04

# And here is code.
import os
target = open(input)

print(f"DELAY {delay}")
print("FLUSH")
while True:
    print("CLS")
    print("NEXTFRAME")
    for i in range(width):
        try:
            print(f"PRINT {target.readline().split()[0]}")
        except:
            pass
    if target.readline() == "":
        break
    print("FLUSH")
    print("WAIT")