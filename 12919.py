import sys
input = sys.stdin.readline

# T를 S로 바꾸는 재귀함수
def recursive(s, t):
    if t == s:
        print(1)
        sys.exit()
    if len(t) == 0 :
        return
    if t[-1] == 'A':
        recursive(s, t[:-1]) # 맨 뒤가 A라면 A를 제거하고 재귀
    # BABA 가 ABA 에서 B를 추가한 건지, BAB에서 A를 추가한 건지 알 수 없으므로 elif로 묶을 수 없음
    if t[0] == 'B':
        recursive(s, t[1:][::-1]) # 맨 앞이 B라면 B를 제거하고 문자열을 뒤집어 재귀


def main():
    S = input().strip()
    T = input().strip()
    recursive(S, T)
    return

if __name__ == "__main__":
    main()
    print(0)