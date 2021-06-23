print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowercase_name = name1 + name2
lower_name = lowercase_name.lower()

add_t = lower_name.count("t")
add_r = lower_name.count("r")
add_u = lower_name.count("u")
add_e = lower_name.count("e")

add_l = lower_name.count("l")
add_o = lower_name.count("o")
add_v = lower_name.count("v")
add_e = lower_name.count("e")

add_true = add_t + add_r + add_u + add_e
add_love = add_l + add_o + add_v + add_e
print("t "+str(add_t))
print("r "+str(add_r))
print("u "+str(add_u))
print("e "+str(add_e))
print("\n")
print("l "+str(add_l))
print("o "+str(add_o))
print("v "+str(add_v))
print("e "+str(add_e))
total = int(str(add_true) + str(add_love))

# print(str(total))

if total < 10 or total > 90:
  print(f"your score is {total}, you go together like coke and mentos.")
elif 40 <= total <= 50:
  print(f"your score is{total}, you are alright together.")
else:
  print(f"you score is {total}")
