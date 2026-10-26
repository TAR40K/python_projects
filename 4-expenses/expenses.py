def main():
    string_sum = str(input().lower().strip())
    el_of_string = string_sum.split()
    RUB_WORDS = {"руб", "рубль", "рубля", "рублей"}
    KOP_WORDS = {"коп", "копейка", "копейки", "копеек"}
    if len(el_of_string) == 4:
        num_rub, txt_rub, num_kop, txt_kop = el_of_string
        if not txt_rub in RUB_WORDS or not txt_kop in KOP_WORDS:
            print("Некорректный формат суммы")
        else:
            try:
                int(num_rub)
                int(num_kop)
            except ValueError:
                print("Некорректный формат суммы")
            else:
                num_rub = int(num_rub)
                num_kop = int(num_kop)
                if num_kop > 99:
                    print("Некорректный формат суммы")
                else:
                    print(f"{num_rub}.{num_kop:02d} ₽")
    elif len(el_of_string) == 2:
        num_rub, txt_rub = el_of_string
        if not txt_rub in RUB_WORDS:
            print("Некорректный формат суммы")
        else:
            try:
                int(num_rub)
            except ValueError:
                print("Некорректный формат суммы")
            else:
                num_rub = int(num_rub)
                print(f"{num_rub}.{0:02d} ₽")
    else:
        print("Некорректный формат суммы")


if __name__ == "__main__":
    main()
