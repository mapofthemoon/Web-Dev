x = input()

rvrs= 0
for digit in str(x)[::-1]:
    rvrs = rvrs * 10 + int(digit)
print(rvrs)