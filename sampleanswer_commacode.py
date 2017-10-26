#Commacode

'''Write a function that takes a
list value as an argument and returns
a string with all the items separated by a comma and a space,
with and inserted before the last item. For example, passing
the previous spam list to the function would return
'apples, bananas, tofu, and cats'. But your func- tion should be able
to work with any list value passed to it.'''


import random

def comma_code(subject):

     a = (len(list(subject)) - 1)

     for i in range(0, len(list(subject))):

          if i != a:
               print(str(subject[i]) + ', ', end="")

          else:
              print('and '+ str(subject[i]))            


spam = ['apples','banana','tofu','cats','monkey']





'''

def comma_code(argument):

    argument_in_string = ''
    argument_len = len(argument)
    for i in range(argument_len):
        if i == (argument_len - 1):
            argument_in_string = argument_in_string + 'and ' + argument[i]
            return argument_in_string

        argument_in_string = argument_in_string + argument[i] + ', '

spam = ['A', 'bananas', 'tofu', 'cats']
return_value = comma_code(spam)
print(return_value)
'''
