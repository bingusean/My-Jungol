i = input().split()
ii = list(map(int, i))
i1, i2, i3, i4, i5 = (ii)

c100 = c90 = c80 = c70 = c60 = c50 = c40 = c30 = c20 = c10 = c0 = 0

if i1 == 100: c100 += 1
elif i1 > 90: c90 += 1
elif i1 >= 80: c80 += 1
elif i1 >= 70: c70 += 1
elif i1 >= 60: c60 += 1
elif i1 >= 50: c50 += 1
elif i1 >= 40: c40 += 1
elif i1 >= 30: c30 += 1
elif i1 >= 20: c20 += 1
elif i1 >= 10: c10 += 1
elif i1 >= 0: c0 += 1

if i2 == 100: c100 += 1
elif i2 >= 90: c90 += 1
elif i2 >= 80: c80 += 1
elif i2 >= 80: c80 += 1
elif i2 >= 70: c70 += 1
elif i2 >= 60: c60 += 1
elif i2 >= 50: c50 += 1
elif i2 >= 40: c40 += 1
elif i2 >= 30: c30 += 1
elif i2 >= 20: c20 += 1
elif i2 >= 10: c10 += 1
elif i2 >= 0: c0 += 1

if i3 == 100: c100 += 1
elif i3 >= 90: c90 += 1
elif i3 >= 80: c80 += 1
elif i3 >= 70: c70 += 1
elif i3 >= 60: c60 += 1
elif i3 >= 50: c50 += 1
elif i3 >= 40: c40 += 1
elif i3 >= 30: c30 += 1
elif i3 >= 20: c20 += 1
elif i3 >= 10: c10 += 1
elif i3 >= 0: c0 += 1

if i4 == 100: c100 += 1
elif i4 >= 90: c90 += 1
elif i4 >= 80: c80 += 1
elif i4 >= 70: c70 += 1
elif i4 >= 60: c60 += 1
elif i4 >= 50: c50 += 1
elif i4 >= 40: c40 += 1
elif i4 >= 30: c30 += 1
elif i4 >= 20: c20 += 1
elif i4 >= 10: c10 += 1
elif i4 >= 0: c0 += 1

if i5 == 100: c100 += 1
elif i5 >= 90: c90 += 1
elif i5 >= 80: c80 += 1
elif i5 >= 80: c80 += 1
elif i5 >= 70: c70 += 1
elif i5 >= 60: c60 += 1
elif i5 >= 50: c50 += 1
elif i5 >= 40: c40 += 1
elif i5 >= 30: c30 += 1
elif i5 >= 20: c20 += 1
elif i5 >= 10: c10 += 1
elif i5 >= 0: c0 += 1

if c100 != 0: print("100: " + str(c100) + " person")
if c90 != 0: print("90: " + str(c90) + " person")
if c80 != 0: print("80: " + str(c80) + " person")
if c70 != 0: print("70: " + str(c70) + " person")
if c60 != 0: print("60: " + str(c60) + " person")
if c50 != 0: print("50: " + str(c50) + " person")
if c40 != 0: print("40: " + str(c40) + " person")
if c30 != 0: print("30: " + str(c30) + " person")
if c20 != 0: print("20: " + str(c20) + " person")
if c10 != 0: print("10: " + str(c10) + " person")
if c0 != 0: print("0: " + str(c0) + " person")
