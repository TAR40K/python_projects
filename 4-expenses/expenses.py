def main():
    string_sum = str(input())
    el_of_string = string_sum.split()
    roubles, copeck = el_of_string[0], el_of_string[2]
    try:
        int(roubles)
        int(copeck)
    except ValueError:
        print("Неккоретно введена сумма")
    else:
        if int(copeck) > 99:
            print("Неккоректно введена сумма")
        else:
            list_sum = roubles, copeck
            normal_sum = float(".".join(list_sum))
            print(f"{normal_sum:.2f} ₽")


if __name__ == "__main__":
    main()
