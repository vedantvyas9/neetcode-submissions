class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {}
        for word in words:
            for c in word:
                graph[c] = set()
                indegree[c] = 0
        def compare(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if (word1[i] != word2[i]):
                    if (word2[i] not in graph[word1[i]]):
                        graph[word1[i]].add(word2[i])
                        indegree[word2[i]] += 1
                    return True
            if (len(word1) > len(word2)):
                return False
            return True
        for i in range(len(words) - 1):
            if (not compare(words[i], words[i + 1])):
                return ""
        visited = set()
        stack = set()
        output = []
        def dfs(curr):
            if (curr in stack):
                return False
            if (curr in visited):
                return True
            stack.add(curr)
            for neigh in graph[curr]:
                
                if not dfs(neigh):
                    return False
            visited.add(curr)
            stack.remove(curr)
            output.append(curr)
            return True
        for c in graph:
            if c not in visited:
                if not dfs(c):
                    return ""
        return "".join(output[::-1])

            