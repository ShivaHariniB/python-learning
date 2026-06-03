# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and they have keys and values.

# Create a dictionary
data = {1: "one", 2: "two", 3: "three"}
# Create a dictionary with mixed keys and values
mixed = {"name": "Alice", "age": 30, "is_student": False}
print(mixed)

# Accessing dictionary items using keys
print(data[1])  # prints "one"

print(data(4))  # if index is not found, it raises a KeyError
print(data.get(4))  # if index is not found, it returns None
# if index is not found, it returns "Not Found"
print(data.get(4, "Not Found"))

# ------------------------------------------Merge two lists-------------------------------
keys = ["Aishu", "Karthika", "Sowmiya"]
values = ["Zyan", "Inba", "Hridhaan"]

# using zip() to merge two lists into a dictionary
merged_dict = dict(zip(keys, values))

# adding a new key-value pair to the dictionary
merged_dict["Abi"] = "baby"

# ------------------------------------------Lists, Dictionaries inside values of Dictionary-------------------------------
programming_languages = {
    "JS": "VS Code",
    "Python": ["PyCharm", "VS Code"],  # list inside a dictionary value
    # dictionary inside a dictionary value
    "Java": {"IDE": "Eclipse", "Version": "11"}
}

print(programming_languages["JS"])  # prints "VS Code"
print(programming_languages["Python"])  # prints ["PyCharm", "VS Code"]
print(programming_languages["Python"][1])  # prints "VS Code"
print(programming_languages["Java"]["Version"])  # prints "11"
