s = 0
for i in range(1,15):
    if i % 4 == 0:
        continue
    if i > 10 and i % 2 == 0:
        break
    s = s + i
print(f'{s},SIX SEVENNNNN')