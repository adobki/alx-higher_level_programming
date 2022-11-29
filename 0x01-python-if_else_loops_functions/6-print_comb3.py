#!/usr/bin/python3
for num1 in range(8):
    for num2 in range(num1 + 1, 10):
        if num1 != num2:
            print(f"{num1}{num2}", end=", ")
print(89)
