'''
Asks for an input from the user as a mark.
If the mark is greater that 85 print "Distinction"
If the mark is between 65 and 85 print "Pass"
Anything else print "Fail"
'''

mark = int(input('Enter mark: '))


if mark >= 85:
   print("Distinction") 
elif mark >= 65:
    print("Pass")
else:
    print("Fail")


'''
if mark >= 65 and mark < 85:
    print("pass")

if mark < 65:
    print("Fail")
'''



