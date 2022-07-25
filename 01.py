"""[Onsite Day1] Drop Drop"""
def main():
    """grade"""
    grade = float(input())
    if grade >= 2.00:
        print("I'm so happy.")
    elif grade < 1.00:
        print("I'm so sad.")
    else:
        passs = 4.00 - grade
        print("%.2f" %passs)
main()
