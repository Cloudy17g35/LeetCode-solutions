
'''Given a string array words, return an array of all characters that show up in all strings within the words 
(including duplicates). You may return the answer in any order.'''
class Solution:
        def commonChars(self, A):
            res = collections.Counter(A[0])
            for a in A:
                res &= collections.Counter(a)
            return list(res.elements())
