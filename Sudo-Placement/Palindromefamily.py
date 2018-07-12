def checkpalindrome(strc):
    lent = len(strc)
    for k in range(lent):
        if strc[k] != strc[lent - 1 - k]:
            return False
    return True


def pfamily(string):
    if checkpalindrome(string):
        return 'PARENT'
    else:
        if checkpalindrome(string[::2]):
            if checkpalindrome(string[1::2]):
                return 'TWIN'
            return 'ODD'
        elif checkpalindrome(string[1::2]):
            return 'EVEN'
    return 'ALIEN'


if __name__ == '__main__':
    for i in range(int(input())):
        print(pfamily(input()))
