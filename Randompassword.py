#Code for Random Password
import random 

lower = 'qwertyuiopasdfghjklzxcvbnm'
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'
symbols = '~!@#$%^&*()_+-={}[]:";,./<>?'

all = lower + upper + numbers + symbols 
length = int(input('Enter your password length: '))
password = "".join(random.sample(all, length))
print(password)
