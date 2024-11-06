'''
z='Волк'
print(z)
l=list()
print(l)
i_new=[]
i_new=list(z)
print(i_new)
'''
'''
x=y=[1,5]
print('пес,голова,тело:',x,'рука,рот,зуб:',y)
y[1]=100
print('пес,голова,тело:',x,'рука,рот,зуб:',y)
x,y=[1,5],[1,5]
print('пес,голова,тело:',x,'рука,рот,зуб:',y)
y[1]=100
print('ВОДА,голова,тело:',x,'рука,рот,зуб:',y)
'''
'''
import copy
x=[1,2,3,4,5]
print(x)
y=list(x)
print(y)
z=x[:]
print(z)
print(x is y)
print(x is z)
y[1]=100
z[0]=200
print(x)
print(y)
print(z)
'''
'''
import copy
x=[1,[2,3,4,5]]
print(x)
y=list(x)
print(y is x)
y[1][2]=100
print(x)
print(y)
'''
'''
import copy
x=[1,[2,3,4,5]]
y=copy.deepcopy(x)
y[1][2]=100
print('Это список x',x)
print('Это список y',y)
x=[1,2]
print('Это список x',x)
y=[x,x,23]
print('Это список y',y)
z=copy.deepcopy(y)
print(z[0] is x)
print(z[1] is x)
print(z[0] is z[1])
'''


