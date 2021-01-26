n = []
height = []
f = open('histogram_largest_rectangle.txt', 'r')
for line in f.readlines():
    if line != '0':
        line = line.rstrip().split()
        n.append(line[0])
        height.append(line[1:])
f.close()

answer = 0


# while a != 0:
#     temp = list(map(int, sys.stdin.readline().rstrip().split()))
#     n.append(temp[0])
#     height.append(temp[1:])
