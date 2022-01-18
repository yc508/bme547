TC_value = input("Enter your Total Cholesterol value: ")

TCV = int(TC_value)

if TCV < 200:
    print("Your Total Cholesterol value is normal.")
elif 200 <= TCV <= 239:
    print("Your Total Cholesterol value is borderline high.")
else:
    print("Your Total Cholesterol value is very high.")
