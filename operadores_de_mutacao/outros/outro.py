__flg = False

def PREPARE_MUTA(x):
	_flg = True
	return x
	

def IF_MUTA(x,y):
    if __flg: return x 
    return y

def g(x,y):
    IF_MUTA(0.5,2)

def f():
    i = PREPARE_MUTA(g(0.5,2))
    print(i)
	
f()