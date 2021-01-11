def solution(triangle):
    answer = 0
    return max(tri(triangle))

def tri(triangle):
    if len(triangle) < 3:
        return [triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]]
    else:
        temp = tri(triangle[:-1])
        result = []
        for i in range(len(triangle[-1])):
            if i == 0:
                result.append(temp[0] + triangle[-1][0])
            elif i == len(triangle[-1]) - 1:
                result.append(temp[-1] + triangle[-1][-1])
            else:
                result.append(temp[i - 1] + triangle[-1][i]
                              if temp[i - 1] > temp[i]
                             else temp[i] + triangle[-1][i])
        return result