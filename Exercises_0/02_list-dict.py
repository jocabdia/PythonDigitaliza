# Student: Josué Ignacio Cabrera Díaz
# List and Dictionary activities

#Create a string list

strings_list = ["Linux Torvalds", "Richard Stallman", "Alan Cox", "Theo de Raadt", 
"Donald Knuth", "Miguel de Icaza", "Keith Packard", "Matthias Ettrich", 
"Ian Murdock", "Andrew Tridgell" ]

print(strings_list)

#Create a integer list

integers_list = [1969, 1953, 1968, 1968, 1938, 1972, 1963, 1972, 1973, 1967]

print(integers_list)

#Create a list containing strings, integer and floats type

mixed_list = ["Sujeto1", 1963, 1.84, "sujeto2", 1984, 1.73, "Sujeto3", 1991, 1.77]

print(mixed_list)

# 3 Sentences for store each last value from the lists

last_string = strings_list[-1]
last_integer = integers_list[-1]
last_mixed = mixed_list[-1]

# Print each variable explaining itself
print
(
  "The last value on the string list is: ", last_string, ".", 
  "The last value on the integer list is: ", last_integer, ".", 
  "The last value on the mixed list is: ", last_mixed, "." 
)

# Making a dictionary for store autor and films

film_Dictionary = {
  "Steven Spielberg":"Jurassic Park",
  "Ridley Scott":"Alien",
  "Neil Blomkamp":"Distrito 9",
  "James Cameron":"Terminator 2", 
  "Ridley Scott":"The Martian"
}

# Print all the dictionary
for x,y in film_Dictionary.items():
  print(x, y)

# Print only autors
for x,y in film_Dictionary.items():
  print(x)

# Print only films
for x,y in film_Dictionary.items():
  print(y)
