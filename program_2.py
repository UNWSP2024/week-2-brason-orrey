from statistics import mean

Friend1 = input("Please enter one of your friends names:")
Friend2 = input("Please enter another friends name:")
Friend3 = input("Please enter a different friends name:")
Friend4 = input("Please enter a fourth friends name:")
Friend5 = input("Please enter one more friends name:")

Friend1_age = int(input(f"Please enter {Friend1}'s age:"))
Friend2_age = int(input(f"Please enter {Friend2}'s age:"))
Friend3_age = int(input(f"Please enter {Friend3}'s age:"))
Friend4_age = int(input(f"Please enter {Friend4}'s age:"))
Friend5_age = int(input(f"Please enter {Friend5}'s age:"))

List_Of_Age__For_Friends = (Friend1_age, Friend2_age, Friend3_age, Friend4_age, Friend5_age)

age_average = mean(List_Of_Age__For_Friends)

print("The average age of your friends is:", age_average)
