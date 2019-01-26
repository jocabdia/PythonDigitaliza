# Student: Josué Ignacio Cabrera Díaz
# Store inputs Exercises

personal_info = (input("Enter your data. Ej: (Josué, Cabrera, 63369702, Madrid, 29): "))

name = personal_info[0]
surname = personal_info[1]
telephone = personal_info[2]
city = personal_info[3]
age = personal_info[4]


print("My name is", name + " " + surname, "I`m living in", city +" during this year. I have " + age, "years old and I´m looking for friends. If you wanna chat contact me at: " + telephone)
