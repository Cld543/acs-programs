# coding: utf-8
'''
This script converts a binary number into a decimal number.
'''
def bin_to_dec(num):
    n = str(num)
    l = len(n)
    result = 0
    for i in range(0, l):
        result += int(n[i]) << l - i - 1
    return result
   




def is_binary(num):
	n = str(num)
	binary = '01'
	for c in n:
		if c not in binary:
			return False
	return True
 
if __name__ == '__main__':


	while True:
		user_input = str(input('Enter a binary string to convert it into a decimal: '))
		if user_input =='q':
			break
		if not is_binary(user_input): 
			print('Please enter a binary number (eg. 1001)')
			continue
		else:
			print(f'Binary = {user_input}\nDecimal = {bin_to_dec(user_input):,}')
		
	
