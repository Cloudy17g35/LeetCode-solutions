import textwrap
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        string = s
        while len(string) % k != 0:
            string += fill

        return textwrap.wrap(string, k)
