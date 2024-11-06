'''
q = 2
f = 150
z = int(input('Введите число:'))
if z>f and z//q:
    print('число четное и больше 150,',z)
else:
    print('другое',z)
'''

'''    
z = int (input('1'))        
w = int (input('2'))
q = int (input('3'))
s = q+w+z
d = s/3
print('сумма чисел  = ',s)
print('средние арифмитическое = ',d)
'''
'''
z = int(input('Введите число: '))
if z>0 and z//2:
     print('число четное и больше 0 ')
else:
    if z>0:
        print('число нечетное и больше 0 ')
    else:
        if z==0:
            print('число = 0')
'''
'''
for i in range(0,50,5):
    print(i)
'''
'''
a=int(input('Введите цену первого билета: '))
m= a
g= 1
print('Цена нового билета:', a,'Колличество билетов:', 1,'Текущая сумма:', m)
while a  <= 250:
    a=int(input('Введите цену нового билета: '))
a += m
g += 1
print('Цена нового билета:', a,'Колличество билетов:', g,'Текущая сумма:', m)
'''
kol=0

start=int(input('Введите начальное значение интервала'))
fin=int(input('Введите конечное значение интервала'))
chislo=int(input('Введите число'))
for i in range(start,fin):
    print('i=',8)
    if i%chislo==0:
      print('Очередное искомое число: ',i) 
      kol+=1   

print('Всего ',kol,'чисел')












