import time

print("Please provide the full path to your .srt file e.g. \"C:\\users\\your_name\\Downloads\\Folder_name\\inputfile.srt\"")
input_file = input("Inputfile: ")

plain_text = []

with open(input_file, "r", encoding="utf-8-sig") as datei1:
    for line in datei1:
       plain_text.append(str(line))


highlighted_words = []
color = "empty"


def getInputs():
    global highlighted_words
    global color
    print("Please list the words that shall be highlighted. Separate the words with a comma.")
    var_A = input("Your words: ")

    if var_A[-1] == (","):
        var_A = var_A[0:-1]

    highlighted_words = var_A.split(",")

    for i in range(0, len(highlighted_words)):
        highlighted_words[i] = highlighted_words[i].strip()

    time.sleep(2)

    var_B = input("Please enter the colorcode for the highlighted words (e.g. #FFF000FF): ")
    time.sleep(2)
    color = var_B

not_found = []
not_together = []

def highlighter(word):
    global not_found
    global not_together
    counter = 0
    for i in range(0, len(plain_text)):
        if word in plain_text[i]:
            plain_text[i] = plain_text[i].replace(word, f"<font color={color}>{word}</font>")
            counter += 1
    if counter == 0 and (not " " in word):
        not_found.append(word)
    elif counter == 0 and (" " in word):
        not_together.append(word)


for element in highlighted_words:
    highlighter(element)

def mainLoop():
    local_yn = "Y"
    while local_yn == "Y" or local_yn == "y":
        getInputs()
        for element in highlighted_words:
            highlighter(element)
        local_yn = input("Do you want to highlight other words in a different color? (Y/N): ")
        time.sleep(2)

mainLoop()

if len(not_found) >= 1:
    print("!ATTENTION! The following words could not be found:" + str(not_found))

if len(not_together) >= 1:
    print("!ATTENTION! The following words are not displayed together and have therefore not been highlighted:" + str(not_together))


#filename = input("Wie soll die fertige Datei heißen? (ohne .srt): ")

time.sleep(2)

#index1 = 1
#for i in range(len(input_file)-1, 0, -1):
#   if input_file[i] == "\\":
#       index1 = i + 1
#       break

#new_path = input_file[0:index1]

new_file = input_file[0:-4] + "_finished" + ".srt"

output_file = open(new_file, "w")

for element in plain_text:
    output_file.write(element)

output_file.close()
print(f"Your new subtitle file has been saved as \"{new_file}\" ")

input("Press any key to quit the program.")
