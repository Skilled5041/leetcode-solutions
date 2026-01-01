class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def combSum(candidates, target):
            if len(candidates) == 0 or target - candidates[0] < 0:
                return []

            combinations = []
            for i in range(len(candidates)):
                if target == candidates[i]:
                    combinations += [[candidates[i]]]
                    break
                combinations += combSum(candidates[i:], target - candidates[i])

            return list(map(lambda x: [candidates[0]] + x, combinations))

        if len(candidates) == 0 or target - candidates[0] < 0:
                return []

        combinations = []
        for i in range(len(candidates)):
                if target == candidates[i]:
                    combinations += [[candidates[i]]]
                    break
                combinations += combSum(candidates[i:], target - candidates[i])
        
        return combinations
