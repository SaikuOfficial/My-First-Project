balance = int(input("На сколько вы хотите пополнить счет? "))

if balance <= 0:
    print("Вы не пополнили счет.")
elif balance > 0:
    print("Счет успешно пополнен.")

valute = input("Выберите валюту для пополнения (USD, EUR, CNY): ")

if valute == "USD":
    print("Вы выбрали доллары США.")
    print(f"{balance * 75,25} долларов США переведено.")
elif valute == "EUR":
    print("Вы выбрали евро.")
    print(f"{balance * 87,98} евро переведено.")
elif valute == "CNY":
    print("Вы выбрали китайские юани.")
    print(f"{balance * 11,02} китайских юаней переведено.")
else:
    print("Извините, но такая валюта не поддерживается.")