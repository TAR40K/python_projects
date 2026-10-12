coast = float(input("Какая цена на товар? "))
discount = float(input("Какая скидка на товар? "))
discount_size = float((coast * discount) / 100)

print(f"Цена за товар со скидкой: {coast - discount_size}")