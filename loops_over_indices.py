def shift_left(L):
    '''(list) -> NoneType

    Shift each item in L one position to the left
    and shift the first item to the last position.

    >>>L = ['a', 'b', 'c','d']
    ['b', 'c', 'd', 'a']

    Precondition: len(L) >=1
    '''

    first_item = L[0]

    for i in range(1, len(L)):
        L[i-1] = L[i]

    L[-1] = first_item
    




def count_adjacent_repeats(s):
    '''(str) -> int

    Return the number of occurrences of a character and
    an adjacent character being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    
    repeats = 0

    for i in range(len(s)-1): #pass over each character
        if s[i] == s[i+1]:
            repeats = repeats+1

    return repeats
    

    #for loop compare current character to previous one
    
    '''repeats = 0

    for i in range(1, len(s)): #pass over each character
        if s[i] == s[i-1]:
            repeats = repeats+1

    return repeats
    '''
    

