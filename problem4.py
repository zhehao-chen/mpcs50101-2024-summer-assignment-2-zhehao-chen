def max_of_three(a,b,c):
    max = a  
    # a transparency middle value
    if (max <= b):
        max = b
        if (max <= c):
            max = c
    return max

