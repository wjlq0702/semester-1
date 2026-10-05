# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["York"] = "Ouse"
rivers["Dewsbury"] = "Calder"
print(rivers)
# Display all the keys
keys = rivers.keys()
print(keys)
# Display all the values
value = rivers.values()
print(value)
# Display all the key:value pairs, as tuples
data_tuple = rivers.items()
print(data_tuple)
# Delete an entry from the rivers database
rivers.pop("York")
print(rivers)