from datetime import datetime

user_input = input("Enter your goal - date in netx format ' dd/mm/yy \n")
user_input = user_input.split("-")

goal = user_input[0]
end_date = user_input[1]

end_date = datetime.strptime(end_date, "%d/%m/%y")
current_date = datetime.today()

delta = end_date - current_date

print(f"You still have {delta.days} days to go till your {goal}")