def has_cycle(graph, start, target):

    visited = set()

    def dfs(node):

        if node == target:
            return True

        visited.add(node)

        for neighbor in graph.get(node, []):

            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        return False

    return dfs(start)