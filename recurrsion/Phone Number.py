

def pad(p, up):
    if len(up) == 0:
        print(p)
        return

    digit = up[0]
    for i in range((ord(digit)-1)*3, ord(digit)*3):
        ch = ('a' + chr(i))
        pad(p+ch, up[1:])


pad("", "12")
