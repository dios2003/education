from fake_math import divide as _f_div
from true_math import divide as _t_div


result1 = _f_div(69, 3)
result2 = _f_div(3, 0)
result3 = _t_div(49, 7)
result4 = _t_div(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
