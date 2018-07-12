if __name__ == '__main__':
    for i in range(int(input())):
        ab = input().split()
        la = list(map(int, input().split()))
        lb = list(map(int, input().split()))
        if sum(la) > sum(lb):
            print('C1')
        else:
            print('C2')