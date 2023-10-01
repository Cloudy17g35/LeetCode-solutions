class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        result = 0

        for num in range(low, high + 1):
            num_as_str = str(num)
            if len(num_as_str) % 2 == 0:
                first_part, second_part = ''.join(split(num_as_str[:len(num_as_str) // 2])), ''.join(split(num_as_str[len(num_as_str) // 2:]))
                if sum([int(n) for n in first_part]) == sum([int(n) for n in second_part]):
                    result += 1

        return result
        
