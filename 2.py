def two(lambs):
    payout = 1
    i = 0
    while True:
        i +=1
        if lambs <= 0:
            return i
        payout *= 2
        lambs -= payout


def fib(lambs):
    a, b = 0, 1
    i = 0
    while True:
        i +=1
        if lambs <= 0:
            return i
        a, b = b, a + b
        lambs -= b
def solution(total_lambs):
    a = two(total_lambs)
    b = fib(total_lambs)
    return max(a,b)-min(a,b)

print(solution(143))