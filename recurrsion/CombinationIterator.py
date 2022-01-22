

# https://leetcode.com/problems/iterator-for-combination/

s = "abc"
os = 2
o = ['ab', 'bc', 'ac']


def CombinationIterator(p, up, lp):

    if len(up) == 0:
        if len(p) == lp:
            print(p)
        return

    ch = up[0]

    CombinationIterator(ch+p, up[1:], lp)
    CombinationIterator(p, up[1:], lp)

print(CombinationIterator("", "abc", 2))
