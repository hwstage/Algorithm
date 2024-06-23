import heapq
import sys
input = sys.stdin.readline
INF = 1e10

N, M, X = map(int, input().split())
graph = [[]for i in range(N+1)] # 방향 그래프
reversed_graph = [[]for i in range(N+1)] # 역방향 그래프
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append([b, t]) # [[], [[2, 4], [3, 2], [4, 7]], [[1, 1], [3, 5]], [[1, 2], [4, 4]], [[2, 3]]]
    reversed_graph[b].append([a, t])



def dijkstra(s, g): # 출발 노드, 그래프
    dist = [INF]*(N+1)
    dist[s] = 0 # 출발 노드와의 거리는 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d: # 이미 구한 최단거리보다 더 크면 continue
            continue
        for i in g[now]: 
            cost = d + i[1]
            if cost < dist[i[0]]: # 최단거리라면 값을 갱신하고, Heapq에 push
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dist


def main():
    toX = dijkstra(X, graph)
    fromX = dijkstra(X, reversed_graph)
    print(max([toX[i] + fromX[i] for i in range(1, N+1) if i != X]))
    

if __name__ == "__main__":
    main()