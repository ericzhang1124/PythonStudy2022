# coding:utf-8

calculation_to_units = 24
name_of_unit = "hours"


def validate_and_execute():
    """
    验证数据合法性，当合法时调用计算方法，不合法时友好提示用户输入合法值
    :return:
    """
    try:
        num_of_days = int(num_of_days_element)
        if num_of_days > 0:
            days_to_unit(num_of_days)
        elif num_of_days == 0:
            print("you enter 0, please input number bigger than 0")
        else:
            print("you enter a negative number, please input a positive number")
    except ValueError as value_error:
        print(value_error.args)
        print("please input validate number(you input a text or float type data), and this number must be integar "
              "type~!")


def days_to_unit(days_num: int):
    """
    计算并打印计算结果
    :param days_num: 天数
    :return:
    """
    print(f"{user_input} days are {days_num * calculation_to_units} {name_of_unit} ")


if __name__ == '__main__':
    user_input = None
    # while user_input != "exit":
    #     user_input = input("Please input days(use 'exit' keyword eixt program):")
    #     for num_of_days_element in user_input.split(","):
    #         validate_and_execute()

    users = ["trentzhang", "ericyang", "ponyma", "trentzhang"]
    print(users)
    users_set = set(users)
    print(users_set)

    my_set = {'hello', 'kitty', 'is', 'kawayi', 'is'}
    print(my_set)