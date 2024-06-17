n, m = map(int, input().split())
ls = [0]*n
for i in range(n):
    ls[i] = int(input())

def main():
    ls.sort()
    mn = 22000000001
    en = 0
    for st in range(n):
        while(en < n and ls[en] - ls[st] < m):
            en += 1
        if (en == n):
            break
        mn = min(mn, ls[en] - ls[st])
    return mn

if __name__ == "__main__":
   print(main())