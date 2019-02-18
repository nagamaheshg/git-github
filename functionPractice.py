def lesser_of_two_evens(a,b):
	# check the both number are evens
	arg1 = a
	arg2 = b
	if arg1 % 2 == 0 and arg2 % 2 == 0:
		if arg1 > arg2:
			return arg2
		elif arg1 < arg2:
			return arg1
		elif arg1 == arg2:
			return 'both even numbers are equal'
	elif arg1 % 2 == 0 and arg2 % 2 != 0:
		if arg1 > arg2:
			return arg1
		else:
			return arg2
	elif arg1 % 2 != 0 and arg2 % 2 == 0:
		if arg1 > arg2:
			return arg1
		else:
			return arg2


result = lesser_of_two_evens(2,4)
print(result)
result = lesser_of_two_evens(2,5)
print(result)

def animal_cracker(text):
	string = text
	string_list = string.split()
	print(string_list[0], string_list[1])
	if string_list[0][0] == string_list[1][0]:
		return True

	else:
		return False


result = animal_cracker('Levelheaded Llama')
print(result)
result = animal_cracker('Crazy Kangaroo')
print(result)

def makes_twenty(n1,n2):
	if n1 == 20 or n2 == 20:
		return True
	else:
		sum_of_two_numbers = n1 + n2
		if sum_of_two_numbers == 20:
			return True
		else:
			return False


result = makes_twenty(20,10)
print(result)
result = makes_twenty(12,8)
print(result)
result = makes_twenty(2,3)
print(result)

print('\n')

def old_macdonald(name):
	first_half = name[:3]
	second_half = name[3:]
	return first_half.capitalize()+second_half.capitalize()


result = old_macdonald('macdonald')
print(result)

def master_yoda(text):
	my_word_list = text.split()
	reversed_list = my_word_list[::-1]
	return ' '.join(reversed_list)
		
	

result = master_yoda('i am home')
print(result) 


def has_33(number_list):
	for i in range(0, len(number_list)-1):
		if number_list[i] == 3 and number_list[i+1] == 3:
			return True

	return False


result = has_33([1,3,3])
print(result)
result = has_33([1,3,1,3])
print(result)
result = has_33([3,1,3])
print(result)

def paper_doll(text):
	string = ''
	for i in text:

		string = string + i*3
	return string


result = paper_doll('hello')
print(result)
result = paper_doll('Mississippi')
print(result)

def blackjack(a,b,c):
	sum = a + b + c
	if sum <= 21:
		return sum
	else:
		total = sum - 11
		total = total + 10
		if total <= 21:
			return total
		else:
			return 'Bust'

result = blackjack(5,6,7)
print(result)
result = blackjack(9,9,9)
print(result)
result = blackjack(9,9,11)
print(result)
