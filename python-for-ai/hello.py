print('Hello World')

name = 'Alice'
place = 'Wonderland'
is_hurt = False

print(f'Hello {name} from {place}' if is_hurt else f'Hello {name}')


# This is a comment
# Below is a simple example of using variables and conditional statements in Python.
first_name = 'Alex'
age = 15
gender = 'male'
online_spend = 100.50
is_online = True

# is_online = False

if is_online:
    print(f'{first_name} aged {age} is online,and he already spent {online_spend} online')
else:
    print(f'{first_name} aged {age} is offline')