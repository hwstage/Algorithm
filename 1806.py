import sys
# 10 15
# 5 1 3 5 10 7 4 9 2 8   
input = sys.stdin.readline
n, s = map(int, input().split())
ls = list(map(int, input().split()))

# # 누적합 리스트
# sumls = [0]*(n+1)
# sumls[1] = ls[0]
# for i in range(1, n):
#     sumls[i] = ls[i] + sumls[i-1]

def main():
    mnm = 100000
    en = 0
    sum = ls[0]
    for st in range(n):
        while(en < n and sum < s):
            en += 1
            if(en < n):
                sum += ls[en]
        if en == n:
            break
        mnm = min(mnm, en - st + 1)
        sum -= ls[st]
    if mnm == 100000:
        mnm = 0
    return mnm

if __name__ == "__main__":
    print(main())