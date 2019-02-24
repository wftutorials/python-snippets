

def write_file(content):
    f = open("note.txt", "a+")
    f.write(content)
    f.close()


def open_file():
    f = open("note.txt", "r")
    if f.mode == "r":
        print(f.read())


def get_input():
    content = input("Write Line:?")
    write_file(content.strip() + "\r\n")
    open_file()


def main():
    while True:
        get_input()


if __name__ == "__main__":
    main()