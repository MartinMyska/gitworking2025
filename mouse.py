
def print_ascii_mouse():
    import pdb
    pdb.set_trace()
    with open("mouse.txt") as f:
        for line in f.readlines():
            print(line)

def main():
    print_ascii_mouse()

main()
