def solution(l):
    divisors = []
    for i in range(len(l)):
        now = l[i]
        divisor = []
        for j in range(i+1,len(l)):
            cur = l[j]
            if cur%now==0:
                divisor.append(j)
        divisors.append(divisor)
    ans = 0
    for i in range(len(l)):
        divisor = divisors[i]
        for x in divisor:
            ans+= len(divisors[x])
    return ans
print(solution([1, 2, 3, 4, 5, 6]))