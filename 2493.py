from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    ls = list(map(int, input().split()))
    # Stack 을 Dequeue로 구현, Tuple을 통해 탑의 번호, 높이를 저장
    stk = deque()
    # 0번째 위치에 최대 높이의 탑이 있다고 가정
    stk.append((0, 100000001))
    for i in range(1, n+1):
        # 스택 내에서 현재 확인하는 탑보다 작은 탑을 모두 제거
        while(stk[-1][1] < ls[i-1]):
            stk.pop()
        print(stk[-1][0], end=' ')
        stk.append((i, ls[i-1]))
    return

if __name__ == "__main__":
    main()