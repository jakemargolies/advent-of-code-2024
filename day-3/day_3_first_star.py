import re

result = 0

with open("input.txt") as file:
    for line in file:
        # Extract valid mul(x,y) pairs
        matches = re.findall(r"mul\(\s*([0-9]+)\s*,\s*([0-9]+)\s*\)", line)

        # Sum up the products of all valid pairs
        for prod1, prod2 in matches:
            result += int(prod1) * int(prod2)

print("Final Result:", result)
