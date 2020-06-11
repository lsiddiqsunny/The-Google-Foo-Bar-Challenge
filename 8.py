from fractions import gcd

def checkList(array, u):
    count = 0
    for p in range(3):
        for i in range(len(array)/2):
            for j in list(reversed(range(i,len(array)))):
                if j <= len(array)-1 and j > i and j != i:
                    if is_forever(array[i],array[j]):
                        if(0 <= i <= len(array) and len(array) > 0):
                            u.append(array.pop(i))
                            count += 1
                        if(0 <= j <= len(array) and len(array) > 0):
                            u.append(array.pop(j-1))
                            count += 1
    return count
    
def is_forever(x, y):
    z = (x + y) / gcd(x, y)
    return bool((z - 1) & z)
    
def solution(banana_list):
    banana_list = list(banana_list)
    banana_list.sort()
    rem = len(banana_list)
    u = []
    count1 = checkList(banana_list, u)
    return rem - count1


print(solution([1,1]))