from fake_math import divide as fake
from true_math import divide as true

result1 = fake(30, 8)
result2 = fake(10, 0)
result3 = true(55, 5)
result4 = true(20, 0)
print(result1)
print(result2)
print(result3)
print(result4)