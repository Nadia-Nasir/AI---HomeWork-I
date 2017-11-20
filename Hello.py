def StrCount(str1):
    str1 = str1.lower() #remove this line to count case sensitive character
    s = ''
    count =0
    for i in range(0,len(str1)):
        count = 0
        if (s.find(str1[i]) == -1 and str1[i] != ' '):

            for j in range(i,len(str1)):
                 if(str1[i] == str1[j]):
                    count += 1
            s = s + str1[i]
            print(str1[i] + ' = ' + str(count))

# =====================================================
def Sq_root(a):
    y = 0
    x=3.0
    while (True):
        y = (x+a/x) / 2
        print(y)
        if y==x:
            break
        x = y

def reverseStr(str1):
    index = len(str1) - 1
    while (index != -1):
        print(str1[index], end='')
        index -= 1

import math
from math import *

def is_reverse(s1 , s2):
     if len(s1) != len(s2):
         return False
     i=0
     j=len(s2)-1

     while j>0:
         if (s1[i] != s2[j]):
             return False
         i += 1
         j -= 1

     return True

def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')
import re
def main():
    """
    s = 'NAdiaa NAdiaa Nadsiaann'

    print(contains_word(s, 'NAdiaa'))  # True
    print(contains_word(s, 'Nasir'))



    i=0
    c = str(input())
    m = re.search(c, s)
    if(m == None):
        print('(-1, -1)')
    else:
        while(re.search(c, s[i:len(s)]) != None):
            m = re.search(c, s[i:len(s)-1])
            print(m.start(),end=' ')
            print(m.end()-1)
            i = m.end()
            """

dict = {}

dict['item1'] = 1
dict['item2'] = 3
dict['item1'] +=2
print(dict)

            











if __name__ == '__main__':
  main()











