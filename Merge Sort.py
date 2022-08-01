# В решении данной задачи использовал алгоритм сортировки слиянием. Алгоритм быстрой сортировки будет работать
# медленно, если опорный элемент равен наименьшему или наибольшему элементам списка. При таких условиях,
# быстрая сортировка в худшем случае будет выполняться O(n²). В отличие от сортировки слиянием, которая имеет в
# худшем случае время сортировки O(n log n).


import array as arr


# функция merge_two_list объединяет два списка
def merge_two_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


# функция merge_sort выполняет сортировку
def merge_sort(s):
    if len(s) == 1:
        return s
    else:
        middle = len(s) // 2
        left = merge_sort(s[:middle])
        right = merge_sort(s[middle:])
        return merge_two_list(left, right)


m = arr.array('i', [71, 52, 32, 36, 92, 18, 56])

print(merge_sort(m))
