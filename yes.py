# a="olma"
# b="anor"
# c=""3
# for i in range(len(a)):
#     c = c+a[i]+b[i]
# print(c)
# a=int(input('son kiriting:'))
# for i in range(2, a+1):
#     if i/a==1 and a%2==1:
#         print('tub')
#     else:
#         print('tub emas')


# a=[1, 4, 5, 6, 9, 45, 87, 90]
# b=[2, 8, 3, 2, 23]
# s=[]
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i] == b[j]:
#            s.append(a+b)
#            print(s)


# import numpy as np
# matrix_a = np.array([[1, 1, 1],
#                     [1, 1, 1],
#                     [1, 1, 2]])
#
# matrix_b = np.array([[1, 3, 1],
#                      [1, 3, 1],
#                      [1, 3, 8]])
#
#
# matrix_d = np.array([[1, 1, 1],
#                      [1, 0, 0],
#                      [1, 0, 1]])
#
# d=np.add(matrix_a, matrix_b, matrix_d)
# print(d)

# f=input("a=")
# b=input("harf=")
# d=0
# for i in range(len(f)):
#     if f[i]==b:
#           d +=1
# # print(f"soz ichida {d} harf bor ")
# d="SamarqanD"
# g=""
# f=""
# for i in d:
#    if i.isupper():
#         g=g+i
#
#    elif i.islower():
#         f=f+i
# print(g, f)

####  small number
# a=[12, 0, 56, 90, 78, 232323]
# s=a[0]
# for i in a:
#     if s>i:
#         s=i
# print(s)


# a=[10, 2, 3, 24, 5, 6, 7, 88, 9, 1, 11, 12]
# for i in range(len(a)):
#     for j in range(0, len(a)):
#            #print(i, j)
#           if a[i]>a[j]:
#               a[i],a[j]=a[j],a[i]
#
# print(a)

#### #  update

# a={"price":50000,
#    "title":"super lang",
#    "body":"note",
#    "color":"blue"
#    }
# a['price']  = 100000
# a['color'] = "green"
#
# print(a)



# a={"price": "language",
#    "title": 233434,
#    "body":  "super",
#    "color": 2
#    }
#
# c=list(a.values())
#
# for i in range(len(c)):
#     for j in range(0, len(c)):
#           if str(c[i])<str(c[j]):
#               c[i],c[j]=c[j],c[i]
# print(c)

#
# mytuple = (1, 2, 5, 4, 0)
#
#
# print(sorted(mytuple))
#

# b=int(input("b="))
# s={}
#
# for i in range(1, b+1):
#      s[i]=i**2
#
# print(s)
#
# f=input("")

#####  7

# a=input("A=")
# c={}
# for i in a:
#     v=a.count(i)
#     c[i]=v
# print(c)
#
#
#
# a=input("A=")
# c={}
# for i in a:
#      if i in c:
#         c[i] +=1
#      else:
#           c[i]=1
#
# for i,j in c.items():
#     print(f"{i}{j}")



# a=(2, 5, 9, "hello", [90, 4], 5)
# for i in a:
#     print(i*10)
#
#
# x=(2, "hello", [1, 78, 2], 2,"hello")
# print(x[2].count(2))
#

# a=("W", "Q", "Y", "R", "Dilshod", 90)
# n=input("A=")
# m=list(a)
# for i in range(len(m)):
#     if m[i]==n:
#         m.remove(i)
#
#     elif int(m[i])==int(n):
#         m.remove(i)
#
#
# print(tuple(m))

#####  Tuple   and Set


#####  Tartibsiz, dublikat qiymat qabul qilmaydi,Indexsiz, dict va List ni qabul qilmaydi

#
# a={12,"hello",12, 9.1, (12,)}
# for i in a:
#     print(type(i))



# a = {"Q", "E", "I", "T"}
# b =  {"U", "O", "B","Q", "P"} ##### update funksiya bilan setlarni bir biriga qoshamz
# a.update(b)
# print(a, type(a))



###### bu funksiya bilan setlarni ichidan keraklisini ochirib yuboramz


#
# a = {"Q", "E", "I", "T","R"}
# a.remove("A")
# print(a)


####### agar setni ichida bolmasa hatolik bermidi
# a = {"Q", "E", "I", "T", "E"}
# a.discard("B")
# print(a)


###### listga otkazish
# a = {"Q", "E", "I", "T", "E"}
# b=list(a)
# print(a)



#######
# a = {"Q", "O", "I", "T", "E"}
# b =  {"R", "U", "E"}
# a.pop()    ####  genaratsiya qilib ochiradi
# b.pop()
# print(a)


# ######
# a={"Q", "O", "I", "T", "B"} ###   1, 2
# b={"A", "U", "R", "B"}  ### 1, 2
# b.intersection_update(a)
# print(b)
#

#####
# s = {-9,1,7,5,9,-1,-5,-3,3,-7}
# print(sorted(s))


# a=[(10, 20, 30), (40, 50, 60), (70, 80, 90)]
# f=list(a[0])
# f.pop()
# f.append(100)
# print(f)

# for i in a:
#     g= list(i)
#     g.pop()
#     g.append(100)
# print(g)

# a=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), (),('d')]
# s=tuple(a)
# for i in s:
#     if i==():
#         a.remove(i)
# print(a)
#

#####  Set   #####   Tartibsiz, Indexsiz, List and Dict qabul qilmaydi

# a={12, 56, "hello", 90.2,  12, (1,)}
# b={12, 34, "good", 56}
#
#
# b.intersection_update(a)
# print(b)



#######    add()

# a={"A", "d", "d", 78}
# s=input("K=")
# a.add(s)
# print(a)



########
# a = {"Q", 89, "I", 90}
# b = {"U", "O", "B","Q", 89, 90}
# a.update(b)
# print(a)



###### bu funksiya bilan setlarni ichidan keraklisini ochirib yuboramz
# a = {"Q", "E", "I", "T","R"}
# s=input("K=")
# for i in a:
#    if i==s:
#   #a.remove("U")
#      a.discard(i)
#      print(a)


# from datetime import datetime
#
# b=input("Ism=")
# a=int(input("Tugilgan yilingiz="))
#
# time = datetime.now()
# year = time.year-a
#
# print(year)


#

# import calendar
# b=calendar.month(2024, 3)
# print(b)




n=int(input("A="))
s=0
for i in range(1, n+1):
          s=s+i**2
          print(s)









