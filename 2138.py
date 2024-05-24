import copy
n = int(input())
cur = list(map(int, input()))
dest = list(map(int, input()))

def switch(self, idx):
    self[idx-1] = 1 - self[idx-1]
    self[idx] = 1 - self[idx]
    self[idx+1] = 1 - self[idx+1]

def solution(s, flg):
    cnt = flg
    if flg == 1:
        s[0] = 1 - s[0]
        s[1] = 1 - s[1]
        if s == dest:
            return cnt
        
    for i in range(1, n-1):
        if s[i-1] != dest[i-1]:
            switch(s, i)
            cnt += 1
    if s[n-2] != dest[n-2]:
        s[n-2] = 1 - s[n-2]
        s[n-1] = 1 - s[n-1]
        cnt +=1
    if s == dest:
        return cnt
    return 0

'''
def solution(s, flg):
    cnt = flg
    if flg == 1:
        s[0] = 1 - s[0]
        s[1] = 1 - s[1]
        if s == dest:
            return cnt
        
    for i in range(1, n-1):
        if s[i-1] != dest[i-1]:
            switch(s, i)
            cnt += 1
        if s == dest:
            return cnt
        
    s[n-2] = 1 - s[n-2]
    s[n-1] = 1 - s[n-1]
    cnt +=1
    if s == dest:
        return cnt
    return 0
'''

def main():
    if cur == dest:
        print(0)
        return
    cur2 = copy.deepcopy(cur)
    # 1번 스위치를 안 눌렀을 때
    r1 = solution(cur2, 0)
    # 1번 스위치를 눌렀을 때
    r2 = solution(cur, 1)
    if r1 != 0 or r2 != 0:
        print(r1 if r1 != 0 else r2)
        return
    print(-1)

if __name__ == "__main__":
    main()