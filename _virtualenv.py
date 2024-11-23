#toplama "+"
#çıkarma "-"
#çarpma "*"
#bölme "/"
#tamsayı bölmesi "//"
#kuvvet alma "**"
#mutlak alma "abs"
#yuvarlama "round"
#işlem önceliği

#karşılaştırma operatörleri
#Eşittir " == "
#Küçüktür " < "
#Büyüktür " > "
#Küçük eşittir " <= "
#büyük eşittir " >= "
#Eşit değildir " ! "

#ÖRN : sayı = "10" dediğimiz zaman tırnak işeterinin arasında bulunduğundan python bunu değer olarak değil metin olarak algılar





sayı1 = 61
sayı2 = 17.5
sayı3 = sayı1 ** 2
sayı4 = sayı3 / sayı2
sayı5 = -16
sayı6 = 32
sayı7 = 3
print(round(sayı6 / sayı7))










print(type(sayı1))
print(type(sayı2))
print(sayı3)
print(sayı4)
print(round(sayı4))
print(sayı5)
print(abs(sayı5))
#
int(50 == 50)
print(sayı1 > sayı2)
print(sayı1 < sayı2)
print(1 >= 3)
print((sayı1 * sayı2) > (sayı3*sayı5))


# #                                              Listeleme
renkler = ["bordo", "mavi", "sarı", "turuncu"]

print(renkler)
print(len(renkler))
print(renkler[0])
print(renkler[3])
print(renkler[2])
print(renkler[1:3])
print(renkler[:3])


# #append listenin sonuna ekleme yapmaya yarar
renkler.append("yeşil")
renkler.append("yeşil")


print(renkler)
# #insert elamanı listenin sonuna değilde aralara eklemek istiyorsak kullanılır
renkler.insert(6,"turkuaz")

print(renkler)
# #remove listeden elemanı silmeye yarar
renkler.remove("sarı")
print(renkler)
# #extend listeye birden fazla eleman eklemeye yarar
renkler2 = ["pembe", "kırmızı"]
renkler.append(renkler2)
print(renkler)
renkler.extend(renkler2)
print(renkler)
# #pop listenin en son elemananını siler
silinen = renkler.pop()
print(renkler)
print(silinen)
# #reverse metodu listeyi tersine döndürür
renkler.reverse()
print(renkler)
# #sort listeyi alfabetik olarak sıralar
renkler.sort()
print(renkler)
# #renkler.sort(reverse=True) alfabetik olarak sondan sırala
# #sorted listeyi sıralamak isteyip listenin bozulmasını istemiyorsam kullanırım
liste = sorted(renkler2)
print(liste)
print(renkler2)

#                                            yeni bölüm
# #min alfabetik ve sayısal değer olarak en küçük olanı yazar
takımlar = ["trabzonspor","bursaspor","kocaelispor","fenerbahçe","galatasaray","beşiktaş"]
sayılar = [61,55,6,34,16,7,103]




print(min(takımlar))
print(min(sayılar))
# #max alfabetik ve sayısal olarak en ilerde olanı yazar
print(max(takımlar))
print(max(sayılar))
#sum toplam fonksiyonu
print(sum(sayılar))
# #for döngüsü ile liste yazdırmak

for takım in takımlar:
 #print(takım)
# #enumarate listeyi numarlanırmaya yarar
print(list(enumerate(takımlar)))
#print(list(enumerate(takımlar,start=7))) numaralandırmıya hangi sayıdan başlayacağına karar vermeni sağlar
# in yazılan değerin o grupta olup olmadığını sorgulamaya yarar
print("bursaspor" in takımlar)
print("denizlispor" in takımlar)
# #listeyi stringe çevirmek için join metodu kullanılır.Join birleştirmek bağlamak anlamına geliyor
stringtakımlar = ",".join(takımlar)
# #stringtakımlar = " ".join(takımlar)"" işaretinin arasında ne kadar bırakırsam veya içine ne koyarsam aralarına o gelir

print(stringtakımlar)
# #stringi listeye çevirmek için split metodu kullanılır
takımlar2= stringtakımlar.split(",")
# #takımlar2= stringtakımlar.split(",") (",") tırnak işaretinin içine girdiğimiz kısım metni nasıl parçalayacğını karar verdiği kısım.
print(takımlar2)

