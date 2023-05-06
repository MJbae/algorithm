minCostSum = 1000

def DFS(layer, costSum, no, works):
    global minCostSum
    #print(layer, costSum, no, works, minCostSum)
    if layer == no:
        for j in range(len(works)):
            costSum = costSum + works[j]**2
        if minCostSum > costSum:
            minCostSum = costSum
    else:
        for i in range(len(works)):
            works[i] -= 1
            DFS(layer + 1, costSum, no, works)
            works[i] += 1


def solution(no, works):
    layer = 0
    costSum = 0
    
    DFS(0, 0, no, works)
    
    return minCostSum