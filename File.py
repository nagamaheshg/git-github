text = open('text.txt')
print(text.read())

print(text.seek(0))
print(text.readlines())
text.close()

with open('text.txt') as my_new_file:
	contents = my_new_file.read()
	print(contents)