import time
from termcolor import colored

# Alıcının telefon numarasını kullanıcıdan isteyin
to_number = input("Lütfen telefon numarasını girin (+90xxxxxxxxxx): ")

# Kaç SMS göndermek istediğini kullanıcıya sorun
num_sms = int(input("Kaç tane SMS göndermek istiyorsunuz?: "))

# Başlık bilgisini ekle
print(colored("Code by:lahhannacı\n", "red"))

# SMS gönderme işlemini gerçekleştirin ve sonucu yazdırın
for i in range(num_sms):
    print(colored("{}. SMS, {} numarasına gönderildi.".format(i+1, to_number), "green"))
    time.sleep(0.1)
