def gcd(a, b):
    while True:
        if a % b == 0 or b % a == 0:
            break
        if a > b:
            a %= b
        else:
            b %= a
    return a if a < b else b

def array_gcd(array):
    gcd_A = 0
    for num in array:
        if gcd_A == 0:
            gcd_A = num
        else:
            gcd_A = gcd(gcd_A, num)
    return gcd_A
def can_divide(array, divisor):
    for num in array:
        if num % divisor == 0:
            return True
    return False

def solution(arrayA, arrayB):
    answer = 0
    gcd_A = array_gcd(arrayA)
    gcd_B = array_gcd(arrayB)
    if not can_divide(arrayA, gcd_B):
        answer = gcd_B
    if not can_divide(arrayB, gcd_A):
        if answer != 0:
            answer = max(answer, gcd_A)
        else:
            answer = gcd_A
    return answer