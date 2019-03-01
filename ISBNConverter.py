import os
import argparse


'''
    ISBNConverter is a terminal app that takes in a product ID and returns a a standard ISBN-10 number.
    The input can either be a single product ID or a file containing a list of product IDs.
'''


def convert(pid):
    # remove first 3 digits
    isbn = pid[3:]

    # initialize total sum of weights and weight for initial element is 10
    total_sum = 0
    weight = len(isbn)+1
    for digit in isbn:
        # sum up the weighted digits
        total_sum += (int(digit) * weight)
        # decrement weight by 1 for each digit
        weight -= 1

    # if sum of weights up till the 9th digit is divisible by 11,
    # checksum can only be 0
    if (total_sum % 11) == 0:
        checksum = 0
    else:
        # if not, first obtain the next closest multiple of 11
        new_sum = ((total_sum / 11) + 1) * 11
        # since checksum digit is only weighted by 1, the difference
        # between the next multiple of 11 and the total sum will give us the checksum
        checksum = new_sum - total_sum

    if checksum == 10:
        checksum = "x"

    print(isbn + str(checksum))


def get_user_choice():
    # Let users know what they can do.
    parser = argparse.ArgumentParser(description='Convert Product ID(s) to ISBN')
    gp = parser.add_mutually_exclusive_group(required=True)
    gp.add_argument('pid', nargs='?', help='Product ID to convert')
    gp.add_argument('--file', "-f", dest="filename",
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
    args = get_user_choice()
    if args.filename:
        productIDs = load_file(args.filename)
        for pid in productIDs:
            convert(pid)
    else:
        convert(args.pid)

