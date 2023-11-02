def odwracanie_i(L, left, right):
    if left < 0 or right >= len(L) or left >= right:
        return

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def odwracanie_r(L, left, right):
    if left < 0 or right >= len(L) or left >= right:
        return

    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_r(L, left + 1, right - 1)