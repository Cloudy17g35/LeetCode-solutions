class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}
        for number in range(1, n + 1):
            current_sum = sum([int(n) for n in str(number)])
            if current_sum not in groups:
                groups[current_sum]  = []
                groups[current_sum].append(number)
            else:
                groups[current_sum].append(number)
                
        maximal_size = max([len(groups[group]) for group in groups])
        
        return len([group for group in groups if len(groups[group]) == maximal_size])
