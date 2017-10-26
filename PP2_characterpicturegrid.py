#Comma Code

def commacode(N):
    '''str -> str

    Return takes a list value as an argument and
    returns
    a string with all the items separated by a comma and a
    space, with and inserted before the last item.


    >>>commacode(spam) = ['apples', 'bananas', 'tofu', 'cats']
    'apples, bananas, tofu, and cats'
    >>>commacode(spam) = ['A', 'B', 'C, 'D']
    'A, B, C, and D'

    '''


    spam = ['apples', 'bananas', 'tofu', 'cats']

    N = spam.insert(3,'and')
    
    return N





