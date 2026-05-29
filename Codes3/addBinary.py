class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = bin(int(a, 2) + int(b, 2))
        print(result)
        return result[2:]
