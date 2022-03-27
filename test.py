# coding:utf-8

calculation_to_units = 24
name_of_unit = "hours"


def days_to_unit():
    while True:
        num_of_days = (input("Please input days(use 'exit' keyword eixt program):"))
        if num_of_days.isdigit():
            int_num_of_days = int(num_of_days)
            if int_num_of_days > 0:
                print(f"{int_num_of_days} days are {int_num_of_days * calculation_to_units} {name_of_unit}")

            elif int_num_of_days == 0:
                print("you enter 0, please input number bigger than 0")
            else:
                print("you enter a nagative number, please input number bigger than 0")
        else:
            if num_of_days == 'exit':
                break
            else:
                print("you enter is not a number, please input number~!")
        # try:
        #     num_of_days_int = int(num_of_days)
        # except ValueError:
        #     if num_of_days == 'exit':
        #         break
        #     else:
        #         print("Please input int number and bigger than 0")
        #         break
        #
        # if num_of_days_int > 0:
        # else:
        #     print("Please input number and bigger than 0")


if __name__ == '__main__':
    # days_to_unit()
    is_digit = "10.35".isdigit()
    print(is_digit)