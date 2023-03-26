a = input()
b = input()
if b == "1":
    if a[0] == a[-1] and a[1] == a[-2]:
        print("YES")
    else:
        print("NO")
else:
    print("YES")