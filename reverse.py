def reverse_list(n):
    n = n[::-1]
    n = [i[::-1] for i in n]
    return n

liste2=[[1, 2], [3, 4], [5, 6, 7]]

print(reverse_list(liste2))
