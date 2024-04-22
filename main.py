from typing import *
from methods import *
from functions import *

func_map = [
  (function1, '(x^2 + 2x - 3) / x'),
  (function2, 'sin(x-2x)'),
  (function3, '3x^3 + 2x^2 - 1'),
  (function4, 'x^2'),
  (function5, '3x^3 - 2x^2 - 7x - 8')
]

# Runge coeffs map
# 0 - left rect
# 1 - mid rect
# 2 - right rect
# 3 - trapez.
# 4 - simps.
runge_coeffs = [1, 3, 1, 3, 15]

# Method map
# 0 - left rect
# 1 - mid rect
# 2 - right rect
# 3 - trapez.
# 4 - simps.
method_map = [
  (left_rec_method, 'Left rect method'),
  (mid_rec_method, 'Mid rect method'),
  (right_rec_method, 'Rigth rect method'),
  (trapez_method, 'Trapez method'),
  (simps_method, 'Simps method')
]

def compute_with_runge(func: Callable[[float], float], a: float, b: float, eps: float, method: int) -> Tuple[float, int]:
  n: int = 4
  k: int = runge_coeffs[method]
  res = method_map[method][0](func, a, b, n)

  n *= 2
  precise_res = method_map[method][0](func, a, b, n)
  while abs(precise_res - res) / k >= eps:
    n *= 2
    precise_res =  method_map[method][0](func, a, b, n)
    res = precise_res
  
  return (res, n // 2)


if __name__ == '__main__':
  try:
    print('Choose desired function (just enter the number): ')
    id: int = 1
    for ft in func_map:
      print(f'{id}. {ft[1]}')
      id += 1
    chosen_func: Callable[[float], float] = func_map[int(input('Chosen func: ')) - 1][0]
    a: float = float(input('Enter lowest integration limit: '))
    b: float = float(input('Enter hiest integration limit: '))
    eps: float = float(input('Eps (accuracy): '))

    print('Choose desired integration method (just enter the number): ')
    id = 1
    for mt in method_map:
      print(f'{id}. {mt[1]}')
      id += 1
    
    chosen_method_id: int = int(input('Chosen method: ')) - 1
    chosen_method: Callable[[Callable[[float], float], float, float, int], float] = method_map[chosen_method_id][0]
    
    if check_convergence(chosen_func, a, b):
      calc_res: Tuple[float, int] = compute_with_runge(chosen_func, a, b, eps, chosen_method_id)
      print(f'Integration result: {calc_res[0]}')
      print(f'Number of divisions of the integration interval to achieve the required accuracy: {calc_res[1]}')
    else:
      print('Integral does not exist')
  except Exception:
    print('Stupid user!')
