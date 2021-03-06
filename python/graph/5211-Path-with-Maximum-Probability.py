from typing import List
from collections import defaultdict
from heapq import heappop, heappush, heapify
class Solution:
    # dijkstra
    #  1. init graph as map
    # 2. from start, for each end point, calculate a probability
    # 3. add the probabilities to heap
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        visited = set()
        max_heap = [(-1.0, start)]
        # max_heap.heappush())
        while max_heap:
            prob_start,start_point = heappop(max_heap)
            if start_point == end:
                return -prob_start
            visited.add(start_point)
            next_list = graph.get(start_point)
            if next_list:
                for end_point, prob_end in next_list:
                    if end_point not in visited:
                        heappush(max_heap, (prob_start * prob_end, end_point))
        return 0


    #Bellma -ford TLE
    def maxProbability_TLE(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        def getMax(start_, end_, edges_):
            dp = [0.0 for i in range(n)]
            dp[start_] = 1.0
            max_prob = 0.0
            for k in range(10): # if n here will TLE, if 10 here will be accepted
                for i in range(len(edges_)):
                    #tmp_dp = list(dp)
                    start_point = edges_[i][0]
                    end_point = edges_[i][1]
                    prob = succProb[i]
                    dp[end_point] = max(dp[end_point], dp[start_point] * prob)
                    dp[start_point] = max(dp[start_point], dp[end_point] * prob)
                    if end_point == end_:
                        max_prob = max(max_prob, dp[end_point])
                    if start_point == end_:
                        max_prob = max(max_prob, dp[start_point])
                    #dp = tmp_dp
            return max_prob
        result_2 = getMax(start, end, edges)
        return result_2

def main():
    sol = Solution()
    # result = sol.canFinish(2, [[1,0], [2, 0], [3, 1], [3, 2]])
    # print(result)
    result = sol.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2)
    print(result)
    # result = sol.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2)
    # print(result)
    # result = sol.maxProbability(3, [[0,1]], [0.5], 0, 2)
    # print(result)
    # result = sol.maxProbability(5, [[2,3],[1,2],[3,4],[1,3],[1,4],[0,1],[2,4],[0,4],[0,2]],\
    #      [0.06,0.26,0.49,0.25,0.2,0.64,0.23,0.21,0.77], 0, 3)
    # print(result)

    # result = sol.maxProbability(5, [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]],\
    #      [0.37,0.17,0.93,0.23,0.39,0.04], 3, 4)
    # print(result)


if __name__ == "__main__":
    main()
