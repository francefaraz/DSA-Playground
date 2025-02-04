
def smart_div(func):
    print("act")
    def inner(a,b,c):
        print('enterd into inner')
        print(c)
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
# def div1(a,b):
#     print(a+b)
#     return a+b
@smart_div
def div2(a,b):
    print(a/b)
print('vade')
# div1(3,7)
div2(2,8,99)

#second way 
def divi1(a,b):
    print(a/b)


div3=smart_div(divi1)
div3(3,9,99)





