class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        letters = 'abcdefgh'
        white = set()
        black = set()
        for i in range(1,9):
            for j, l in enumerate(letters, start=1):
                if i % 2:
                    if j % 2:
                        black.add(l + str(i))
                    else:
                        white.add(l + str(i))
                else:
                    if j % 2:
                        white.add(l + str(i))
                    else:
                        black.add(l + str(i))
        condition1 = (coordinate1 in white) and (coordinate2 in white)
        condition2 = (coordinate1 in black) and (coordinate2 in black)
        return condition1 or condition2

        
