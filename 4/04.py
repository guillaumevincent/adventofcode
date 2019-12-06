a = 0
for pwd in range(256310, 732736 + 1):
    digits = [int(x) for x in str(pwd)]
    has_p = any(
        [
            (i == 0 or digits[i] != digits[i - 1])
            and digits[i] == digits[i + 1]
            and (i == len(digits) - 2 or digits[i] != digits[i + 2])
            for i in range(len(digits) - 1)
        ]
    )
    has_d = any([digits[i] > digits[i + 1] for i in range(len(digits) - 1)])
    if has_p and not has_d:
        a += 1
print(a)
