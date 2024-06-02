N, K, P, X = map(int, input().split())

''' 
  --A--
 |     |
 F     B
 |     |
  --G--
 |     |
 E     C
 |     |
  --D--  '''
num = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1]   # 9
]

def main():
    result = 0
    # 1부터 N층 까지 조사한다.
    for i in range(1, N+1):
        # 현재 층은 생략한다.
        if i == X:
            continue
        # 디스플레이를 반전시킨 횟수
        cnt = 0
        # 변수 복사
        cur = X
        dest = i
        # k자리수니 k번 조사
        for j in range(K):
            for k in range(7):
                if num[cur%10][k] != num[dest%10][k]:
                    cnt += 1
            cur //= 10
            dest //= 10
        if cnt <= P:
            result += 1
    print(result)
    return
            

if __name__ == "__main__":
    main()
