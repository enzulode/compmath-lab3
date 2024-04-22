from typing import *

from functions import function1 as func1


# Rectang. methods
def left_rec_method(func: Callable[[float], float], a: float, b: float, n: int) -> float:
  h: float = (b - a) / n
  res: float = 0
  for i in range(n):
    res += func(a + i * h)
  res *= h
  return res

def mid_rec_method(func: Callable[[float], float], a: float, b: float, n: int) -> float:
  h: float = (b - a) / n
  res: float = 0
  for i in range(n):
    res += func(a + (i + 0.5) * h)
  res *= h
  return res

def right_rec_method(func: Callable[[float], float], a: float, b: float, n: int) -> float:
  h: float = (b - a) / n
  res: float = 0
  for i in range(1, n + 1):
    res += func(a + i * h)
  res *= h
  return res


# Trapez. method
def trapez_method(func: Callable[[float], float], a: float, b: float, n: int) -> float:
  h: float = (b - a) / n
  res: float = (func(a) + func(b)) / 2
  for i in range(1, n):
    res += func(a + i * h)
  res *= h
  return res


# Simps. method
def simps_method(func: Callable[[float], float], a: float, b: float, n: int) -> float:
  h: float = (b - a) / n
  res: float = func(a) + func(b)
  k: float
  for i in range(1, n):
    k = 3 + (-1) ** (i + 1)
    res += k * func(a + i * h)
  res *= h / 3
  return res

def check_convergence(func: Callable[[float], float], a: float, b: float) -> bool:
  if abs(a) == float('inf') or abs(b) == float('inf'):
    return False
  
  if func == func1:
    if a * b <= 0:
      return False
  
  return True


