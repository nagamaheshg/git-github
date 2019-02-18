st = 'print only the words that start with s in this sentence'
stringList = []

for word in st.split():
	stringList.append(word)
	if word.startswith('s') == True:
		print(word)
print(stringList)
print('\n')

for num in range(0,10,2):
	print(num)
print('\n')


number = [num for num in range(1,50) if num%3 == 0]
print(number)
print('\n')

st = 'print every word in this sentence that has an even number of letters'
word_list = []
for word in st.split():
	word_list.append(word)
	if len(word)%2 == 0:
		print(f'{word} and length of the word {len(word)} even')
		print('\n')
print(word_list)

integers_list = []
for num in range(1,100):
	integers_list.append(num)
	if num % 3 == 0 and num % 5 == 0:
		print(f'{num} is fizzBuzz')
	elif num % 3 == 0:
		print(f'{num} is multiple by 3 Fizz')
	elif num % 5 == 0:
		print(f'{num} is multiple by 5 Buzz')
	else:
		print(num)
print(integers_list)
print('\n')

st = 'Create a list of the first letters of every word in this string'
string_list = [string[0] for string in st.split()]
print(string_list)