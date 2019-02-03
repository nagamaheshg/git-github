msg = 'Hello World!'
print(msg)
print(len(msg))
print(msg.upper()+' '+msg.lower()+' '+str(msg.count('l'))+' '+str(msg.find('H'))+' '+msg.capitalize())

new_msg = msg.replace('World','Universe')
print(new_msg)

name = 'Naga Mahesh Gatta'
greetings = 'Welcome!'

wish = '{}, {}'.format(greetings, name)
print(wish)
wish = f'{greetings}, {name}'
print(wish)
# print(dir(msg))

# Slicing

my_list = [0,1,2,3,4,5,6,7,8,9]

# list[start:end:step]
print(my_list[0:6])
print(my_list[-10:6])
print(my_list[0::2])

# sample_url

sample_url = "http:coreyms.com"
print(sample_url)
# reterive top domain
print(sample_url[-4:])
# reterive the http from the sample_url
print(sample_url[0:4])
# reterive the url without http:// or the top level domain
print(sample_url[5:-4])

# string formatting
