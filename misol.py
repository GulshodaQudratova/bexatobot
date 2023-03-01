a = [[19,-2,29], [-10,-4,-6]]
# f = []
# for k in a:
#   for i in  k:
#       f.append(i)
# print(max(f))
import sys
maxElement = 0
for i in range(3):
        for j in range(2):
            if a[i][j] > maxElement:
                maxElement = a[i][j]
print(maxElement)