# keystream to dec
def ToDecimal(list: list) -> int:
    newList = []
    dec = 0
    for i in range(0, len(list)):
        newList.append(list[i] << (len(list) - i - 1) * 3)
    for i in newList:
        dec = dec | i
    return dec


# theo bang trong slide trang 61
# A = 0
# B = 1
# C = 2
# D = 3
# E = 4
# F = 5
# G = 6
# H = 7
def TextToDecimal(text: str) -> int:
    text = text.lower()
    newText = []
    for i in text:
        match i:
            case "a":
                newText.append(0)
            case "b":
                newText.append(1)
            case "c":
                newText.append(2)
            case "d":
                newText.append(3)
            case "e":
                newText.append(4)
            case "f":
                newText.append(5)
            case "g":
                newText.append(6)
            case "h":
                newText.append(7)
            case _:
                raise "khong hop le!"

    return ToDecimal(newText)

def DecimalToBinary(binInt: int) -> str:
    binstr = bin(binInt)[2:]
    length = len(binstr)
    if length % 3 != 0:
        binstr = binstr.zfill(length + 3 - (length%3))
    return binstr

def DecimalToBinaryWithPlainText(binInt: int, plainTextLength: int) -> str:
    binstr = bin(binInt)[2:]
    length = len(binstr)
    if length % 3 != 0:
        binstr = binstr.zfill(length + 3 - (length%3))

    if len(binstr) < plainTextLength*3:
        binstr = binstr.zfill(plainTextLength*3)
    return binstr

def BinaryToText(binstr: str) -> str:
    binlist = []
    result = ""
    binstr.split()
    for i in range(len(binstr)):
        if i%3 == 0:
            binlist.append(str(binstr[i:i+3]))
    for i in binlist:
        match i:
            case '000':
                result = result + "A"
            case '001':
                result = result + "B"
            case '010':
                result = result + "C"
            case '011':
                result = result + "D"
            case '100':
                result = result + "E"
            case '101':
                result = result + "F"
            case '110':
                result = result + "G"
            case '111':
                result = result + "H"
            case _:
                raise "khong hop le!"
    return result
                



# test
# print(ToDecimal([5, 1, 7]))
# print(ToDecimal([0, 0, 2, 6, 3, 3]))

# print(TextToDecimal("bag"))
# print(TextToDecimal("aag"))

# print(BinaryToText("001000110"))

# printDecimalToBinary(70))

# print(DecimalToBinaryWithPlainText(5, 3))
# print(DecimalToBinaryWithPlainText(2443, 6))
# print(DecimalToBinaryWithPlainText(TextToDecimal("dghf"), len("dghf")))
