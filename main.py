def calculate_profit(skin_price, platform_fee, steam):
    # Рассчитываем цену с учетом площадки

    total_price = skin_price * (100 + platform_fee) / 100

    # Рассчитываем прибыль при продаже на Steam
    steam_price = steam * (1 - 13.042 / 100)  # 13,042% комиссия Steam

    profit = steam_price - total_price

    return profit, total_price, steam_price

def main():
    # Вводим данные от пользователя
    skin_price = float(input("Введите цену скина на площадке: "))
    platform_fee = float(input("Введите процент площадки: "))
    steam = float(input("Введите стоимость скина на Steam: "))

    # Вычисляем прибыль
    profit = calculate_profit(skin_price, platform_fee, steam)

    # Выводим результат
    print("Потенциальная прибыль при продаже на Steam:", round(profit))


if __name__ == "__main__":
    main()
