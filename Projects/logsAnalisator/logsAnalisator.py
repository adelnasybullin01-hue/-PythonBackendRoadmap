
filename = "server.log"

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print(f"File {filename} not found")

else:

    def massage_quanity():
        info_quanity = 0
        warning_quanity = 0
        error_quanity = 0
        content_line = list(content.split("\n"))
        for line in content_line:
            new_line = line.strip() 
            if new_line == "":
                continue
            words = line.split()
            if words[0] == "INFO":
                info_quanity = info_quanity + 1
            if words[0] == "WARNING":
                warning_quanity = warning_quanity + 1
            if words[0] == "ERROR":
                error_quanity = error_quanity + 1
        print()
        print(f"INFO: {info_quanity}")
        print(f"WARNING: {warning_quanity}")
        print(f"ERROR: {error_quanity}")
        print()

    def find_the_most_frequnt_message():
        massages = {}
        content_line = list(content.split("\n"))
        for line in content_line:
            new_line = line.strip() 
            if new_line == "":
                continue
            only_massage = line.split(None, 1)[1]
            if only_massage not in massages:
                massages[only_massage] = 1
            else:
                massages[only_massage] = massages[only_massage] + 1
        quanity = 0
        the_most_frequnt_message = "" 
        for massage in massages:
            if massages[massage] > quanity:
                quanity = massages[massage]
                the_most_frequnt_message = massage
        print("Самое частое сообщение: ")
        print(f'"{the_most_frequnt_message}": {quanity}')

    def all_errors():
        print()
        content_line = list(content.split("\n"))
        for line in content_line:
            new_line = line.strip() 
            if new_line == "":
                continue
            word = line.split()
            if word[0] == "ERROR":
                print(line)
        print()

    massage_quanity()
    find_the_most_frequnt_message()
    all_errors()