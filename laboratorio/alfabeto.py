frase = input().lower()
caratteri = {}

for c in frase:
    if not c.isalpha():
        continue
    if c not in caratteri:
        caratteri[c] = 1
    else:
        caratteri[c] += 1

print(" ".join([f"{k}{v}" for k, v in caratteri.items()]))
