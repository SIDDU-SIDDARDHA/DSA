def findMajority(arr):
    n = len(arr)

    ele1, ele2 = -1, -1
    cnt1, cnt2 = 0, 0

    # Step 1: Find candidates
    for ele in arr:
        if ele == ele1:
            cnt1 += 1
        elif ele == ele2:
            cnt2 += 1
        elif cnt1 == 0:
            ele1 = ele
            cnt1 = 1
        elif cnt2 == 0:
            ele2 = ele
            cnt2 = 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    # Step 2: Count actual occurrences
    cnt1, cnt2 = 0, 0
    for ele in arr:
        if ele == ele1:
            cnt1 += 1
        elif ele == ele2:
            cnt2 += 1

    res = []
    if cnt1 > n // 3:
        res.append(ele1)
    if cnt2 > n // 3:
        res.append(ele2)

    return sorted(res)


# -------- DRIVER CODE --------
arr = [2, 2, 3, 1, 3, 2, 1, 1]

result = findMajority(arr)

print("Majority elements (> n/3):")
for x in result:
    print(x, end=" ")
