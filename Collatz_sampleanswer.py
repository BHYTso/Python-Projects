'''import time

number = 0

print('Enter any integer, we will apply the Collatz method to it: ')
number = int(input())

while number != 1:
    if number % 2 == 0: #if number is even
        number = number / 2
        print('Dividing by 2 because the number is even:')
    else:
        number = number * 3 + 1
        print('Multiplying by 3 and adding 1 because the number is odd:')
    time.sleep(1)
    print(str(number))
print(str(number) + ' - See, the Collatz method ends with a 1 every time!')

'''

def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result



                


try:      ##input validation
    n = input("Give me a number: ")
    
    while n != 1:
        n = collatz(int(n))

except ValueError:
    print('Error: Give me a damn integer number!')

    







