n = int(input())
points = list(map(int, input().split()))
count = 0

for i in range(0, len(points)): 
    if i == 0: 
        continue
    sub_points = [points[i] for i in range(0, i)] 
    min_point = min(sub_points)
    max_point = max(sub_points)
    if points[i] > max_point:
        count += 1 
    if points[i] < min_point:
        count += 1

print(count)

