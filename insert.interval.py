class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        inserted = []

        insertIndex = 0
        for interval in intervals:
            if interval[0] < newInterval[0]:
                inserted.append(interval)
            elif interval[0] > newInterval[0]:
                if len(inserted) != 0 and newInterval[0] <= inserted[-1][1]:
                    inserted[-1][1] = max(newInterval[1], inserted[-1][1])
                else:
                    inserted.append(newInterval)
                break
            else:
                inserted.append([newInterval[0], max(interval[1], newInterval[1])])

            insertIndex += 1

        if len(inserted) == len(intervals):
            if newInterval[0] == inserted[-1][0]:
                inserted[-1][1] = max(newInterval[1], inserted[-1][1])
            elif newInterval[0] <= inserted[-1][1]:
                inserted[-1][1] = max(newInterval[1], inserted[-1][1])
            else:
                inserted.append(newInterval)

        for i in range(insertIndex, len(intervals)):
            interval = intervals[i]
            if interval[0] <= inserted[-1][1]:
                inserted[-1][1] = max(interval[1], inserted[-1][1])
            else:
                inserted.append(interval)

        return inserted
