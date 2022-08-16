import os


print("Instructions:\nRefresh whole program after creating new file\nDelete or rename files manually\nDont rename Note.txt or delete the file\nType:\n\tclose = stop typing\n\tdelete = delete last line\n\tclear = delete all file contents\n\tchange = open another file\n")

f = open("Note.txt")

original = f.read()

print(original)

f.close()

new = input("")

currentfile = "Note.txt"

while new != "close":
    if new == "delete":
        delete = open(currentfile, 'rb')
        pos = next = 0
        for line in delete:
          pos = next
          next += len(line)
        delete.close()
        delete = open(currentfile, 'ab')
        delete.truncate(pos-2)
        delete.close()
        print("")
        print("")
        delete.close()
        delete = open(currentfile)
        print(delete.read())
    elif new == "clear":
        clear = open(currentfile, "r+")
        clear.truncate(0)
        print("")
        print("")
    elif new == "new":
        name = input("Enter name of file: ")
        newfile = open(name + ".txt", "x")
        currentfile = name + ".txt"
        print("")
        print("")
    elif new == "change":
        changeto = input("Change file to: ")
        if changeto[-4:] != ".txt":
            changeto = changeto + ".txt"
        while os.path.exists(changeto) == False:
            changeto = input("File doesn't exist. Change file to: ")
        currentfile = changeto
        print("")
        print("")
        changed = open(currentfile)
        print(changed.read())
    elif new == "instructions" or "instruction":
        print("Instructions:\nRefresh whole program after creating new file\nDelete or rename files manually\nDont rename Note.txt or delete the file\nType:\n\tclose = stop typing\n\tdelete = delete last line\n\tclear = delete all file contents\n\tchange = open another file\n")
    else:
        add = open(currentfile, "a")
        emptyfile = open(currentfile)
        if emptyfile.read() == "":
            add.write(new)
            add.close()
        else:
            add.write("\n" + new)
            add.close()
    new = input("")
