from prettytable import PrettyTable
mm = []
option = True
tambah = "T"
hapus = "H"
lihat = "L"

while option != 0:
    print("(T)ambah, (H)apus, (L)ihat, (U)bah")

    x = PrettyTable()
    i = 0

    pilihan = input("masukan pilihan :")
    if pilihan == "T":
        nama = input("Masukan nama:")
        nim = input("Masukan NIM:")
        tugas = input("Nilai tugas: ")
        uts = input("Nilai UTS: ")
        uas = input("Nilai UAS: ")
        nilai_akhir = 0.3 * float(tugas) + 0.35 * float(uts) + 0.35 * float(uas)
        mm.append([nama, nim, tugas, uts, uas, nilai_akhir])
        
    elif pilihan == "L" :
        for data in mm:
            i +=1
            x.field_names = ["No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir"]
            x.add_row([i, data[0], data[1], data[2], data[3], data[4], data[5]])
            print(x)
    elif pilihan == "H":
        pili = input("Masukan NIM:")
        for i in mm:
            del mm[i]
            print(pili)
            


        

       




