
print(""" we use triple if
we need      to
use
more than 1    line""")
print('------------')
learning_index= "Learning python"
print(learning_index[1])
print(learning_index[-2])
print(learning_index[1:5])
print(learning_index[1:])
print(learning_index[-2:])
print(learning_index[:2])
print(learning_index[:])
client_name= "Andromeda"
client_family="galaxy"
print(f"{client_name} uses 'f'ormat to put variables inside strings of the {client_family}.")
print(len(client_name))    #len function: will be used to count the lenght of a variable
print(client_name.lower())    #lower and upper method
print(client_name.upper())
print(client_name.find("dr"))    #to find sth inside our variable
print(client_name.replace("Andromeda", client_family))    #to replace any variable with any variable
print("meda" in client_name)    # to check if sth is inside sth
print(client_family.title())    # to make the first letter of a word capital
print('----------')
x= -2.51
print(round(x))    # it rounds the vlue
print(abs(x))     # absolute valu always result in a positive value
import math    #to import math madual to our code
print(math.ceil(x))  # it rounds up toward the positive infinity
print(math.floor(x))  # it rounds down toward hte negative infinity
# can search in google about each module to see what it has to offer

credit=input("How much money do you have:? price is 1M $ ")
credit=float(credit)
if credit>500000:
    print("You only need to put down 100k in cash.")
elif credit<=500000:
    print("you need to put down 200k in cash.")
else:
    print("You can have this")
 
weather_is_cold=True
have_jacket=True
forgot_umbrela=False

if weather_is_cold and have_jacket and not forgot_umbrela:       #not reverts the boolean value
    print("Im gonna be fine today!")


name=input("Please enter you name: ")
if len(name)<3:
    print("Your name must be at least 3 characters!")
elif len(name)>20:
    print("Your name must be less than 20 characters!")
else:
    print("welcome")




weight=input("Please enter your weight: ")
x=input("k(g) or l(bs): ")
kg=float(weight)/0.45
lbs=float(weight)*0.45
if x=="k" or x=="K":
    print(f"You are {kg} pounds!")
elif x=="l" or x=="L":
    print(f"You are {lbs} Kg!")
else:
    print("respond with 'k' or 'L'")


