# Nama file : tree.py
# Pembuat : Ananda Rizky Pratama
# NIM : 24060121140118
# Tanggal :  25 November 2021
# Deskripsi : Membuat berbagai macam fungsi yang berhubungan dengan tree

# Modul Umum
def is_empty(S):
    return S == []

def first(S):
    return S[0]

def tail(S):
    return S[1:]

def nb_element(L):
    if is_empty(L):
        return 0
    else:
        return 1 + nb_element(tail(L))

def isOne(L):
    if L == 0:
        return False
    elif nb_element(L)==1:
        return True
    else:
        False

def is_list(S):
    if type(S) == list:
        return True
    else:
        return False
    
def IsMember(x, L):
    if (istreeEmpty(L)):
        return False
    else:
        if first(L) == x:
            return True
        else:
            return IsMember(x, tail(L))
        
def KonsoPB(e, L):
      return [e] + L

def listTengah(list):
	return list[len(list)//2]

def bagiList1(list):
	return list[:len(list)//2]

def bagiList2(list):
	if len(list) % 2 == 0:
		return list[((len(list)+1)//2)+1:]
	else:
		return list[(len(list)+1)//2:]

def Insert(x,L):
  if is_empty(L):
    return [x]
  else:
    if x <= first(L):
      return KonsoPB(x,L)
    else:
      return KonsoPB(first(L), Insert(x, tail(L)))

def SortMin(L):
  if is_empty(L):
    return []
  else:
    return Insert(first(L), SortMin(tail(L)))

#=====================================================
def makePB(root, left, right):
    return [root, left, right]

def root(P):
    return P[0]

def left(P):
    return P[1]

def right(P):
    return P[2]

def istreeEmpty(P):
    if P == None:
        return True
    else:
        return False

def isOneElmt(P):
    if not istreeEmpty(P) and istreeEmpty(left(P)) and istreeEmpty(right(P)):
        return True
    else:
        return False
    
def isUnerLeft(P):
    if not istreeEmpty(P) and not istreeEmpty(left(P)) and istreeEmpty(right(P)):
        return True
    else:
        return False

def isUnerRight(P):
    if not istreeEmpty(P) and istreeEmpty(left(P)) and not istreeEmpty(right(P)):
        return True
    else:
        return False

def isbiner(P):
    if not istreeEmpty(P) and not istreeEmpty(left(P)) and not istreeEmpty(right(P)):
        return True
    else: 
        return False

def isExistLeft(P):
    if not istreeEmpty(P) and not istreeEmpty(left(P)):
        return True
    else:
        return False

def isExistRight(P):
    if not istreeEmpty(P) and not istreeEmpty(right(P)):
        return True
    else:
        return False

def NbElmt(P):
    if istreeEmpty(P):
        return 0
    elif isOneElmt(P):
        return 1 
    else:
        if isbiner(P):
            return NbElmt(left(P)) + 1 + NbElmt(right(P))
        elif isUnerLeft(P):
            return NbElmt(left(P)) + 1
        elif isUnerRight(P):
            return NbElmt(right(P)) +1
        else:
            return 0

def repPrefix(P):
    if isOneElmt(P):
        return [root(P)]
    else:
        if isbiner(P):
            return [root(P)] + [repPrefix(left(P))] + [repPrefix(right(P))]
        elif isUnerLeft(P):
            return [root(P)] + [repPrefix(left(P))]
        elif isUnerRight(P):
            return [root(P)] + [repPrefix(right(P))]

def NbDaun(P):
    if istreeEmpty(P):
        return 0
    elif isOneElmt(P):
        return 1
    else:
        if isbiner(P):
            return NbDaun(left(P)) + NbDaun(right(P))
        elif isUnerLeft(P):
            return NbDaun(left(P))
        elif isUnerRight(P):
            return NbDaun(right(P))
        else:
            return 0
        
def faktor(n,count):
    if(n == count):
        return 1
    elif(n % count == 0):
        return 1 + faktor(n,count+1)
    else:
        return faktor(n,count+1)
    
def SortMin(L):
    if is_empty(L):
        return []
    else:
        return Insert(first(L), SortMin(tail(L)))

# BSearch : binSearchTree, element --> boolean
# {BSearch(P,x) mengirimkan true jika ada node dari pohon binary search tree P yang bernilai X, mengirimkan false jika tidak ada}

#Realisasi
def BSearch(P, x):
    if istreeEmpty(P):
        return False 
    else:
        if root(P) == x:
            return True
        else:
            return BSearch(left(P), x) or BSearch(right(P), x)

         
# AddX(P,x) : binSearchTree, elemen --> pohonbiner
# {AddX (P,x) menghasilkan sebuah ppohon binary search tree P dengan tambahan simpul X, belum ada simpul P yang bernilai X}    

# Realisasi
def AddX(P,x):
    if istreeEmpty(P):
        return [x, None, None]
    else:
        if root(P) > x:
            return makePB(root(P),AddX(left(P),x),right(P))
        else:
            return makePB(root(P),left(P),AddX(right(P),x))
    

# makebintree : list of element --> pohon biner
# {makebintree(L) menghasilkan sebuah pohon binary search tree P yang elemennya berasal dari elemen list L yang dijamin unik}

# Realisasi
def makeBinSearchTree(L):
	if is_empty(L):
		return None
	elif len(L) == 1:
		return L[0]
	elif len(L) == 2:
		return [L[0], None, L[1]]
	else:
		return makePB(listTengah(L),makeBinSearchTree(bagiList1(L)),makeBinSearchTree(bagiList2(L)))

def makebintree(L):
    return makeBinSearchTree(SortMin(L))

# delBtree : binsearchtree tidak kosong, elemen --> pohon biner
# {delBtree(P,x) menghasilkan sebuah pohon binary search tree p tanpa node yang bernilai x, x pasti ada sebagai salah satu node, tree menghasilkan tree kosong jika p hanya terdiri dari x}        

#Realisasi
def delBTree(P,x):
    if root(P) == x:
        return None
    else:
        if x < root(P):
            return makePB(root(P),delBTree(left(P), x),right(P))
        else:
            return makePB(root(P),left(P),delBTree(right(P),x))
        

# makeBaltree : list of node, integer --> binBaltree
# {menghasilkan sebuah balace tree dengan n node, nilai setiap node yang berasal dari list}

# Realisasi

def makeBalanceTree(L):
    if is_empty(L):
	    return None
    elif len(L) == 1:
	    return L[0]
    elif len(L) == 2:
	    return [L[0], None, L[1]]
    else:
	    return makePB(listTengah(L),makeBalanceTree(bagiList1(L)),makeBalanceTree(bagiList2(L)))

def makeBaltree(L):
	return makeBalanceTree(SortMin(L))

# Aplikasi
L1 = [5,3,7,2,6,9]
L2 = [5,3,7,2,6,9,10,54,24,13]
P1 = makePB(6,makePB(7,makePB(4,None,None),makePB(6,None,None)),makePB(8,makePB(5,None,None),makePB(12,None,None)))
P2 = makePB(8,makePB(5,makePB(1,None,None),makePB(4,None,None)),makePB(6,None,None))
print(BSearch(P1,12))
print(makebintree(L1))
print(AddX(P1,9))
print(delBTree(P2,1))
print(makeBaltree(L2))