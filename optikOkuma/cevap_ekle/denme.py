import numpy as np

cevaplar_ogrenci = [[1, 1], [2, 1], [3, 1], [4, 8], [5, 8], [6, 4], [7, 4], [8, 3], [9, 3], [10, 7], [11, 7], [12, 10], [13, 10], [14, 8], [15, 8], 
[16, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8]]

# np.array(cevaplar_ogrenci)


sözlük= {
    "0": "None", 
    "1": "0", 
    "2": "1",
    "3": "2",
    "4": "3", 
    "5": "4",
    "6": "5", 
    "7": "6", 
    "8": "7", 
    "9": "8", 
    "10": "9"}


for i,j in (cevaplar_ogrenci):
    print(sözlük[j])
    
    # print("çıktı" ,i,j)