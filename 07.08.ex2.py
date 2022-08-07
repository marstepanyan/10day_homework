given_txt_file = open("p022_names.txt", "rt+")
new_names_file = open("new_names.txt", "rt+")
new_names_file.write(given_txt_file.read().title())
