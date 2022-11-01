def printRoman(n):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
      
    while n:
        div = n // num[i]
        n %= num[i]
  
        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1
n = int(input())
printRoman(n)