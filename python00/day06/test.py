
from Outerfile import Annimal

class Inner:

    def __init__(self):
        print("-------------------")


if __name__ == "__main__":
    annimal = Annimal()
    annimal.inner_method()