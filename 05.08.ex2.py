given_txt_file = open("text.txt", "rt+")
new_txt_file = open("new_text.txt", "rt+")
new_txt_file.write(given_txt_file.read().title())
