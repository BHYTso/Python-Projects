#Collatz - trial code

#Write a function named collatz() that has one parameter named number.
#If number is even, then collatz() should print number // 2 and return this value.
#If number is odd, then collatz() should print and return 3 * number + 1.
#Then write a program that lets the user type in an integer and that keeps calling collatz()
#    on that number until the function returns the value 1.
#(Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1!
#Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called
#    “the simplest impossible math problem.”)
#Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.
#Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.





def collatz(number):
    '''int -> int

    Return integer number if even or odd, printing //2 or 3*number+1
    given number integer

    >>>collatz(4)
    2
    >>>collatz(20)
    10
    >>>collatz(7)
    22
    >>>>>collatz(11)
    34
    >>collatz(3) #repeated collatz n times till value of 1.
    3
    10
    5
    16
    8
    4
    2
    1
    
    '''
    if number%2 == 0:
        print(number//2)
    else:
        print(3*number+1)

        
'''
print('Please input any integer.')
INTGR = int(input())

for sequence in range (0,100):
    sequence = collatz(INTR)
        

    if sequence !=1:
        collatz(even)
        print (even)
    else:
        collatz(odd)
        print (odd)

    else:
        break    #Value reaches 1

print ('1')
'''
        
        
