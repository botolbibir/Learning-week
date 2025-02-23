def menentukan_tujuan():
    print("Menentukan tujuan")

def mengumpulkan_data():
    print("Mengumpulkan data")

def augmentasi_data_set():
    print("Augmentasi data set")

def anotasi_data_set():
    print("Anotasi data set")

def persiapan_memproses_data():
    print("Persiapan memproses data")

def input_data_ke_model():
    print("Input data ke Model")

def melatih_model():
    print("Melatih model")

def evaluasi_model():
    print("Evaluasi model")

def penerapan_model():
    print("Penerapan model")

def main():
    menentukan_tujuan()
    mengumpulkan_data()
    augmentasi_data_set()
    
    augmentasi_data = int(input("Masukkan jumlah data untuk augmentasi: "))
    
    anotasi_data_set()
    persiapan_memproses_data()
    input_data_ke_model()
    
    model = input("Masukkan kualitas model (Good/Bad): ")
    while model == "bad":
        print("Model masih buruk, lakukan prosesing ulang")
        model = input("Apakah model sudah membaik? (Good/Bad): ")
    
    if model == "good":
        melatih_model()
        evaluasi_model()
        penerapan_model()

    else: print("Perintah tidak sesuai")
main()