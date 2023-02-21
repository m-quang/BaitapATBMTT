from Utils import *

du_lieu = {}

class TinyRC4:
    def __init__(self):
        self.S = [0, 1, 2, 3, 4, 5, 6, 7]
        self.T = [0, 0, 0, 0, 0, 0, 0, 0]
        self.K = []
        self.keyStream = []
        self.plainTextInt = 0
        self.plainTextLength = 0

    def StreamGeneration(self, key: list) -> list:  
        for i in range(len(key)):
            key[i] = int(key[i])
        self.K = key
        # khoi tao
        self.keyStream.clear()
        for i in range(0, 8):
            self.S[i] = i
            self.T[i] = self.K[i % len(self.K)]
        # hoan vi day S
        du_lieu["Hoán vị"] = ""
        j = 0
        for i in range(0, 8):
            j = (j + self.S[i] + self.T[i]) % 8
            self.S[i], self.S[j] = self.S[j], self.S[i]
            du_lieu["lần hoán vị thứ " + str(i+1)] = list(self.S)
        # sinh so
        du_lieu["--------------"] = ""
        du_lieu["Sinh số"] = ""
        j = 0; i = 0; a = 0
        while (len(self.keyStream) < self.plainTextLength):
            i = (i + 1) % 8
            j = (j + self.S[i]) % 8
            self.S[i], self.S[j] = self.S[j], self.S[i]
            t = (self.S[i] + self.S[j]) % 8
            k = self.S[t]
            self.keyStream.append(k)
            du_lieu["lần thứ " + str(a+1)] = list(self.S)
            a += 1
        return self.keyStream

    def encrypt_int(self, plainText: int, plainTextLength: int, key: list) -> int:
        self.plainTextLength = plainTextLength
        self.plainTextInt = plainText
        keyStream = self.StreamGeneration(key)
        result = plainText ^ ToDecimal(keyStream)
        return result

    def decrypt_int(self, plainText: int, plainTextLength: int, key: list) -> int:
        self.plainTextLength = plainTextLength
        self.plainTextInt = plainText
        keyStream = self.StreamGeneration(key)
        result = plainText ^ ToDecimal(keyStream)
        return result

    def encrypt_str(self, plainText: str, key: list) -> int:
        self.plainTextLength = len(plainText)
        self.plainTextInt = TextToDecimal(plainText)
        keyStream = self.StreamGeneration(key)
        result = self.plainTextInt ^ ToDecimal(keyStream)
        return result

    def decrypt_str(self, plainText: str, key: list) -> int:
        self.plainTextLength = len(plainText)
        self.plainTextInt = TextToDecimal(plainText)
        keyStream = self.StreamGeneration(key)
        result = self.plainTextInt ^ ToDecimal(keyStream)
        return result

# test
# rc4 = TinyRC4()
# print(rc4.encrypt_int(70, 3, [2, 1, 3]))
# print(rc4.decrypt_int(264, 3, [2, 1, 3]))

# print(rc4.encrypt_int(70, 3, [3, 2, 1]))
# print(rc4.decrypt_int(329, 3, [3, 2, 1]))

# print(rc4.encrypt_str("bag", [2, 1, 3]))
# print(rc4.encrypt_str("aag", [2, 1, 3]))
