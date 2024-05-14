import sys
input = sys.stdin.readline

def main():
    n, x = map(int, input().split())
    ls = list(map(int, input().split()))
    # 누적합 리스트
    sumLs = [0] * n
    sumLs[0] = ls[0]
    for i in range(1, n):
        sumLs[i] = sumLs[i-1] + ls[i]
    
    # 최대 방문자 수가 0일 경우
    if sumLs[-1] == 0:
        print("SAD")
        return
    
    max = sumLs[x-1]
    cnt = 1

    for i in range(x, n):
        if max < sumLs[i] - sumLs[i-x]:
            max = sumLs[i] - sumLs[i-x]
            cnt = 1
        elif max == sumLs[i] - sumLs[i-x]:
            cnt += 1
    print(max)
    print(cnt)



if __name__ == "__main__":
    main()