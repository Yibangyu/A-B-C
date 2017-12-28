#/usr/bin/python

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
    
