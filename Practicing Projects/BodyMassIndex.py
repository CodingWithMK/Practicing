#BODY MASS INDEX CALCULATOR

kişi_ad = input("Adınızı giriniz: ")
kişi_soyad = input("Soyadınızı giriniz: ")
kişi_yaş = str(input("Yaşınızı giriniz: "))
kişi_boy = float(input("Boyunuzu giriniz: "))
kişi_kilo = float(input("Ağırlığınızı giriniz: "))

BMI = (kişi_kilo/kişi_boy**2)

print(kişi_ad, kişi_soyad, "/", kişi_yaş)

if BMI < 18.5:
    print("Your BMI is",(BMI),".", "You are underweight! You have to eat more, otherwise it can be dangerous for you.")
elif BMI > 18.5 and BMI <= 24.9:
    print("Your BMI is",(BMI),".", "You are in normal body condition. That is great!")
elif BMI > 25 and BMI <= 29.9:
    print("Your BMI is",(BMI),".", "You are overweight. Do more sports or make a mealplan.")
elif BMI > 30 and BMI <= 34.9:
    print("Your BMI is"(BMI),".", "You are obese. You have to be careful! Eat less and do more sports.")
else:
    print("Your BMI is",(BMI),".", "You are extremely obese. You must eat more less than obese people and must do sports for hours, otherwise it will be very dangerous for your health!")
