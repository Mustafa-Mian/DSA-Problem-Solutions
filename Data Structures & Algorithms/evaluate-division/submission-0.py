class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        weights = {}
        for i in range(len(equations)):
            var1, var2 = equations[i]
            ans = values[i]
            graph[var1].append(var2)
            weights[(var1, var2)] = ans
            graph[var2].append(var1)
            weights[(var2, var1)] = (1 / ans)

        def dfs(src, dst, visited):
            if src == dst:
                return 1.0
            visited.add(src)
            neighbours = graph[src]
            for neig in neighbours:
                if neig in visited:
                    continue
                factor = dfs(neig, dst, visited)
                if factor != -1:
                    return weights[(src, neig)] * factor
            return -1

        result = []
        for query in queries:
            var1, var2 = query
            if (var1 not in graph) or (var2 not in graph):
                result.append(-1.0)
            else:
                result.append(dfs(var1, var2, set()))
        return result