# soru 1
def flatten_list(lst):
    flattened_list = []
    for item in lst:
        if isinstance(item, list):
            """ 
            listenin elemanlarında geziyoruz item liste ise onu yeni listenin sonuna ekleyip 
            fonksiyonu tekrar çağırıyor özyineleme.
            """
            flattened_list.extend(flatten_list(item))
        else:
            """
            eğer item bir liste değilse direkt append ile liste sonuna eklenir.
            """
            flattened_list.append(item)
    return flattened_list

liste1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(liste1)
liste1 = flatten_list(liste1)
print(liste1)

# soru 2

def reverse_list(n):
    n = n[::-1]
    n = [i[::-1] for i in n]
    return n

liste2=[[1, 2], [3, 4], [5, 6, 7]]
print(liste2)
print(reverse_list(liste2))