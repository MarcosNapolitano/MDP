

b = {"ARC0050" : 642,
    "ARC0048": 10,
    "ARC0105":60} 



a = {"ARC0030" : 25, 
     "ARC0050": 501,  
     "ARC0025" : 20, 
     "ARC0048": 3}


for i in b:
    if i in a:
        a.update({i:b[i]+a[i]})
    else:
        a.update({i:b[i]})


print(a)
