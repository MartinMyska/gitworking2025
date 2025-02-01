
def print_ascii_mouse():
    with open("mouse.txt") as f:
        for line in f.readlines():
            print(line)

def main():
    print_ascii_mouse()

main()
