def main():
    expenses_list = [121.55, 73.86, 13.75, 135.40, 461.23, 32.05, 61.09]
    sum_expense = sum(expenses_list)
    average_expense = sum_expense / len(expenses_list)
    min_expense = min(expenses_list)
    max_expense = max(expenses_list)
    expenses_tuple = (sum_expense, min_expense, max_expense)
    print(expenses_tuple)


if __name__ == "__main__":
    main()
