#/usr/bin/python
'''
给定区间[-2的31次方, 2的31次方]内的3个整数A、B和C，请判断A+B是否大于C。
'''

T = input()
li = []
for i in range(int(T)):
    str1 = input()
    arr = [int(n) for n in str1.split()]
    if (arr[0]+arr[1] > arr[2]):
        str2 = "Case #"+str(i+1)+": true"
    else:
        str2 = "Case #"+str(i+1)+": false"
    li.append(str2)
for value in li:
    print(value)
    
