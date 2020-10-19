#input
kode = int(input("kode barang ="))
nama = input("nama barang =")
harga = int(input("harga satuan ="))
jumlah = int(input("jumlah barang ="))

#proses
total = harga * jumlah
potongan = 0.10 * total
tb = total - potongan

#output
print("total harga =",total)
print("potongan harga =",potongan)
print("total bayar =",tb)