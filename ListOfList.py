# NIM         : 24060121140118
# Nama        : Ananda Rizky Pratama
# Deskripsi   : Membuat Fungsi yang menyangkut List of list
# Tanggal     : 14 November 2021

def IsEmpty(L):
    return L == []
def FirstElmt(T):
    if not IsEmpty(T):
        return T[0]
    else:
        return []
def LastElmt(L):
    if not IsEmpty(L):
        return L[-1]
    else:
        return []
def Head(L):
    if not IsEmpty(L):
        return L[:-1]
    else:
        return []
def Tail(T):
    if not IsEmpty(T):
        return T[1:]
    else:
        return []
def IsMember(X, L):
    if IsEmpty(L):
        return False
    elif FirstElmt(L) == X:
        return True
    else:
        return IsMember(X, Tail(L))
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))
def Konso(x, l):
	return [x] + l
def Kons(l, x):
	return l + [x]
def Konsa(x, y, l):
	return [y] + [x] + l
def Rember(x, l):
    if IsEmpty(l):
        return []
    elif FirstElmt(l)==x:
        return Tail(l)
    else:
        return Konso(FirstElmt(l), Rember(x, Tail(l)))
def ApakahPrima(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
          
def IsAtom(e):
    if (type(e)!= list):
        return True
    else:
        return False
def IsList(e):
    if (type(e)==list):
        return True
    else:
        return False
        
# Nomer 1
# DefSpek
# NbEleX : elemen, list of list --> integer
# NbEleX (L,X) menentukan banyaknya X dalam list L

# Realisasi
def NbEleX(L,X):
      if IsEmpty(L):
            return 0
      else:
            if IsAtom(FirstElmt(L)):
                  if FirstElmt(L) == X:
                        return 1 + NbEleX(Tail(L), X)
                  else:
                        return NbEleX(Tail(L), X)
            elif IsList(FirstElmt(L)):
                  if FirstElmt(FirstElmt(L)) == X:
                        return 1 + NbEleX(Tail(FirstElmt(L)), X) + NbEleX(Tail(L), X)
                  else:
                        return NbEleX(Tail(FirstElmt(L)), X) + NbEleX(Tail(L), X)

# aplikasi : NbEleX(L1,4) --> 3
print("====Nomor 1====") 
L1 = [[4], 2, [3,4], 1, 4]
print(NbEleX(L1,4))

# Nomer 2
# DefSpek
# KaliMatrix : Integer, list of list dalam bentuk matrix --> list
# KaliMatrix (k, L) menghasilkan matrix dalama bentuk list
# yang telah dikali dengan suatu konstanta K

# Realisasi
def KaliMatrix(k, L):
      if IsEmpty(L):
            return []
      else:
            if IsList(FirstElmt(L)):
                  return Konso(Konso(FirstElmt(FirstElmt(L))*k, KaliMatrix(k, Tail(FirstElmt(L)))), KaliMatrix(k, Tail(L)))
            else:
                  return Konso(FirstElmt(L)*k, KaliMatrix(k, Tail(L)))

# aplikasi : KaliMatrix(2, L3) --> [[2,4,6],[8,10,12],[14,16,18]]
print("====Nomor 2====")
L3 = [[1,2,3], [4,5,6], [7,8,9]]
print(KaliMatrix(2, L3))

# Nomer 3
# DefSpek
# NbList : list of list --> integer
# NbList (L) menghitung jumlah list dalam list L

# Realisasi 
def NbList(L):
      if IsEmpty(L):
        return 0
      else:
            if IsList(FirstElmt(L)):
                  return 1 + NbList(Tail(L))
            else:
                  return NbList(Tail(L))

# aplikasi : NbList(L4) --> 2
#               NbList(L3) --> 3
#               NbList(L2) --> 0
print("====Nomer 3====")
L4 = [1, [2,3], [4]]
L3 = [[5], [6], [7]]
L2 = [8, 9, 10]
print(NbList(L4))
print(NbList(L3))
print(NbList(L2))