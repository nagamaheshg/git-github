my_list = [1, 2, 3]
for item_name in my_list:
	my_new_list = []
	my_new_list.append(item_name)
	print(my_new_list)

my_list = [1,2,3,4,5,6,7,8,9,10]

for num in my_list:
	if num % 2 == 0:
		print(str(num)+' is Even Number')
	else:
		print(str(num)+' is Odd Number')

for num in range(1,10):
	print(num)