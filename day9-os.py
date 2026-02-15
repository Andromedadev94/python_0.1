if False:
    file2 = open("../python-0.2test/test4.py", "w")  #"w" to write, it deletes everything that was on the file before
                                                    "r" to read, #"a" to append extra note at the end of our file #"b" to open in binary
    file3 = open("../python-0.2test/test4.py", "r+")  #"adding + after mode means doing read and write"
    file3.write("\nHello")
    file3.write("\nHow you doing?\n")
    file3.close()

    file1 = open("../python-0.2test/test4.csv", "a")
    file1.write("Username, Age, Gender\n")
    file1.write("Andro, 29, Male\n")
    file1.write("Akiara, 22, Male\n")
    file1.write("Sara, 17, Female\n")
    file1.close()
    #best is to use with x as variablename: to open file or open connection, so it closes them auto

    with open("../python-0.2test/test4.csv", "a+") as file1:
        file1.write("yotoro, 29, Male\n")      

    with open("../python-0.2test/x.jpg", "rb") as source:                # used for opening the binary data like in a picture
        with open("../python-0.2test/1.jpg", "wb") as destination:
            destination.write(source.read())
    with open("../python-0.2test/test4.csv", "r") as file1:
        list_of_5byetes = file1.readline()       #can use readline to read line
        print(list_of_5byetes)                    #can use readlines to turn the whole text into a list
    import os
    current_dr = os.getcwd()
    os.chdir('python-0.1') 
    os.mkdir("lets-see")
    os.rmdir("lets-see")               
    changed_dr = os.getcwd()
    os.rename("my", "mymoduls")
    list_of_dir = os.listdir()
    os.remove("day1.py")
    print(current_dr, changed_dr, "\n", list_of_dir)

    import shutil
    shutil.copy("day8.py", "day12.py")



