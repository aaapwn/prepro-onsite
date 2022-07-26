"""[Onsite Day 2] ตัวเลขที่มีอยู่"""
def get(num):
    """geet"""
    word = input()
    if word != "No more!":
        num.append(int(word))
        get(num)
    else:
        return num

def main():
    """main"""
    ans = 0
    num = []
    longg = int(input())
    if longg == 0:
        print("No Tape Measure")
        return
    get(num)
    for i in num:
        if i < longg:
            ans += i
    if ans == 0:
        print("Not Found Number")
        return
    print("Sum of Found Number = %d" %(ans))
main()
