import random
import string

pass_length=10
values= string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

#list comprehension:
res= "".join([random.choice(values) for i in range(pass_length)])
print(res)


password=""
for value in range(pass_length):
    password += random.choice(values)

print("Your password is :", password)

