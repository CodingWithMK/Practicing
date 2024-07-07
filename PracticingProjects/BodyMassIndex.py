#BODY MASS INDEX CALCULATOR

user_name = input("Adinizi giriniz: ")
user_surname = input("Soyadinizi giriniz: ")
user_age = str(input("Yaşinizi giriniz: "))
user_height = float(input("Boyunuzu giriniz: "))
user_weight = float(input("Ağirliğinizi giriniz: "))

BMI = (user_weight/user_height**2)

print(user_name, user_surname, "/", user_age)

if BMI < 18.5:
    print("Your BMI is",(BMI),".", "You are underweight! You have to gain weight, otherwise it can be dangerous for you.")
elif BMI > 18.5 and BMI <= 24.9:
    print("Your BMI is",(BMI),".", "You are in normal body condition. That is great!")
elif BMI > 25 and BMI <= 29.9:
    print("Your BMI is",(BMI),".", "You are overweight. Do more sports or make a mealplan.")
elif BMI > 30 and BMI <= 34.9:
    print("Your BMI is",(BMI),".", "You are obese. You have to be careful! Eat less and do more sports.")
else:
    print("Your BMI is",(BMI),".", "You are extremely obese. You must be very careful! Make a mealplan and do regularly sports for hours, otherwise it will be very dangerous for your health!")
