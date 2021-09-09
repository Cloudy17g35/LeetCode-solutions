class Solution:
    def getLucky(self,s: str, k: int) -> int:
        converted = ''.join([str(ord(char) - 96) for char in s])
        transformed = sum([int(number) for number in converted])
        k -= 1
        while k != 0:
            transformed = sum([int(number) for number in str(transformed)])
            k -= 1
        return transformed
