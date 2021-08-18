i = 0
binary = {
    0: "0000",
    1: "0001",
    2: "0010",
    3: "0011",
    4: "0100",
    5: "0101",
    6: "0111",
    7: "1000",
    8: "1001",
    9: "1011",
    10: "1111",
}

dec = str(input("Insert decimal integer: "))
print("Binary: ", end = " ")
while i != len(dec):
    print(binary.get(int(dec[i])), end = ' ')
    i += 1;