import datetime
from html import unescape

# user_input = input("enter your goal with a deadline separated by colon\n")
user_input = "StudyPython:2022/12/07"
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%Y/%m/%d")
today_data = datetime.datetime.today()
time_till = deadline_date - today_data

print(type(time_till))
print(f"Dear user! Time remaining for your goal:{goal} is {time_till.days} days!")


def calculate_total_amount(year_salary, year_money , n , mode):
    if mode == "2N":
        return (year_salary + year_money) / 12 * 2 * n
    elif mode == "N+1":
        return (year_salary + year_money) / 12 * (n + 1)



print(f"N + 1 with last year total income get total: {calculate_total_amount(266728, 108830, 4.5, 'N+1')}")
print(f"2N with last year total income get total: {calculate_total_amount(266728, 108830, 4.5, '2N')}")
