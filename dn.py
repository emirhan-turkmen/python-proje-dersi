def reversed(liste):
    reverse_list = liste
    for item in liste:
        if isinstance(item, list):
            reverse_list.extend(reversed(item))
        else:
            reverse_list.append(item)
            break
    return reverse_list

liste1 = [[1, 2], [3, 4], [5, 6, 7]]
print("/////////////////////////")
liste1 = reversed(liste1)
print(liste1)   