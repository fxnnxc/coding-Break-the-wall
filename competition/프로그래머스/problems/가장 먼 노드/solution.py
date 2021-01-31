def bfs(start, graph, lengths):
    queue = [1]
    lengths[start] = 1
    while queue:
        v = queue.pop(0)
        for nei in graph[v]:
            if lengths[nei]==0:
                lengths[nei] = lengths[v]+1
                graph[nei].remove(v)
                queue.append(nei)


def solution(n, edge):
    graph = {i:[] for i in range(1, n+1)}
    for s,e in edge:
        graph[s].append(e)
        graph[e].append(s)
    lengths = [0 for i in range(n+1)] 
    bfs(1, graph, lengths)
    answer = lengths.count(max(lengths))
    return answer