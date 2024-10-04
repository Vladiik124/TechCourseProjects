#Float to binary

def negativeBinary(str):
    flip = str.replace("0", "2").replace("1", "0").replace("2", "1")
    negative_value = bin(int(flip, 2) + 1)[2:]
    return negative_value.zfill(8)

FloatValue = float(input("Enter float value: "))
FloatValue = int(FloatValue)

binary = bin(FloatValue & 0xFF)[2:].zfill(8)


# Print the binary numbers
print(f"positive binary: {binary}")
print(f"negative binary: {negativeBinary(binary)}")
