pos=-1
def search(list,n):
    for i in range(0,len(list)):
        if list[i]==n:
            globals()['pos']=i
            i = i + 1
            return True


    return False
list=[]
n=int(input())
m=int(input())
for j in range(0,m):
    ele = int(input())
    list.append(ele)
    list=sorted(list)
print(list)
if search(list,n):
    pr
    int("Found at",pos)
else:
    print("Not Found")
