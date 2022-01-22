

def pattern(r, c):
    if r == 0:
        return

    if c < r:
        print("* ", end="")
        pattern(r, c+1)
    else:
        print()
        pattern(r-1, 0)


pattern(r=4, c=0)


'''
* * * * 
* * * 
* *
*
'''
