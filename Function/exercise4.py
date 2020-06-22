def computepay() :
    hours = float(input("enter your hours: "))
    rate = float(input("enter your rate: "))
    pay = float((hours-40)*(1.5*rate)+40*rate)
    print("Your pay : {}".format(pay))

computepay()