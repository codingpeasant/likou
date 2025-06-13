from collections import defaultdict


input = [
    ['prodId', 'sales', 'cost', 'state', 'timestamp'],
    [1, 914, 414, 'OH', '1605433721'],
    [2, 315, 281, 'PA', '1654349339'],
    [3, 990, 822, 'WA', '1663967760'],
    [4, 416, 318, 'FL', '1667737923'],
    [5, 192, 92,  'TX', '1612727969'],
    [6, 683, 276, 'MI', '1694646617'],
    [7, 879, 636, 'TX', '1641627302'],
    [8, 151, 38,  'IL', '1663369922'],
    [9, 623, 123, 'IL', '1658273557'],
    [10,373, 332, 'FL', '1674158472']
]

columnToIndex = {
  "state": 3,
  "timestamp": 4
}

def getProfitPivotTable(column):
  resProfitBy = defaultdict(int)
  for rowId in range(1, len(input)):
    resProfitBy[input[rowId][columnToIndex[column]]] += input[rowId][1]-input[rowId][2]

  res = [[column, "profit"]]
  for state, profit in resProfitBy.items():
    res.append([state, profit])
  return res

def getProfitPivotTableWithTimeRange(bucketSize: int):
  timestamps = [int(input[rowId][columnToIndex['timestamp']]) for rowId in range(1, len(input))]
  minTimestamp, maxTimestamp = min(timestamps), max(timestamps)
  print(minTimestamp, maxTimestamp)
  buckets = [minTimestamp] + [int(minTimestamp + (maxTimestamp-minTimestamp)/bucketSize * (i+1)) for i in range(bucketSize)]
  sortedByTimestamp = sorted(input[1:], key=lambda x: x[4])
  print(buckets)

  rowId = 0
  bucketWithSalesSum = defaultdict(int)
  for i in range(1, len(buckets)):
    curBucket = (buckets[i-1], buckets[i])
    while rowId < len(sortedByTimestamp) and curBucket[0] <= int(sortedByTimestamp[rowId][columnToIndex['timestamp']]) <= curBucket[1]:
      bucketWithSalesSum[curBucket]+=sortedByTimestamp[rowId][1]
      rowId+=1
    if not bucketWithSalesSum[curBucket]:
      bucketWithSalesSum[curBucket] = 0
    
  print(bucketWithSalesSum)
  

print(getProfitPivotTable("state"))
print(getProfitPivotTable("timestamp"))
print(getProfitPivotTableWithTimeRange(5))