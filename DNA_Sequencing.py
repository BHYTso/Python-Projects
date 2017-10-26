def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    >>> is_longer('ATCG', 'ATGG')
    False
    """
    if len(dna1)>len(dna2):
        return True
    else:
        return False
       
    


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    >>> count_nucleotides('', 'G')
    0
    """
    s1 = nucleotide
    s2 = dna
    return s2.count(s1)
    
    


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    >>> contains_sequence('TCCG','CG')
    True

    """

    s1 = dna1
    s2 = dna2
    if s2 in s1:
        return True
    else:
        return False

    





def is_valid_sequence(dna1):
    '''(str) -> bool

    Return True if and only if DNA sequence dna1 contains only nucleotides.


    >>>is_valid_sequence('ATCGGC')
    True
    >>>is_valid_sequence('CCG')
    True
    >>>is_valid_sequence('ATCGP')
    False
    >>>is_valid_sequence('ATCGacg')
    False
    >>>is_valid_sequence('')
    False
    '''
    ##valid_nucleotide = ''
    num_non_nucleotide = 0

    for char in dna1:
        if char not in 'ATCG':
            ##valid_nucleotide = valid_nucleotide + char
            num_non_nucleotide = num_non_nucleotide + 1

    if num_non_nucleotide>0:
        return False
    else:
        return True 

    return num_non_nucleotide

    

def insert_sequence(dna1,dna2,index):
    '''(str, str, int) -> str

    Return a new string contains
    inserted sequence with dna2 characters into dna1 sequence at
    index point.

    >>>insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>>insert_sequence('CCGG','AT',0)
    'ATCCGG'
    >>>insert_sequence('CCGG','AT',3)
    'CCGATG'

    '''
    
    return   dna1[0:index]+dna2+dna1[index:len(dna1)]

    


    #s[0:index]+s2+s[index:len(s)]
    
    ##return dna1.find(dna2)
    
    
    ##return dna1-dna2


def get_complement(nucl):
    '''(str) -> str

    Return the complement of a nucleotide
    

    >>>get_complement('A')
    'T'
    >>>get_complement('C')
    'G'
    >>>get_complement('T')
    'A'
    >>>get_complement('G')
    'C'
    >>>
    '''

    if nucl == 'A':
        return 'T'
    if nucl == 'T':
        return 'A'
    if nucl == 'C':
        return 'G'
    if nucl == 'G':
        return 'C'



    ##complement = ''
    
    ##for char in nucl:
    ##    if char in 'ATCG':
    ##        complement = complement+char




    ##if complement=='A':
    ##    return 'T'
    ##elif complement=='C':
        return 'G'
    ##elif complement=='T':
    ##    return 'A'
    ##else:
    ##    return 'C'
    
    #return complement


def get_complementary_sequence(dna1):
    '''(str) -> str

    Return the complementary dna sequence of a the given dna1 sequence
    

    >>>get_complementary_sequence('AT')
    'TA'
    >>>get_complementary_sequence('CT')
    'GA'
    >>>get_complementary_sequence('TG')
    'AC'
    >>>get_complementary_sequence('G')
    'C'
    >>>get_complementary_sequence('ACGTACG')
    'TGCATGC'
    '''
    nucl = ''

    for char in dna1:
        if char in 'ATCG':
            nucl= nucl + get_complement(char)

    
    return nucl
    



        
            

    
    
    
