#Nama = ABDAN FITRA MAHESYA
#NIM  = 2010031802013

tb = int(input("Total Belanja = "))
yn = input("Puny Kartu Member? Y Untuk Ya Dan N Untuk Tidak = ")
if (yn == "Y"):
    tp = tb - tb * 0.10
else:
    tp = tb
print ("Total Pembayaran Adalah",tp)