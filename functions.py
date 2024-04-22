from typing import *
import math

def function1(x: float) -> float:
  return (x * x + 2 * x - 3) / x

def function2(x: float) -> float:
  return math.sin(x - 2 * x)

def function3(x: float) -> float:
  return 3 * x * x * x + 2 * x * x - 1

def function4(x: float) -> float:
  return x ** 2

def function5(x: float) -> float:
  return 3 * x * x * x - 2 * x * x - 7 * x - 8
