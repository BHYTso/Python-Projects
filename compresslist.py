def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent
    pairs of string elements
    from L concatenated together,
    starting with indices 0 and 1,    2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        # MISSING CODE HERE
        i = i+2
        
    return compressed_list

def sum_list(L):

    
    '''(list of int) -> int

    Return the sum value of list of even
    numbers between 524 till 10508 inclusive (while and for loop)

    Precondition:i starts with 524, skips 2 steps, include 10508


    >>>sum_list(524, 526, 528......10508):
    ?
    '''

    '''
    num = 524
    total = 0

    while num<=10508:
        total = total + num
        num =num + 2

        print(total)

    '''

    total = 0
    for num in range (2,10,2):
        total = total+num

    print (total)   #total aliased to L 
        
        

    
