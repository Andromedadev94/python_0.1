from pathlib import Path
import os
import shutil
if False:
    pass
    cd = Path.cwd()    #current working dir
    print(cd)
    d1 = cd / "python-0.1"     #path of a file
    print(d1)
    d2 = d1 / "day13.py"        #creating a path object
    print(d2)
    does_exist = d2.exists()    #to check if sth exist
    print(does_exist)

    my_folder = Path.cwd() / "python-0.1"
    for files in Path().iterdir():
        if files.is_file():
            print(files.name)
        elif files.is_dir():
            print(f"folder: {files.name}")
    day13_path = my_folder / "day13.py"

    day13_path.touch(exist_ok=True)
    #day13_path.rename(my_folder / "day13.py")
    with open(day13_path, "w") as day13: #or with day13_pat.open("w") as day13:
        day13.write("Fuck")


    x = Path.home()
    print(x)  # to see the path
    print(x.name)  # to see the name of the file or folder
    print(x.stem)  #to see the name w/o the type
    print(x.parent) #shows the parent of the path(technicly it is like "..")
    y = Path()
    print(y)
    print(y.absolute()) #since y is a relative path, we can use absolute to see the full path
    n = Path("..")   #here we want to go back to parent dic from current dir, and then ask for absolute path
    print(n)
    print(n.absolute())   #but absolute is not working
    print(n.resolve())     #that's why it is better to use resolve for full path
    search = Path(__file__).resolve() #shows the resolve path of current working file
    for files in search.parent.glob("*.py"): #glov is like iterdir but we can search with wild cards 
        print(files.name)                   # * to show all
                                            # *n to show whatever ends in n                       
                                            # *n* to show whatever han n somewhere in the middle
    search = Path(__file__).resolve() 
    for files in search.parent.rglob("*day*", case_sensitive=False): # we use rglob to search in subdirrectories too
        print(files.name)                                              # case_sensitive can be used to upperlower doesnt matter

    creating = Path(__file__).resolve().parent / "testing/test/test1"
    creating.mkdir(parents=True, exist_ok=True) #to creat a dir even if it's parent doesnt exist, so it creats parrent too
    shutil.rmtree(creating)

    replacing = Path(__file__).resolve().parent / "day13.py"
    replacing.replace(Path(__file__).resolve().parent / "day11.py") #can use replace instead of rename

    deleting = Path(__file__).resolve().parent / "day12.py"
    deleting.unlink()  #to delete a file