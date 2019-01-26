# Student: Josué Ignacio Cabrera Díaz
# Store inputs Exercises

info = input("Enter your data. Ej: (Josué, Cabrera, 63369702, Madrid, 29): ")

personal_info = info.split(",")

name = personal_info[0]
surname = personal_info[1]
telephone = int(personal_info[2])
city = personal_info[3]
age = int(personal_info[4])



print("My name is", name, surname, "I`m living in", city," during this year. I have ", age, "years old and I´m looking for friends. If you wanna chat contact me at:", telephone)
