def len(a):
    if a == '':
        return 0
    else:
        return(1+len(a[1: ]))
a=input()
print(len(a))
