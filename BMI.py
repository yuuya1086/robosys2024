#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Yuuya Tanaka s23c1086uu@s.chibakoudai.jp
# SPDX-License-Identifier: BSD-3-Clause

import sys

n = float(sys.argv[1])
m = float(sys.argv[2])

n = n / 100

BMI = m / (n * n)
tekisei = (n * n) * 22

print("あなたのBMI値は"'{:.2f}'.format(BMI))
print("適正体重は{:.1f}kg".format(tekisei))

if BMI < 18.50:

    print("瘦せ型です")

elif BMI > 25.00:

    print("肥満です")

else:

    print("適正です")
