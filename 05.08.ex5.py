given_txt_file = open("text.txt", "rt+")
old_text = given_txt_file.read()
new_text = ''

for i in range(len(old_text)):
    if (i + 1) % 3 != 0:
        new_text += old_text[i]

print(new_text)
