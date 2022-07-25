"""[Onsite Day1] Suvarnabhumi Airport"""
def cal(rr0, rr1):
    """cal"""
    if rr1 >= 60:
        rr1 = rr1 - 60
        rr0 += 1
    if rr0 >= 24:
        rr0 -= 24
    return rr0, rr1

def main():
    """flight"""
    input()
    finshh = input().upper()
    timee = input().split(" ")
    realtime = timee[0]
    realtime = str(realtime).split(":")
    if timee[1].upper() == "PM":
        realtime[0] = int(realtime[0]) + 12
    realtime[0] = int(realtime[0]) - 7
    realtime[1] = int(realtime[1])
    if "SYD" in finshh:
        realtime[0] = int(realtime[0]) + 9 + 10
        realtime[0], realtime[1] = cal(realtime[0], realtime[1])
        too = "SYD"
    elif "SGN" in finshh:
        realtime[0] = int(realtime[0]) + 1 + 7
        realtime[1] = realtime[1] + 50
        realtime[0], realtime[1] = cal(realtime[0], realtime[1])
        too = "SGN"
    elif "ATL" in finshh:
        realtime[0] = int(realtime[0]) + 20 - 4
        realtime[1] = realtime[1] + 55
        realtime[0], realtime[1] = cal(realtime[0], realtime[1])
        too = "ATL"
    elif "YVR" in finshh:
        realtime[0] = int(realtime[0]) + 16 - 7
        realtime[1] = realtime[1] + 20
        realtime[0], realtime[1] = cal(realtime[0], realtime[1])
        too = "YVR"
    elif "KTM" in finshh:
        realtime[0] = int(realtime[0]) + 13 + 5
        realtime[1] = realtime[1] + 45
        realtime[0], realtime[1] = cal(realtime[0], realtime[1])
        too = "KTM"
    if realtime[0] == 0:
        realtime[0] = 12
        ttt = "AM"
        print("BKK - %s" %too)
        print("%02d:%02d %s" %(realtime[0], realtime[1], ttt))
        return
    if realtime[0] == 12:
        ttt = "PM"
        print("BKK - %s" %too)
        print("%02d:%02d %s" %(realtime[0], realtime[1], ttt))
        return
    if realtime[0] > 12:
        realtime[0] -= 12
        ttt = "PM"
    else:
        ttt = "AM"
    print("BKK - %s" %too)
    print("%02d:%02d %s" %(realtime[0], realtime[1], ttt))
main()
