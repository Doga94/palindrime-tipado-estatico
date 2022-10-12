def primos(number: int) -> bool:
    newlist = [x for x in range(2, number+1) if (number % x) ==0]
    newlist_end = len(newlist) == 1
    if newlist_end == True:
        print(number, "Is prime")
    else:
        print(number, "Not is prime, divisor are: ", newlist)
    # for i in range(2, number):
    #     if (number % i) == 0:
    #         return False
    #     return True


def run():
    number_user = int(input("Type number"))
    number : int = int(number_user)
    if number >= 1:
        primos(number)


if __name__ == '__main__':
    run()