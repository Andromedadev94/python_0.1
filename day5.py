def emoji_disc(message):
    message=message.split(' ')
    emoji_dictionary={
        ":)":"😊",
        ":(": "😢",
        ":D":"😂",                   #building a function to convert the message into emoji if it has any
        ":))":"🤣"
    }
    converted_emoji=""
    for emoji in message:
        converted_emoji+=emoji_dictionary.get(emoji, emoji) + " "
    return converted_emoji   
n=emoji_disc(input(">: "))
print(n)

#--------
while True:
    try:        #we use try so we can also use exception that crashes our code
        age=int(input("Enter your age pls: "))
        year_of_birth=2025-age
        print(f"You are born in {year_of_birth}!")
        break
    except ZeroDivisionError:
        print("Age can't be zero!")
    except ValueError:
        print("Age can only be numbers!")
