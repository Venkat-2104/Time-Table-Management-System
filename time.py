import re

def add_event():
    d = {}
    print("Enter the time in 24-hour format only.")
    a = input("Enter the start time of work: ")
    b = input("Enter the end time of work: ")
    w = input("Enter the work: ")
    s = a + "-" + b
    d[s] = w
    print("Work was updated successfully.")
    try:
        with open("file.txt", "a") as f:
            f.write(str(d))
            f.write("\n")
    except:
        print("Error occurred while writing to file.")

def ud_event():
    d = {}
    print("Enter the time in 24-hour format only.")
    a = input("Enter the start time of work: ")
    b = input("Enter the end time of work: ")
    w = input("Enter the work: ")
    s = a + "-" + b
    d[s] = w
    print("Work was updated successfully.")
    try:
        with open("file.txt", "a") as f:
            f.write("\n")
            f.write(str(d))
    except:
        print("Error occurred while updating the file.")

    t = "{\"" + s + "\":\""
    try:
        with open("file.txt", "r") as f:
            with open("file2.txt", "w") as f2:
                for line in f.readlines():
                    if not (line.startswith(t)):
                        f2.write(line)
                    elif line.startswith(t + w):
                        f2.write(line)
                for line in f.readlines():
                    f2.write(line)
    except:
        print("Error occurred while reading or writing to the file.")

    try:
        with open("file.txt", "w") as f:
            try:
                with open("file2.txt", "r") as f2:
                    f.write(f2.read())
            except:
                print("Error occurred while reading from file2.txt.")
    except:
        print("Error occurred while writing to file.txt.")

def del_event():
    try:
        with open("file.txt", "r") as f:
            t = input("Enter the time interval: ")
            s = "{\"" + t
            try:
                with open("file2.txt", "w") as f2:
                    for line in f.readlines():
                        if not (line.startswith(s)):
                            f2.write(line)
            except:
                print("Error occurred while writing to file2.txt.")
    except:
        print("Error occurred while reading from file.txt.")
    
    try:
        with open("file.txt", "w") as f:
            try:
                with open("file2.txt", "r") as f2:
                    f.write(f2.read())
            except:
                print("Error occurred while reading from file2.txt.")
    except:
        print("Error occurred while writing to file.txt.")

def display():
    try:
        with open("file.txt", "r") as f:
            while True:
                print("Enter 1 to display work for a specific time\nEnter 2 to display the whole timetable")
                k = int(input())
                if k == 1:
                    t = input("Enter the time interval: ")
                    match = re.search(t, f.read())
                    if match:
                        a = match.start()
                        f.seek(a)
                        for i in f.read():
                            if i == "}":
                                break
                            else:
                                print(i, end="")
                        print()  # To end the line after displaying the specific work
                    else:
                        print("No work found for the given time interval.")
                elif k == 2:
                    f.seek(0)  # Reset the file pointer to the beginning
                    for i in sorted(f.readlines()):
                        print(i, end="")
                    print()  # To end the line after displaying the whole timetable
                else:
                    print("Invalid input. Please enter 1 or 2.")
    except:
        print("Error occurred while reading from the file.")

while True:
    print("\nTIME TABLE MANAGEMENT")
    print("=====================")
    print("1. Add event\n2. Update event\n3. Delete an event\n4. Display\n5. Exit")
    print("=====================")
    n = int(input("Choose your option: "))
    if n == 1:
        add_event()
    elif n == 2:
        ud_event()
    elif n == 3:
        del_event()
    elif n == 4:
        display()
    elif n == 5:
        break
    else:
        print("Invalid input.")
