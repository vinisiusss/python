'''
import webbrowser

def val(func):
    def wap(url):
        if "4" in url:
            func(url)
        else:
            print("neverniy url")
    return wap
    
@val

def open(url):
    webbrowser.open(url)

open("https://www.labirint.ru/books/311244/")
'''
import webbrowser
z = 45
print (z) 
s = input("z=")
if z == s:
    webbrowser.open open("https://www.labirint.ru/books/311244/")
