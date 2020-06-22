def distance_from_zero():

    argument = eval(input())

    if type(argument)==int:

        print(abs(argument))

    if type(argument)==float:
        print(abs(argument))

    else:
        return "nope"

distance_from_zero()