print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
percentage_tips = input("What percentage tip would you lie to give? 10, 12, or 15? 12: ")
split = input("How many people you want to split the bill?")


tips_percentage =  1 + (float(percentage_tips) / 100)

total_pay = tips_percentage * float(total_bill)
each_person_pay = round(total_pay / float(split), 2)
final_amount = "{:.2f}".format(each_person_pay)

print(f"Each Person should pay: ${final_amount}")
