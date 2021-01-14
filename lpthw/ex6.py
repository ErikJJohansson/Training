
# variable assignment
types_of_people = 10

# f string assignment
x = f"There are {types_of_people} types of people"

# variable string declaration
binary = "binary"
do_not = "don't"

# f string declaration
y = f"Those who know {binary} and those who {do_not}."

# print the f strings
print(x)
print(y)

# print f strings with inline variables
print(f"I said: {x}")
print(f"I also said: '{y}'")


# boolean variable assignment
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# add in boolean evaluation
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# print concatenated string
print(w + e)