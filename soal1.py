def pangkat(num1, num2):
    number = 1  # initialize first that number = 1
    for _ in range(num2):   # pake for loop
        number *= num1
    return number


# Jika mau pake user input, caranya begini
'''
# asking user to input for base and power
base = int(input('Input your BASE number : '))
power = int(input('Input your POWER number : '))

# testing out the function
print(pangkat(base, power))
'''

print(pangkat(2,2))
print(pangkat(3,3))
print(pangkat(10,5))