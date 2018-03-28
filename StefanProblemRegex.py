'''
Disclaimer: For differentiation purposes, I will be using triple quotesself.
Hashtag quotes are from the assignment itself.
'''

##### Problem #####
##### CNS-380/597 - Ryan Haley####


#Write a regular expression to fit the following:
'''
I used the following website for real-time testing: http://pythex.org/.
Just because I will have to save time wherever possible in order to pass this class!!
Update:
After testing with the website, I tested with my own code.
The second and third regex did not work at first...
Debugging:
test2 - First, I realized that I forgot the dash. Then, I needed to convert \s to [\ ] to ONLY look for space.
test3 - The plus sign and the dots... Many stackoverflow sites have been browsed and many errors have been debugged...
        Eventually, the testing string was incorrect... Instead of +3 333.333.3333, I had +x 333.333.3333.
'''
import re

#1 Phone number in the format of
#  xxx-xxx-xxxx
test1 = re.compile("\d{3}\-\d{3}\-\d{4}")

#2 Phone number in the format of
#  (xxx) xxx-xxx
test2 = re.compile("\(\d{3}\)[\ ]\d{3}\-\d{3}")

#3 Phone number in the format of
#  +x xxx.xxx.xxxx
test3 = re.compile("\+\d[\ ]\d{3}\.\d{3}\.\d{4}")

#4 SSN in the format of
#  xxx-xx-xxxx or xxxxxxxxx
'''I used the following website to look up the syntax for 0 or more and then, used the regex for 0 or 1:
https://stackoverflow.com/questions/7636074/regular-expression-no-characters'''
test4 = re.compile("\d{3}[-]?\d{2}[-]?\d{4}")

teststring = 'test1 111-111-1111 test2 (222) 222-222 test3 +3 333.333.3333 test4.1 444-44-4444 test4.2 444444444 test5 1 555_555_5555; 2 (555)  555-555; 2 (555)\n555-555; 3 +5 555:555:5555; 4 555:555:5555; 4 55555555; any 555;'

firsttest = test1.findall(teststring)
secondtest = test2.findall(teststring)
thirdtest = test3.findall(teststring)
fourthtest = test4.findall(teststring)

'''print(teststring)'''
print(firsttest, secondtest, thirdtest, fourthtest)
