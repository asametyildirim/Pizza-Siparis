import csv

class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
        
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    

class Klasik(Pizza):
    def __init__(self):
        description = """Eğer klasik bir pizza hayranıysanız, doğru yerdesiniz! Çünkü bizim pizzalarımız tam da istediğiniz gibi. Taze malzemeler, lezzetli soslar ve ince hamurlarla hazırlanan pizzalarımız, her ısırığınızda damaklarınızda bir şölen yaşatacak.
Sadece basit malzemelerle yapılan klasik pizzalarımız, yine de her zaman tatmin edici bir lezzet sunar. Mozarella peyniri, domates sosu ve harika baharatlarla hazırlanan pizzalarımızın tadına bakınca, basit olmanın ne kadar lezzetli olabileceğini anlayacaksınız.
Ayrıca, bizim pizzalarımızı yemek, her zaman keyifli bir deneyimdir. Arkadaşlarınızla birlikte oturup, paylaşım yaparak pizzalarımızın tadını çıkarabilirsiniz. Belki de pizzalarımızın tadı size unutulmaz anılar kazandıracaktır."""
        cost = 40
        super().__init__(description, cost)
        
class Margarita(Pizza):
    def __init__(self):
        description = """Margarita Pizza, klasik pizzaların en sevilenlerinden biridir. İnce hamurun üzerine mozarella peyniri, taze domates ve fesleğen yaprakları ile hazırlanır. Margarita Pizza'nın enfes lezzeti, özenle seçilen malzemelerle birleşerek ortaya çıkar.
Bizim Margarita Pizzamız, lezzeti ile sizi büyüleyecek. İnce hamuru, taze domates sosu, mozarella peyniri ve fesleğenin mükemmel uyumu, her ısırıkta ağızda müthiş bir tat bırakır. Üstelik pizzamızı sipariş ederken, isteğinize göre ekstra malzemeler de ekleyebilirsiniz."""
        cost = 40
        super().__init__(description, cost)
        
class TurkPizza(Pizza):
    def __init__(self):
        description = """ürk Pizza'sı, pizza tutkunlarının Türk mutfağına olan ilgisini yansıtan bir lezzet harikasıdır. İnce hamurun üzerine döner eti, taze domates, biber, soğan, sarımsak ve yoğurt sosu ile hazırlanır. Türk Pizza'sı, enfes lezzeti ile damaklarda unutulmaz bir tat bırakır.
Bizim Türk Pizza'mız, özenle seçilen malzemelerle hazırlanır. İnce hamurumuzun üzerine döner eti, taze sebzeler ve baharatlar eklenerek hazırlanan pizza, fırından çıktığında mükemmel bir aroma yaymaktadır.
Türk Pizza'sı, özellikle Türk mutfağına ilgi duyanların favori lezzetlerinden biridir. Yoğurt sosunun hafifliği, sebzelerin tazeliği ve döner etinin lezzeti, her ısırıkta ağızda muhteşem bir uyum sağlar."""
        cost = 40
        super().__init__(description, cost)
        
class SadePizza(Pizza):
    def __init__(self):
        description = """Sade Pizza, klasik ve en sevilen pizza çeşitlerinden biridir. İnce hamurun üzerine taze domates sosu ve mozarella peyniri ile hazırlanır. Bu basit ama lezzetli malzemelerin birleşimi, mükemmel bir pizza deneyimi sunar.
Bizim Sade Pizza'mız, özenle seçilen malzemelerle hazırlanır. İnce hamurumuz, taze domates sosumuz ve mozarella peynirimiz, lezzetlerini birleştirerek ağızda müthiş bir tat bırakır.
Sade Pizza, en sevilen pizza çeşitlerinden biri olmasının yanı sıra, kolay ve hızlı bir şekilde hazırlanması sebebiyle de tercih edilmektedir. İster tek başınıza, ister arkadaşlarınızla, Sade Pizza'nın lezzeti sizi büyüleyecek."""
        cost = 40
        super().__init__(description, cost)

class Decorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.pizza.get_description() + ', ' + Pizza.get_description(self)

class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin sosu, zeytinlerin eşsiz lezzetini pizzanıza taşıyan harika bir sos çeşididir. İnce doğranmış siyah veya yeşil zeytinler, özel bir sos ile karıştırılarak hazırlanan zeytin sosu, pizzanıza zengin bir aroma ve lezzet katmaktadır."
        self.cost = 5

    def get_description(self):
        return f"{self.pizza.get_description()}, {self.description}"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Mantarlar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantar, pizza yapımında sıkça kulllanıan malzemelerden biridir ve lezzetiyle pizzaya ayrı bir boyut kazandırır. Taze mantarların ince dilimleri, pizzanızın üzerinde sıcakken çıtır çıtır bir lezzet sunar. Mantarın lezzetini arttırmak isterseniz, keçi peyniri gibi yoğun bir lezzete sahip peynirlerle birleştirebilirsiniz."
        self.cost = 5 

    def get_description(self):
        return f"{self.pizza.get_description()}, {self.description}"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keçi peyniri, pizza severlerin favori peynirlerinden biridir. Yoğun, kremsi ve keskin bir tadı olan keçi peyniri, pizzanın lezzetini tamamlamak için harika bir seçenektir. İnce dilimlenmiş keçi peyniri, pizzanın üstünde eridikçe, yoğun aroması ile pizzanızı benzersiz bir lezzete dönüştürür."
        self.cost = 5

    def get_description(self):
        return f"{self.pizza.get_description()}, {self.description}"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost


class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et, pizzalarda genellikle jambon, sosis veya biftek olarak kullanılır. Taze ve ince dilimlenmiş et, pizzanın lezzetini tamamlayarak, pizzanızın daha da doyurucu olmasını sağlar."
        self.cost = 5

    def get_description(self):
        return f"{self.pizza.get_description()}, {self.description}"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Soğan, tatlı aroması ve çıtır çıtır dokusu ile pizzaya harika bir lezzet katmaktadır. Dilimlenmiş soğanlar, pizzanın üzerinde eridikçe, tatlı aroması pizzanızı daha da lezzetli hale getirir."
        self.cost = 5

    def get_description(self):
        return f"{self.pizza.get_description()}, {self.description}"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost


class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Misir"
        self.cost = 5

    def get_description(self):
        return f"{self.pizza.get_description()}, {self.description}"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost



def main():
    # Menüyü yazdır
    with open('Menu.txt', 'r') as file:
      print(file.read())
    
    # Kullanıcıdan pizza seçimini al
    pizza_choice = input("Lütfen pizza seçiminizi yapınız (1-4) (Her pizza 40tl) : ")
    
    # Seçilen pizzayı oluştur
    if pizza_choice == "1":
        pizza = Klasik()
    elif pizza_choice == "2":
        pizza = Margarita()
    elif pizza_choice == "3":
        pizza = TurkPizza()
    elif pizza_choice == "4":
        pizza = SadePizza()
    else:
        print("Geçersiz pizza seçimi!")
        return
    
    # Sos seçimini al
    sos_choice = input("Lütfen sos seçiminizi yapınız (11-16) (Her sos 5tl): ")
    
    # Seçilen sostan pizzayı oluştur
    if sos_choice == "11":
        pizza = Zeytin(pizza)
    elif sos_choice == "12":
        pizza = Mantarlar(pizza)
    elif sos_choice == "13":
        pizza = KeciPeyniri(pizza)
    elif sos_choice == "14":
        pizza = Et(pizza)
    elif sos_choice == "15":
        pizza = Sogan(pizza)
    elif sos_choice == "16":
        pizza = Misir(pizza)
    else:
        print("Geçersiz sos seçimi!")
        return
    
    # Toplam fiyatı hesapla
    total_cost = pizza.get_cost()
    print("Toplam fiyat: ", total_cost)
    
    # Kullanıcı bilgilerini al
    name = input("İsim: ")
    tc = input("TC Kimlik Numarası: ")
    cc_number = input("Kredi Kartı Numarası: ")
    cc_cvv = input("Kredi Kartı CVV: ")
    
    # Siparişi veritabanına kaydet
    with open('Orders_Database.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, tc, cc_number, pizza.get_description(), total_cost, cc_cvv])
    print("Sipariş başarıyla kaydedildi!")
    
if __name__ == '__main__':
    main()