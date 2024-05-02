# coding: utf-8
'''
Function to add colons to a mac address string.

User should input the string they want to be separated by colons
and the sctipt will return the colon-separated mac address

This function was used when formatting a large number of exported
mac addresses that did not include the colon separators.
'''
def add_colons(s):
    pairs = []
    hexcode = ''
    for i in range(len(s)):
        if i > 0:
            if i % 2 == 0:
                pairs.append(s[i-2] + s[i-1])
            elif i == len(s):
                print(s[i])
    for i in range(len(pairs)):
            hexcode += str(pairs[i]) + ':'
            
    return hexcode + s[-2] + s[-1]
    
