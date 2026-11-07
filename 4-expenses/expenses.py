def main():
    COMANDS = (
        "добавить расход",
        "показать все расходы",
        "показать сумму и средний расход",
        "удалить расход по номеру",
        "выход",
    )
    menu_input = input(
        "- Добавить расход\n"
        "- Показать всех расходы\n"
        "- Показать сумму и средний расход\n"
        "- Удалить расход по номеру\n"
        "- Выход\n"
    ).lower()

    for comand in COMANDS:
        while menu_input not in COMANDS:
            print("\nВведенная команда отсутствует. Попробуйте еще раз\n")
            menu_input = str(
                input(
                    "- Добавить расход\n"
                    "- Показать всех расходы\n"
                    "- Показать сумму и средний расход\n"
                    "- Удалить расход по номеру\n"
                    "- Выход\n"
                )
            ).lower()
        if comand == "выход":
            print("\nВсего доброго!\n")
            break


if __name__ == "__main__":
    main()

    # string_sum = str(input().lower().strip())
    # el_of_string = string_sum.split()
    # RUB_WORDS = {"руб", "рубль", "рубля", "рублей"}
    # KOP_WORDS = {"коп", "копейка", "копейки", "копеек"}
    # if len(el_of_string) == 4:
    #     num_rub, txt_rub, num_kop, txt_kop = el_of_string
    #     if not txt_rub in RUB_WORDS or not txt_kop in KOP_WORDS:
    #         print("Некорректный формат суммы")
    #     else:
    #         try:
    #             int(num_rub)
    #             int(num_kop)
    #         except ValueError:
    #             print("Некорректный формат суммы")
    #         else:
    #             num_rub = int(num_rub)
    #             num_kop = int(num_kop)
    #             if num_kop > 99:
    #                 print("Некорректный формат суммы")
    #             else:
    #                 print(f"{num_rub}.{num_kop:02d} ₽")
    # elif len(el_of_string) == 2:
    #     num_rub, txt_rub = el_of_string
    #     if not txt_rub in RUB_WORDS:
    #         print("Некорректный формат суммы")
    #     else:
    #         try:
    #             int(num_rub)
    #         except ValueError:
    #             print("Некорректный формат суммы")
    #         else:
    #             num_rub = int(num_rub)
    #             print(f"{num_rub}.{0:02d} ₽")
    # else:
    #     print("Некорректный формат суммы")
