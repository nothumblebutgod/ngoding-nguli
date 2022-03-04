# Nama file: Tugas_Pert8.py
# Pembuat: Ananda Rizky Pratama
# Tanggal: 30 October 2021
# Deskripsi: membuat fungsi-fungsi list dengan cara rekursif

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

# Soal 
# 0
# DefSpek
# NbVokal : list of char --> integer
# NbVokal(l) menghitung banyak elemen vokal dalam list

def NbVokal(L):
    if IsEmpty(L):
        return 0
    else :
        if FirstElmt(L) in ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']:
            return 1 + NbVokal(Tail(L))
        else :
            return NbVokal(Tail(L))

#1
#SumElmt : list of integer --> integer
#SumElmt(L) menghasilkan jumlah semua elemen dalam list
#REALISASI
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))

#2
#KEMUNCULAN MAKSIMUM versi-2
#maxNb : list of integer --> <integer, integer>
#maxNb(Li) menghasilkan <nilai maksimum, kemunculan nilai maksimum> dari suatu list integer Li; <m,n> = m adalah maks x dari n
#          occurence m dalam list
#
#max : list of integer --> integer
#max(Li) menghasilkan nilai maksimum dari elemen suatu list integer Li
#
#Vmax : list of integer --> integer
#Vmax(Li) adalah NbOcc(max(Li),Li) yaitu banyaknya kemunculan nilai maksimum dari
#         Li, dengan aplikasi terhadap NbOcc(max(Li),Li)
#
#NbOcc : integer, list of integer --> integer > 0
#NbOcc(X,Li) yaitu banyaknya kemunculan nilai X pada Li
#REALISASI
def maxNbCount(Li, max):
    if IsEmpty(Li):
        return 0
    else:
        if FirstElmt(Li) == max:
            return 1 + maxNbCount(Tail(Li), max)
        else:
            return maxNbCount(Tail(Li), max)

def maxNb(Li):
    return max(Li), maxNbCount(Li, max(Li))

def max(Li):
    if IsEmpty(Li):
        return 0
    else:
        if FirstElmt(Li) > max(Tail(Li)):
            return FirstElmt(Li)
        else:
            return max(Tail(Li))

def Vmax(Li):
    return NbOcc(max(Li),Li)

def NbOcc(X, Li):
    if IsEmpty(Li):
        return 0
    else:
        if FirstElmt(Li) == X:
            return 1 + NbOcc(X, Tail(Li))
        else:
            return 0 + NbOcc(X, Tail(Li))

# 3
# LPrime(L) : list of integer --> list
# LPrime(L) menghasilkan list baru yang dimana isinya hanya bilangan prima
def LPrime(L):
    if not IsEmpty(L):
        if ApakahPrima(FirstElmt(L)):
            return Konso((FirstElmt(L)), LPrime(Tail(L)))
        else:
            return LPrime(Tail(L))
    else:
        return []

# 4
#InsertAfter: list --> list
#InsertAfter(L,x,e) menghasilkan list baru dimana menambahkan elemen x setelah elemen e
#REALISASI
def InsertAfter(L, x, e):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == e:
            return [FirstElmt(L)] + [x] + InsertAfter(Tail(L), x, e)
        else:
            return [FirstElmt(L)] + InsertAfter(Tail(L), x, e)

#5
#MakeMinus: 2 set --> set
#MakeMinus(H1,H2) membuat set baru dimana anggota H1 yang BUKAN merupakan anggota H2
def MakeMinus(H1, H2):
    if IsEmpty(H1):
        return []
    else:
        if FirstElmt(H1) in H2:
            return MakeMinus(Tail(H1), H2)
        else:
            return [FirstElmt(H1)] + MakeMinus(Tail(H1), H2)

#6
#MakeKomplemen: 2 set --> set
#MakeKomplemen(H1,H2)   membuat set baru yang anggotanya adalah anggota semua anggota H1 dan H2
#                       tetapi bukan interseksi keduanya
# Realisasi
def MakeKomplemen(H1, H2):
    if IsEmpty(H1):
        return H2
    elif IsEmpty(H2):
        return H1
    else:
        return MakeMinus(H1, H2) + MakeMinus(H2, H1)

# Aplikasi
print('Nomor 0')
L = ['a', 'i', 'e', 'd', 'o','f','g']
print(NbVokal(L))
print('Nomor 1')
L = [1,2,3,4]
print(SumElmt(L))
print('Nomor 2')
L1 = [1,4,4,4,5,5,7,8,8,8,8]
L2 = [2,2,4,5,5,7,9,9,9,9,9]
print(maxNb(L1))
print(maxNb(L2))
print(max(L1))
print(max(L2))
print(Vmax(L1))
print(Vmax(L2))
print(NbOcc(4, (L1)))
print(NbOcc(2, (L2)))
print('Nomor 3')
L = [1,4,4,4,5,5,7,8,8,8,8]
print(LPrime(L1))
print('Nomor 4')
L = [2,3,4,6,7,9,11,14,]
print(InsertAfter(L, 5 , 4))
print('Nomor 5')
L1 = [0, 1, 2, 3, 7]
L2 = [1, 2, 3, 6, 8]
print(MakeMinus(L1, L2))
print('Nomor 6')
L1 = [0, 1, 2, 3, 7]
L2 = [1, 2, 3, 6, 8]
print(MakeKomplemen(L1, L2))