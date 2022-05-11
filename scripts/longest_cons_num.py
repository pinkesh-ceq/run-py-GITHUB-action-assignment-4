import sys

# n = input("Enter string to get the greatest consecutive num/string : ")
n = sys.argv[1]
occurrence = {}

for i in n:
    count = 0
    for j in n:

        if i == j:  # next element is equal to previous element
            count += 1
            if j in occurrence.keys():
                if count > occurrence[j]:
                    occurrence[j] = count
                else:
                    continue
            else:
                occurrence[i] = count
        count = 0
m = max(occurrence.values())

print("Longest consecutive number(s) :", [key for key, val in occurrence.items() if val == m][0] * m)