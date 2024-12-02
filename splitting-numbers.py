def num_split(num):
  sign = 1 if num >= 0 else -1
  num *= sign
  result = []

  if num == 0:
    return [0]

  while num > 0:
    result.insert(0, num % 10 * 10 ** (len(result)) * sign)
    num //= 10

  return result

if __name__ == "__main__":
  test = [39, -434, 100, 0]
  for t in test:
    print(num_split(t))
  
