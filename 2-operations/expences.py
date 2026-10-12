eat_waste = float(input("Сколько вы потратили на еду? "))
transport_waste = float(input("Сколько вы потратили на поездки? "))
amusement_waste = float(input("Сколько вы потратили на развлечения? "))
sum_waste = eat_waste + transport_waste + amusement_waste
middle_of_sum = sum_waste / 3

print(f"Сумма ваших затрат: {sum_waste}")
print(f"Среднее от ваших затрат: {middle_of_sum:.2f}")