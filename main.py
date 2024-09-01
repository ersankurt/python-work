#  Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight."
text.upper().replace(","," ").replace("."," ").split()

######
#  Verilen liste için aşağıdaki görevleri yapınız.

liste = ["M","Y","W","A","Y",">","D","A","T","A","S","C","I","E","N","C","E"]
#LİSTENİN ELEMAN SAYISI

len(liste)

#5. ve 16. indexteki elemanları

liste[5]
liste[16]

#liste üzerinden ["D","A","T","A"] listesi oluşturun.

new_liste = liste[6:10]
print(new_liste)

#5. indexteki elemanı silin.

liste.pop(5)
liste

# listenin sonuna "Must be work for future" ekleyiniz.

liste.append("Must be work for future")
liste

#5. indexe  "=>" elemanını tekrar ekleyin.

liste.insert(5,"=>")
liste


######
#Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {'Ahmet': ["Karasenir",18],
        'Yunus':["Karahasanli",12],
        'Recep':["Hiziruşagi",22],
        'Veli':["Kanlica",25]}
#Key değerlerine erişiniz.

dict.keys()

#Value'lara erişiniz.

dict.values()

#Veli key'ine ait 25 değerini 19 olarak güncelleyiniz.

dict["Veli"][1] = 19
dict

# key değeri Seçkin value değeri Aydıncık, 23 olan yeni veri ekleyiniz.

dict.update({"Seçkin": ["Aydıncık, 23"]})
dict

# Recep kişisini dict'den siliniz.

dict.pop("Recep")
dict


######
# l isimli liste içindeki değerleri tek ve çift sayıları farklı listelere return olarak döndürünüz.

l = [2,3,7,34,11,97,88,26]

def func(list):
    cift_say= []
    tek_say = []

    for e in list:
        if e % 2 == 0:
            cift_say.append(e)
        else:
            tek_say.append(e)
    return cift_say, tek_say

func(l)

######
# can, cem, maya, sude, mert, fırat isimli öğrencilerin ilk 3 ü yardımcı yönetici son 3 ü asistandır.
#çıktıyı ( x. yardımcı yönetici : can ...  son 3 öğrenciyi y. asistan : sude ... şeklinde enumerate ile değiştirip sıralama yapınız.

ogrenciler = ["CAN","CEM","MAYA","SUDE","MERT","FIRAT"]

for i,x in enumerate(ogrenciler):
    if i<3 :
        i += 1
        print(i,". Yardımcı Yönetici: ",x)
    else:
        i -= 2
        print(i, ". Asistan: ", x)


######
#3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır.
# Zip kullanarak ders bilgilerini bastırınız.


ders_kodu = ["mat103","camy102","geo103","anly203"]
kredi = [3,5,2,7]
kontenjan = [50,70,120,40]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
  print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

######

# A'de olup B'de olmayanlar, B'de olup A'de olmayanlar, İki kümede de birbirlerine göre olmayanlar,
#İki kümenin kesişimi, İki kümenin birleşimi,İki kümenin kesişimi boş mu? Bir küme diğer kümenin alt kümesi mi? Bir küme diğer kümeyi kapsıyor mu?

kume_A= set(["data", "python", "conda", "jupiter"])
kume_B= set(["data", "jenkins", "docker", "flow", "python", "apply", "enumerate"])
#
kume_B - kume_A
kume_A - kume_B
#
kume_A.symmetric_difference(kume_B)
#
kume_B.intersection(kume_A)
#
kume_A.union(kume_B)
#
kume_A.isdisjoint(kume_B)
#
kume_A.issubset(kume_B)
#
kume_B.issuperset(kume_A)
