def word_break(s, word_dict):
    
    """
    arguments:
    
    s: string , word_dict:list
    
    it checks if it's able to break the s with the word(s) from the list
    
    for instance:
    
    s = 'helloworld', word_dict=['hello', 'world'] will return True
    
    s = 'mama you been on my mind', word_dict = ['mama', 'you', 'been'] will return False
    
    s = 'like a rolling stone', word_dict = ['stone', 'rolling', 'like', 'a'] will return True
    
    s = 'look at the sky', word_dict = ['hello', 'sky', 'look', 'at', 'the'] will return True
    """
    
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
    
    for i in range(len(s) - 1, -1, -1):
        for w in word_dict:
            if  (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]
