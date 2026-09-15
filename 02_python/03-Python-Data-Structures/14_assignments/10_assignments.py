numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]





seen=set()
duplicate=set()


for num in numbers:
    if num in seen:
        duplicate.add(num)
    else:
        seen.add(num)



print(f"duplicates are{duplicate}")



