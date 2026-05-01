course = "Python Programming"
print("Prints length: " + str(len(course)))
print("Prints first character: " + course[0])
print("Prints last character: " + course[-1])

# substrings
print("Prints substring: " + course[0:6])
print("substring if 2nd character isnt given: " + course[0:])
print("substring if 1st character isnt given: " + course[:6])

# Escape Sequences
# \"
# \' - single quote
# \\ - backslash
# \n - new line
course_name = "Python \nProgramming"
print(course_name)

# Formatted Strings
first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
print("one way to use formatted strings: " + full_name)
full_name = f"{first_name} {last_name}"
print("another way to use formatted strings: " + full_name)

# String Methods
course = "  python Programming"
print(course.upper())  # prints an new string , doesn't change the original string
print(course)  # prints the original string
print(course.lower())
print(course.title())
# removes leading and trailing whitespace, lstrip() removes only leading whitespace, rstrip() removes only trailing whitespace
print(course.strip())
print(course.replace("p", "j"))
# "find" returns the index of the first occurrence of the substring, -1 if not found
print(course.find("P"))
# "in" returns True if the substring is found in the string, False otherwise
print("pro" in course)
