class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def convert_string_to_float(s):
            replaced = s.replace(':', '.')
            return float(replaced)
        event1, event2 = [int(convert_string_to_float(e) * 1000) for e in event1], [int(convert_string_to_float(e) * 1000) for e in event2]
        
        event1, event2 = set(list(range(event1[0], event1[1] + 1))), set(list(range(event2[0], event2[1] + 1)))
        return True if event1 & event2 else False
