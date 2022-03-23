def sumar(a, b):
    return a + b

print(sumar(4, 5))
print(sumar(a=5, b=6))

parametros = {
    'a':45,
    'b':120
}

print(sumar(**parametros))
print(sumar(**{'a':451, 'b':120}))

print(sumar(*[12, 45]))

def restar(**kwargs):
    return(kwargs)

print(restar(d=5,f=52,t=6,uid=458))