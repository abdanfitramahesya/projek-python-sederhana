#Nama = ABDAN FITRA MAHESYA
#NIM  = 2010031802013

tm = int(input("Total Menginap = "))
if (tm > 3):
    tb = (tm - 1) * 500000
else:
    tb = tm * 500000

print ("Total Pembayaran",tb)