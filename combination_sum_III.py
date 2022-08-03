class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def dfs(current, i, total):
            if len(current) == k:
                if total == n:
                    result.append(current)
                return
        
            for x in range(i, 9+1):
                if total+x > n:
                    break
                dfs(current+[x], x+1, total+x)
                
        dfs([], 1, 0)
        
        return result


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 9+1)]
        
        combi = itertools.combinations(nums, k)
        
        return [c for c in combi if sum(c)==n]