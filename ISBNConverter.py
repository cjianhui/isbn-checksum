import os
import argparse


'''
    ISBNConverter is a terminal app that takes in a product ID and returns a a standard ISBN-10 number.
    The input can either be a single product ID or a file containing a list of product IDs.
'''

def convertToISBN(productID):




def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')

    print("\t**********************************************")
    print("\t***  ISBN Converter!  ***")
    print("\t**********************************************")


def get_user_choice():
    # Let users know what they can do.
    parser = argparse.ArgumentParser(description='Convert Product ID(s) to ISBN')
    parser.add_argument('pid', help='Product ID to convert')
    parser.add_argument('--file', "-f", dest="filename",
                    help="input file containing product IDs")
    args = parser.parse_args()
    return args


def load_file(fname):
    if os.path.isfile(fname):
        with open(fname) as f:
            content = f.readlines()
            content = [id.strip() for id in content]
        return content

    else:
        print("Please enter a valid filename.")


if __name__ == "__main__":
    display_title_bar()
    args = get_user_choice()
    if args.filename:
        productIDs = load_file(args.filename)
        for id in productIDs:
            convertToISBN(id)
        else:
            convertToISBN(args.pid)

