str_input = input("Input your string: ")
result_str = ""
vovwles= "aeiouAEIOU"
for char in str_input:
    upper_char = char.upper()
    if upper_char in vovwles:
        result_str += "*"
    else:
        result_str += char 
print("Modified string:", result_str)         

