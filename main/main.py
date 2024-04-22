def calculate_profit(skin_price, platform_fee, steam):
    # Рассчитываем цену с учетом площадки
    total_price = skin_price * (100 + platform_fee) / 100

    # Рассчитываем цену скина на Steam с учетом комиссии Steam 13,042% комиссия
    steam_price = steam * (1 - 13.042 / 100)

    # Рассчитываем прибыль
    profit = steam_price - total_price

    return profit

def main():
    # Вводим данные от пользователя
    skin_price = float(input("Введите цену скина на площадке: "))
    platform_fee = float(input("Введите процент площадки: "))
    steam = float(input("Введите стоимость скина на Steam: "))

    # Вычисляем прибыль
    profit = calculate_profit(skin_price, platform_fee, steam)

    # Выводим результат, округленный до ближайшего целого
    print("Потенциальная прибыль при продаже на Steam:", round(profit, 2))

if __name__ == "__main__":
    main()
