class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return 0
        queue = deque([])
        queue.append(root)
        frequencies = {}
        while queue:
            cur_node = queue.pop()
            if cur_node:
                cur_val = cur_node.val
                if cur_val in frequencies:
                    frequencies[cur_val] += 1
                else:
                    frequencies[cur_val] = 1
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        list_of_most_common = sorted(frequencies.items(), key=lambda x: x[1])
        _, biggest_freq = list_of_most_common[-1]
        return [key for key, freq in list_of_most_common if freq == biggest_freq]
