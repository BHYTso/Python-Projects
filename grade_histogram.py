import tkinter.filedialog

a1_filename = tkinter.filedialog.askopenfilename()
a1_file = open(a1_filename,'r')
for line in a1_file:
    print(line)

## Read the grades into a list
## Count the grades per range
## Write the histograms to the file

'''
0-9: *
10-19: **
20-29: ****
:
100: *
'''
