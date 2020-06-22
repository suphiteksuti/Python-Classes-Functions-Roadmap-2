def hotel_cost(days):

    days = float(days*140)
    print("Hotel Cost : ", end = ' ')
    print(days)
    return days



def plane_ride_cost(city):

    if city == "Charlotte" :
        city = 183
        print("Plane Ride Cost : ", end = ' ')
        print(city)
        return city
    elif city == "Tampa" :
        city = 220
        print("Plane Ride Cost : ", end = ' ')
        print(city)
        return city
    elif city == "Pittsburgh" :
        city = 222
        print("Plane Ride Cost : ", end = ' ')
        print(city)
        return city
    elif city == "Los Angeles" :
        city = 475
        print("Plane Ride Cost : ", end = ' ')
        print(city)
        return city



def rental_cost (days):

    if days >= 3 and days < 7 :

        days = float(days*40-20)
        print("Rental Cost :", end = ' ')
        print(days)
        return days

    elif days >=7 :

        days = days*40-50
        print("Rental Cost :", end = ' ')
        print(days)
        return days

    else :

        days = days*40
        print("Rental Cost :", end = ' ')
        print(days)
        return days

def trip_cost(days,city):

    spending_money = hotel_cost(days)+plane_ride_cost(city)+rental_cost(days)
    print("Spendin Money : ", spending_money)

trip_cost(8,"Tampa")