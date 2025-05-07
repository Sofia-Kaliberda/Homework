lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
new_lst = []
zero_count = 0

for numb in lst:
    if numb == 0:
        zero_count += 1
    else:
        new_lst.append(numb)

new_lst.extend([0] * zero_count)
print("result:", new_lst)