
import math
n1, n2 = map(int, input().split())

gcd_result = math.gcd(n1, n2)
lcm_result = (n1 * n2) // gcd_result

print(gcd_result)
print(lcm_result)



