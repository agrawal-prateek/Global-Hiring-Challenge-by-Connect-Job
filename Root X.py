from collections import defaultdict


def preprocessing(gph, nds, dta, ca, cn):
    if not nds[cn]:
        nds[cn] = True
        dta[cn] = ca
        for node in gph[cn]:
            preprocessing(gph=gph, nds=nds, dta=dta, ca=ca + [node], cn=node)
        nds[cn] = False


n, q = [int(x) for x in input().rstrip().split()]
values_of_node = [0] + [int(x) for x in input().rstrip().split()]
u, v, x = None, None, None

graph = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
nodes = [False for _ in range(n + 1)]
preprocessed_data = {}

preprocessing(gph=graph, nds=nodes, dta=preprocessed_data, ca=[1], cn=1)

for _ in range(q):
    v, x = map(int, input().rstrip().split())
    answer = 0
    for node_value in preprocessed_data[v]:
        if values_of_node[node_value] <= x:
            answer += 1
    print(answer)
