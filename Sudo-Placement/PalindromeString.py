# code


def checkpalindrome(len, strc):
    for k in range(len):
        if strc[k] != strc[len - 1 - k]:
            return False
    return True


if __name__ == '__main__':
    for i in range(int(input())):
        if checkpalindrome(int(input()), input()):
            print('Yes')
        else:
            print('No')
