a_list = ["a", "", "c"]
without_empty_strings = []
for string in a_list:
    if (string != ""):
        without_empty_strings.append(string)

print(without_empty_strings);

######
## Use a list comprehension for a more compact solution.
a_list = ["a", "", "c"]
without_empty_strings = [string for string in a_list if string != ""]
print(without_empty_strings)

#######
a_list = ["a", "", "c"]
filter_object = filter(lambda x: x != "", a_list)
without_empty_strings = list(filter_object)
print(without_empty_strings)
