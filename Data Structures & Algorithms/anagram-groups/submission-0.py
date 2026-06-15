class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_result = []
        visited = [False] * len(strs)

        for i in range(len(strs)):

            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, len(strs)):

                if len(strs[i]) != len(strs[j]):
                    continue

                if sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    visited[j] = True

            main_result.append(group)

        return main_result