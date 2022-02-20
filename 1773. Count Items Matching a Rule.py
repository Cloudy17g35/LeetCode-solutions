class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        count = 0
        
        for item in items:
            item_type, color, name = item
            if ruleKey == 'type' and item_type == ruleValue:
                count += 1
            elif ruleKey == 'color' and color == ruleValue:
                count += 1
            elif ruleKey == 'name' and name == ruleValue:
                count += 1
                
        return count
