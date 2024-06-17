import sys
input = sys.stdin.readline

city = []

n = int(input())
m = int(input())
for i in range(n):
    city.append(list(map(int, input().split())))

plan = list(map(int, input().split()))
visited = [0]*(n+1)
def dfs(a):
    if visited[a] == 1:
        return
    visited[a] = 1
    for i in range(1, n+1):
        if city[a-1][i-1] == 1:
            dfs(i)

def main():
    dfs(plan[0])
    for i in plan:
        if visited[i] == 0:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    main()