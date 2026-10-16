menu = input("Выберите категорию блюда (напиток, суп или десерт): ").lower().strip()


def main():
    match menu:
        case "напиток":
            drink = input("Чай, кофе, сок? ").lower().strip()
            match drink:
                case "чай":
                    print("10 рублей")
                case "кофе":
                    print("15 рублей")
                case "сок":
                    print("13 рублей")
                case _:
                    print("Такого напитка нет в меню")
        case "суп":
            soup = input("Борщ, щи, суп-пюре? ").lower().strip()
            match soup:
                case "борщ":
                    print("55 рублей")
                case "щи":
                    print("45 рублей")
                case "суп-пюре":
                    print("75 рублей")
                case _:
                    print("Такого супа нет в меню")
        case "десерт":
            dessert = input("Торт, мороженое, фрукты? ").lower().strip()
            match dessert:
                case "торт":
                    print("100 рублей")
                case "мороженое":
                    print("95 рублей")
                case "фрукты":
                    print("55 рублей")
                case _:
                    print("Такого десерта нет в меню")
        case _:
            print("Такой категории блюда нет в меню")


if __name__ == "__main__":
    main()
