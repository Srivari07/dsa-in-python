# s = "abc"
# ans = ["abc", "acb", "bac", "bca", "cab", "cba"]

def fun(p, up):
    if len(up) == 0:
        print(p, end=" ")
        return
    ch = up[0]
    for i in range(0, len(p)):
        firstStr = p[0:i]
        secondStr = p[i:len(p)]
        fun(firstStr+ch+secondStr, up[1:])


# print(fun(p="", up="abc"))


def get_permutation(string, i=0):

    if i == len(string):
        print("".join(string), end=" ")

    for j in range(i, len(string)):
        words = [c for c in string]
        words[i], words[j] = words[j], words[i]
        get_permutation(words, i + 1)


print(get_permutation(string='abc'))
