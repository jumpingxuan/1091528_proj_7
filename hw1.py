print("input:",end="")
y=input()
ys=y.split(",")
#print(ys)
print(len(ys))
m={'*':"*",'#':"#",'@':"@",'$':"$"}
#改變symbol所代表的value
for i in range(0,len(ys)):
    if ys[i][0]=='*':
        m['*']=ys[i][2]
    elif ys[i][0]=='#':
        m['#']=ys[i][2]
    elif ys[i][0]=='@':
        m['@']=ys[i][2]
    elif ys[i][0]=='$':
        m['$']=ys[i][2]
print(m) #沒錯，直接輸出這一行就好了

#讀檔案輸出每一行
f=open("symbols.txt")
for i in range(20):
    s=f.readline()
    print(s)
    for j in range(0,len(s)-1): #注意keyerror寫什麼 
        print(m[s[j]], end="")
        # if s[j]=='*':
        #     print(m['*'],end="")
        # elif s[j]=='#':
        #     print(m['#'],end="")
        # elif s[j]=='@':
        #     print(m['@'],end="")
        # elif s[j]=='$':
        #     print(m['$'],end="")
    print('\n')

