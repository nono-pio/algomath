def diviseur(n: int):
  result = []
  for i in range(1, n // 2):
    if n % i == 0: result.append(i)
  result.append(n)
  return n


print(diviseur(18))