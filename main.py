import numpy as np

def rac(x, n = 1):
  sign = np.angle(x)
  x = np.abs(x)

  result = []

  for i in range(n):
    result.append(pow(x,1/n)*(np.cos(sign)+np.sin(sign)*1j))
  
  return result

print(rac(4,2))