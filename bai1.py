"""
1. Viết một chương trình Python để tìm tất cả các số nguyên tố trong một dãy
 số cho trước, sau đó sắp xếp dãy số tìm được theo chiều từ lớn đến bé và in ra dãy
 số đó đây là dãy số cho trước [18, 9, 99, 23, 11, 4, 13, 97, 1, 3]
"""
day_so = [18, 9, 99, 23, 11, 4, 13, 97, 1, 3]
ds_snt = []
def list_snt(danhsach):
    for x in danhsach:
        for i in range(2, x):
            if x % i == 0:
                break
            else:
                ds_snt.append(x)
                break
    return ds_snt
    
print(list_snt(day_so))
print(ds_snt)


ds_snt.sort(reverse=False)
print(ds_snt)




                