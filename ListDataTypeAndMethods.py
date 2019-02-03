# Example1
# animal List
animal = ['cat', 'dog', 'rabbit']
# an element is added
animal.append('guinea pig')
# updated animal list
print('Updated Animal List: ',animal)

# Example2
# animal List
animal = ['cat', 'dog', 'rabbit']
# adding another list of wild animals
wild_animal = ['tiger', 'fox']
#adding wild_animal list to a animal_list
animal.append(wild_animal)
# updated List
print('Updated List is: ',animal)

# ---------------------------------------

#Exapmple1
language = ['French', 'English', 'German']
language1 = ['spanish', 'portuguese']

language.extend(language1)
# Extended language List
print('Language List: ',language)

#Example2
# language_list
language = ['French', 'English', 'German']
# language_tuple
language1 = ('spanish', 'portuguese')
# language_set
language2 = {'chines', 'japanese'}

# appending element of language language_tuple
language.extend(list(language1))
# ----------- or ------------------------------
language.extend(language1)
print('New Language List: ',language)
# appending element of language language_set
language.extend(language2)
print('New Language List: ',language)

a = [1,2]
b = [3,4]
a += b
print(a)
# ------------------------------------------

# Insert method
#vowel list
vowel = ['a', 'e', 'i', 'u']
vowel.insert(3,'o')
print('Updated list: ', vowel)

# Inserting tuple as an element
mixed_list = [{1,2}, [5, 6, 7]]
#number_tuple
number_tuple = (3, 4)
mixed_list.insert(1,number_tuple)
print('Updated List: ', mixed_list)
# --------------------------------------------------

# Python List Count()
# random list
vowel = ['a', 'e', 'i', 'i', 'u']
count = vowel.count('i')
print('the count value of i is: ',count)
count = vowel.count('p')
print('the count value of p is: ',count)

random = ['a', (a,b), (a,b), [3,4]]
count = random.count((a,b))
print('the count value of (a,b) is: ',count)
count = random.count([3,4])
print('the count value of [3,4] is: ',count)
# ----------------------------------------------------
# pop() method
language = ['Python', 'Java', 'C++', 'French', 'C']

# Return value from pop() when 3 is passed

return_value = language.pop(3)
print('Return_value: ', return_value)
print('Updated List is: ', language)


# pop() method without an index, and for negitive indices

language = ['Python', 'Java', 'C++', 'Ruby', 'C']

# when index is not passed
print('when index is not passed: ')
print('Return value: ',language.pop())
print('Updated List: ',language)

# when -1 is passed
# pop third last element
print('\nwhen -1 index passed')
print('Return_value: ',language.pop(-1))
print('Updated List: ',language)

# when -3 is passed
# pop third last element
print('\nwhen -3 index passed')
print('Return_value: ',language.pop(-3))
print('Updated List: ',language)
