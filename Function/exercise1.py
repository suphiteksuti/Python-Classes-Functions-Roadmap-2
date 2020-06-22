def shut_down():
    argument = input("please input your value : ")
    if argument == "yes" :
        print("Shutting Down")
    elif argument == "no":
        print("Shutdown aborted")
    else:
        print("sorry")

shut_down()