# Nama file : TugasPertemuan12.py
# Pembuat : Ananda Rizky Pratama
# NIM : 24060121140118
# Tanggal :  5 Desember 2021
# Deskripsi : Tugas pertemuan 12 mengerjakan soal UAS tahun 2020

# Nomor 1
# a.
# Definisi dan Spesifikasi
# max2: 2 integer --> integer
# max2(a,b){menentukan nilai maksimum dari a dan b}

# Realisasi:
def max2(a,b):
    if a > b :
        return a
    else:
        return b

# Aplikasi
print('==a.nomor 1==')
print(max(9,4))

# b.
# Definisi dan Spesifikasi
# min2: 2 integer --> integer
# min2 (a,b) {menentukan nilai minimum dari a dan b}
# Realisasi
def min2(a,b) :
    if a < b :
        return a
    else:
        return b

# Aplikasi
print('==b.nomor 1==')
print(min(9,4))

# c.
# max_list: list --> integer
# max_list(L) {menentukan nilai maksimum dari sebuah list}
# Realisasi
def empty_list(L):
    return L == []

def IsOneElmt(L):
    if L == 0:
        return False
    elif nb_element(L)==1:
        return True
    else:
        False

def nb_element(L):
    if empty_list(L):
        return 0
    else:
        return 1 + nb_element(tail(L))

def tail(L):
    return L[1:]

def FirstElmt(L):
    return L[0]

def max2(a,b):
    if(a > b):
        return a
    else:
        return b
        
def max_list(L):
    if(empty_list(L)):
        return 0
    elif(IsOneElmt(L)):
        return FirstElmt(L)
    else:
        return max2(FirstElmt(L), max_list(tail(L)))

# Aplikasi
L1=[5,3,1,0,-1,-2,-6]
print('==c.nomor 1==')
print(max_list(L1))


# d.
# min_list: list --> integer
# min_list(L) {menentukan bilangan minimum dari sebuah list}

# Realisasi
def empty_list(L):
    return L == []

def IsOneElmt(L):
    if L == 0:
        return False
    elif nb_element(L)==1:
        return True
    else:
        False

def nb_element(L):
    if empty_list(L):
        return 0
    else:
        return 1 + nb_element(tail(L))

def tail(L):
    return L[1:]

def FirstElmt(L):
    return L[0]

def min2(a,b) :
    if(a < b):
        return a
    else:
        return b

def min_list(L):
    if(empty_list(L)):
        return 0
    elif(IsOneElmt(L)):
        return FirstElmt(L)
    else:
        return min2(FirstElmt(L), min_list(tail(L)))

# Aplikasi
L1=[5,3,1,0,-1,-2,-6]
print('==d.nomor 1==')
print(min_list(L1))



# Nomor 2
# a. total_elemen_daun()
# total_elemen_daun: PohonBiner --> integer
# total_elemen_daun(P) {menghitung banyanknya jumlah daun yang ada pada pohon biner}

# Realisasi
def IsTreeEmpty(P):
    if P == [None, None, None] or P == None:
        return True
    else:
        return False

def is_biner(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(left(P)) and not IsTreeEmpty(right(P)):
        return True
    else:
        return False

def is_uner_left(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(left(P)) and IsTreeEmpty(right(P)):
        return True
    else:
        return False

def is_uner_right(P): 
    if not IsTreeEmpty(P) and IsTreeEmpty(left(P)) and not IsTreeEmpty(right(P)):
        return True
    else:
        return False

def is_one_element(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(left(P)) and IsTreeEmpty(right(P)):
        return True
    else:
        return False

def akar(P):
    return P[0]

def left(P):
    return P[1]

def right(P):
    return P[2]

def makePB(root, left, right):
    return [root, left, right]

def NbDaun(P):
    if is_one_element(P):
        return 1
    else:  
        if is_biner(P):
            return NbDaun(left(P)) + NbDaun(right(P))
        elif is_uner_left(P):
            return NbDaun(left(P))
        elif is_uner_right(P):
            return NbDaun(right(P))

def total_elemen_daun(P):
    if is_one_element(P):
        return akar(P)
    elif is_biner(P):
        return total_elemen_daun(left(P)) + total_elemen_daun(right(P))
    elif is_uner_right(P):
        return total_elemen_daun(right(P))
    elif is_uner_left(P):
        return total_elemen_daun(left(P))

# Aplikasi
P1 = makePB(8,makePB(3,makePB(1,None,None),makePB(6,makePB(4,None,None),makePB(7,None,None))),makePB(10,None,makePB(14,makePB(13,None,None),None)))
print(total_elemen_daun(P1)) 
        
# b. total_elemen_node
# total_elemen_node: PohonBiner --> integer
# total_elemen_node(P) {menghitung jumlah semua elemen yang ada pada pohon biner}
# Realisasi
def total_elemen_node(P):
    if is_one_element(P):
        return akar(P)
    elif is_biner(P):
        return total_elemen_node(left(P)) + akar(P) + total_elemen_node(right(P))
    elif is_uner_left(P):
        return total_elemen_node(left(P)) + akar(P)
    elif is_uner_right(P):
        return total_elemen_node(right(P)) + akar(P)
    
# Aplikasi
P1 = makePB(8,makePB(3,makePB(1,None,None),makePB(6,makePB(4,None,None),makePB(7,None,None))),makePB(10,None,makePB(14,makePB(13,None,None),None)))
print(total_elemen_node(P1)) 

'''
c. Tuliskan unjungan secara Pre-Order, In-Order, dan Post-Order dari Pohon Biner P di atas:
    Pre-Order  =[8,3,1,6,4,7,10,14,13]
    In-Order   =[1,3,4,6,7,8,13,14,10]
    Post-Order =[1,4,7,6,3,13,14,10,8]
'''

# Nomor 3
# a.
# Definisi dan Spesifikasi
# Filter_list: list --> list
# Filter_list(L) {menentukan ganjil atau genap dengan memfilter elemen list L}

# Realisasi
def is_empty(L):
    return L == []

def first_elmt(L):
    return L[0]

def tail(L):
    return L[1:]

def konso(E, L):
    return [E] + L

def Filter_List(L,f):
    if is_empty(L):
        return[]
    if not (f(first_elmt(L))):
        return Filter_List(tail(L),f)
    else:
        return konso(first_elmt(L),Filter_List(tail(L),f))


# is_genap: integer --> boolean
# is_genap(x) {bernilai true jika integer tersebut bernilai genap}
#Realisasi
def is_genap(x):
    if x % 2 == 0:
        return True
    else:
        return False

# Aplikasi
L1 = [1,4,5,10,15,17,30]
print('==a. nomor 3==')
print(Filter_List(L1,is_genap))

# is_ganjil: integer --> boolean
# is_ganjil(L) {bernilai true jika integer tersebut bernilai ganjil}
# Realisasi
def is_ganjil(x):
    if x % 2 != 0:
        return True
    else:
        return False

# Aplikasi
L1 = [1,4,5,10,15,17,30]
print(Filter_List(L1,is_ganjil))

# b.
# Ekspresi lambda yang digunakan untuk menghasilkan L2 dan L3
# L2 = filter_list(L1, lambda x : x%2 == 0)
# L3 = filter_list(L1, lambda x : x%2 !=0)

print('==b. nomor 3==')
print(Filter_List(L1,lambda x:x % 2 ==0))
print(Filter_List(L1,lambda x:x % 2 !=0))

# No.4
# Definisi dan Spesifikasi
# is_member: elemen, list --> boolean
# is_member(x,L) {bernilai true jika x adalah elemen dari list L}

# Realisasi
def IsEmpty(L):
    return L == []

def FirstElmt(L):
    return L[0]

def Tail(L):
    return L[1:]

def is_member(x,L):
    if(IsEmpty(L)):
        return False
    else:
        if(FirstElmt(L) == x):
            return True
        else:
            return is_member(x, Tail(L))
        
# is_sub_set: 2 list --> boolean
# is_sub_set(H1,H2) {bernilai True jika semua elemen H1 adalah elemen H2}
# Realisasi
def is_sub_set(H1,H2):
    if IsEmpty(H1):
        return True
    elif not is_member(FirstElmt(H1), H2):
        return False
    else:
        return is_sub_set(Tail(H1), H2)

# Minus(H1,H2) {menghitung selisih dari 2 himpunan A dan B}
# Realisasi
def Konso(E, L):
    return [E] + L

def Minus(H1,H2):
    if is_sub_set(H1,H2):
        return []
    elif is_member(FirstElmt(H1),H2):
        return Minus(Tail(H1),H2)
    else :
        return Konso(FirstElmt(H1),Minus(Tail(H1),H2))

# Aplikasi
A=[5,7,9,11,17,21,27]
B=[2,11,21,22]
print('==nomor 4==')
print(Minus(A,B))


