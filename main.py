
from traceback import print_exc

def main():
    pass

if __name__ == "__main__":
    try:
        main()
    except:
        print_exc()
        raise Exception("Could not execute main!")

