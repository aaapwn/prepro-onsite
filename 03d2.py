"""[Onsite Day 2] Math Symbol"""
def get(num, ans):
    """geet"""
    word = input()
    if word.isnumeric():
        num.append(int(word))
        get(num, ans)
    else:
        ans = num[0]
        if word == "+":
            for i in num[1:]:
                ans += i
        elif word == "-":
            for i in num[1:]:
                ans -= i
        elif word == "*":
            for i in num[1:]:
                ans *= i
        elif word == "/":
            for i in num[1:]:
                ans /= i
        print("%.2f" %ans)

def main():
    """main"""
    num = []
    ans = 0
    get(num, ans)
main()
