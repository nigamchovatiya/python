
# Count vowels
char = "nigam Ae"
vowel = "aeiouAEIOU"
count = 0

for n in char:
    if n in vowel:
        count = count + 1
        print(n)  # (i,a,A,e)

print("total vowel in ", count)  # 4
