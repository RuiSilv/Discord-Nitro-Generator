import random
import string
import colorama

amount = int(input("How many nitro codes do you want to generate\n> "))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    file = open('Generated_Nitro.txt', "a")
    file.write(code + '\n')
    file.close()
    print(code)
    value += 1
