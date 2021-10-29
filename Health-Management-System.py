import datetime
def getTime():
    return datetime.datetime.now()

def put(k):
    if k==1:
        c = int(input("Enter 1 for Excercise and 2 for Diet : "))
        if c == 1:
            value = input("Type here .....")
            with open("sanket-ex.txt","a") as op:
                op.write(str([str(getTime())])+" : "+value+"\n")
            print("Successfully Written ........")
        elif c == 2:
            value = input("Type here .....")
            with open("sanket-diet.txt","a") as op:
                op.write(str([str(getTime())])+" : "+value+"\n")
            print("Successfully Written ........")
    elif k==2:
        c = int(input("Enter 1 for Excercise and 2 for Diet : "))
        if c == 1:
            value = input("Type here .....")
            with open("yash-ex.txt","a") as op:
                op.write(str([str(getTime())])+" : "+value+"\n")
            print("Successfully Written ........")
        elif c == 2:
            value = input("Type here .....")
            with open("yash-diet.txt","a") as op:
                op.write(str([str(getTime())])+" : "+value+"\n")
            print("Successfully Written ........")
    elif k==3:
        c = int(input("Enter 1 for Excercise and 2 for Diet : "))
        if c == 1:
            value = input("Type here .....")
            with open("mayur-ex.txt","a") as op:
                op.write(str([str(getTime())])+" : "+value+"\n")
            print("Successfully Written ........")
        elif c == 2:
            value = input("Type here .....")
            with open("mayur-diet.txt","a") as op:
                op.write(str([str(getTime())])+" : "+value+"\n")
            print("Successfully Written ........")
    else:
        print("Please Enter Valid value .......")

def retrieve(k):
    if k==1:
        c = int(input("Enter 1 for Excercise and 2 for Diet : "))
        if c == 1:
            with open("sanket-ex.txt") as op:
                for i in op:
                    print(i,end="\n")
        elif c == 2:
            with open("sanket-diet.txt") as op:
                for i in op:
                    print(i,end="\n")
    elif k==2:
        c = int(input("Enter 1 for Excercise and 2 for Diet : "))
        if c == 1:
            with open("yash-ex.txt") as op:
                for i in op:
                    print(i,end="\n")
        elif c == 2:
            with open("yash-diet.txt") as op:
                for i in op:
                    print(i,end="\n")
    elif k==3:
        c = int(input("Enter 1 for Excercise and 2 for Diet : "))
        if c == 1:
            with open("mayur-ex.txt") as op:
                for i in op:
                    print(i,end="\n")
        elif c == 2:
            with open("mayur-diet.txt") as op:
                for i in op:
                    print(i,end="\n")
    else:
        print("Please Enter Valid value .......")


if __name__ == "__main__":
    print("Health Management System .....")
    a = int(input("Press 1 to log the value and 2 for retrieve the value : "))
    if a==1:
        b = int(input("Press 1 for Sanket, 2 for Yash, 3 for Mayur : "))
        put(b)
    elif a==2:
        b = int(input("Press 1 for Sanket, 2 for Yash, 3 for Mayur : "))
        retrieve(b)
    else:
        print("Please enter valid value ..........")