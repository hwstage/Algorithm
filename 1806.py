import sys
input = sys.stdin.readline

n, s = map(int, input().split())
ls = list(map(int, input().split()))


def main():
    # 누적합 리스트
    sumls = [0] * (n + 1)
    for i in range(1, n + 1):
        sumls[i] = sumls[i - 1] + ls[i - 1]
    
    mnm = 100000
    en = 1  # 두 번째 포인터 end
    
    # 첫 번째 포인터의 이동
    for st in range(n):
        # 두 번째 포인터를 부분합이 s 이상이 될 때까지 이동
        while en <= n and sumls[en] - sumls[st] < s:
            en += 1
        if en == n + 1:
            break
        mnm = min(mnm, en - st)
    
    # 조건을 만족하는 부분합이 없을 떄
    if mnm == 100000:
        return 0
    return mnm
'''

if __name__ == "__main__":
    print(main())

def main():
    mnm = 100000
    # 두 번째 포인터 end
    en = 0
    # 현재까지의 부분합
    sum = ls[0]
    
    # 첫 번째 포인터의 이동
    for st in range(n):
        # 두 번째 포인터를 부분합이 s 이상이 될 때까지 이동
        while(en < n and sum < s):
            en += 1
            if(en < n):
                sum += ls[en]
        
        # 인덱스 에러
        if en == n:
            break
        
        # 현재 부분합이 s 이상이면 최소 길이 갱신
        mnm = min(mnm, en - st + 1)
        
        # 첫 번째 포인터 이동하며 부분합 갱신
        sum -= ls[st]
    
    # 조건을 만족하는 부분합이 없을 떄
    if mnm == 100000:
        mnm = 0
    
    return mnm
'''
if __name__ == "__main__":
    print(main())