a=[10,20,30,40,50]
print(a) # [10, 20, 30, 40, 50]

a.append(80)
print(a) # [10, 20, 30, 40, 50, 80]

a.insert(5,60)
print(a) # [10, 20, 30, 40, 50, 60, 80]

a.remove(80)
print(a) # [10, 20, 30, 40, 50, 60]

a.remove(a[4])
print(a) # [10, 20, 30, 40, 60]

print(a[4]) # 60

print(a[2:4]) # [30, 40]

print(a[-1]) # 60

print(a.index(60)) # 4

a.append(60)
print(a.count(60)) # 2

a.sort()
print(a) #[10, 20, 30, 40, 60, 60]