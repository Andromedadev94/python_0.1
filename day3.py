
correct_num=9
remaining_guess=3
while remaining_guess>=1:  #as long as this line is true, python executes whatever in under unless we say break!
    remaining_guess=remaining_guess-1
    answer=int(input("What is 3 to the power of 3?: "))
    if answer==9:
        print("You won")
        remaining_guess=-1  #we could also type Break here. it ends the while loop instantly.
    else:
        print(f"Wrong! {remaining_guess} guesses remain.")
if remaining_guess==0:
    print("You lost!")

# -------------
car_situation=""
while True:
    user_request=input("> ")  #could also do user_request=input("> ").lower()  to make the input lower from the begining
    user_request=user_request.lower()
    if user_request=="help":
        print("""
Start - to start the car
Stop -  to Stop the car
Quit -  to exit
        """)
    elif user_request=="start" and car_situation!="starting":
        print("Car started.")
        car_situation="starting"
    elif user_request=="stop" and car_situation!="stopping":
        print("Car stopped.")
        car_situation="stopping"
    elif user_request=="quit":
        print("exiting...")
        break
    elif user_request=="start" and car_situation=="starting":
        print("car already started! ")
    elif user_request=="stop" and car_situation=="stopping":
        print("car already stopped.")
# ------

user_command=""
pc_started=False
Pc_shutdown=False
while True:
    user_command=input('> ').lower()
    if user_command=="on":
        if pc_started==True:
            print("pc is on already!")
        else:
            print("Windows is booting!")
            pc_started=True
    elif user_command=="off":
        if Pc_shutdown==True:
            print("pc is already shutdown!")
        else:
            print("windows is shutting down!")
            Pc_shutdown=True
    elif user_command=="help":
        print("""
on  > to turn on pc
off > to turn off pc
exit> to burn in hell       
        """)
    elif user_command=="exit":
        print("Initiating burning in hell! ")
        break
    else:
        print("command not recognizable, pls type 'help' !")
# ------



                           
for eachthing in [1, 3, 2]:               #“Take each thing inside x and do do this with it.”
    print(eachthing)
print("-----")
for x in range(5):
    print(x)
print("-----")
for x in range(1, 7, 2):
    print(x)
print("-----")

price_of_items = [20, 40, 60, 100]
total_price=0
for x in price_of_items:
    total_price=total_price+x
print(total_price)

print("-----")


shape_list=[2, 2, 2, 2, 5]
for number_of_x in shape_list:
    x=""
    for n in range(number_of_x):
        x=x+"x"
    print(x)






