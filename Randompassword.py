import random 

lower = 'qwertyuiopasdfghjklzxcvbnm'
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'
symbols = '~!@#$%^&*()_+-={}[]:";,./<>?'

all = lower + upper + numbers + symbols 
lenght = int(input('Enter your password lenght: '))
password = "".join(random.sample(all, lenght))
print(password)