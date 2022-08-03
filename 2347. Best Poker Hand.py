def check_if_flush(suits):
    
    return len(set(suits)) == 1


def check_if_three_of_a_kind(ranks):
    
    card_count = Counter(ranks).values()
    
    for count in card_count:
        if count >= 3:
            return True
    return False

def check_if_pair(ranks):
    
    card_count = Counter(ranks).values()
    
    for count in card_count:
        if count == 2:
            return True
    return False


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if check_if_flush(suits):
            return "Flush"
        
        if check_if_three_of_a_kind(ranks):
            return "Three of a Kind"
        
        if check_if_pair(ranks):
            return "Pair"
        return "High Card"
        
