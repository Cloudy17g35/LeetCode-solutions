def palindrome(num,s):
    
    if not isinstance(num, int) or not isinstance(s, int) or num < 0 or s < 0:
        return 'Not valid'
    
    r = []
    
    while s:
        str_num: str = str(num)
        if len(str_num) != 1 and str_num == str_num[::-1]:
            r.append(int(str_num))
            s -= 1
        
        num += 1
        
    return r
      
