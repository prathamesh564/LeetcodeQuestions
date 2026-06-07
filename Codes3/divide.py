class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        div=int(dividend/divisor)
        return 2147483647 if div > 2147483647 else div
