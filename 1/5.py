
rub = int(input("Введите цену пирожка (рубли): "))
kop = int(input("Введите цену пирожка (копейки): "))
kol = int(input("Введите количество пирожков: "))
total_kop = kop * kol
total_rub = rub * kol + total_kop // 100
total_kop %= 100

print("К оплате: {} руб. {} коп.".format(total_rub, total_kop))