"""[Onsite Day1] เบื่อแล้วขนมตู้ อยากเป็นชู้กับเธอ"""
def main():
    """calculate"""
    money = int(input())
    first = money
    water = int(input())
    money -= water
    left = money%3
    if left == 0:
        sl1 = 10
    elif left == 1:
        sl1 = 15
    elif left == 2:
        sl1 = 20
    wantsl1 = int(input())
    money = money - (wantsl1*sl1)
    left = money%3
    if left == 0:
        sl2 = 12
    elif left == 1:
        sl2 = 15
    elif left == 2:
        sl2 = 18
    wantsl2 = int(input())
    money = money - (wantsl2*sl2)
    left = money%3
    if left == 0:
        sl3 = 5
    elif left == 1:
        sl3 = 7
    elif left == 2:
        sl3 = 9
    wantsl3 = int(input())
    money = money - (wantsl3*sl3)
    if money < 0:
        print("Now you have %d left." %first)
        print("You don't have enough money!")
    else:
        print("Now you have %d left." %money)
        print("Here's your order!")
        print("Water: %d baht" %water)
        print("Snack number 1: %d baht" %(wantsl1*sl1))
        print("Snack number 2: %d baht" %(wantsl2*sl2))
        print("Snack number 3: %d baht" %(wantsl3*sl3))
main()
