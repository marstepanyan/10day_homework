def build_target(target, n):
    new_target = []
    res = []
    lst = [i for i in range(1, n + 1)]
    for item in lst:
        new_target.append(item)
        res.append("Push")
        if item not in target:
            new_target.pop()
            res.append("Pop")
        if new_target == target:
            break

    return res


lst1 = [1, 3]
num = 3
print(build_target(lst1, num))
