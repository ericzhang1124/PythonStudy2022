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
