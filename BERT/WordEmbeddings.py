import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input data file')
args = parser.parse_args()


def read_file(input_file):
    comments = []

    with open(input_file, mode='r', encoding='utf-8') as file:
        csvfile = csv.reader(file)

        # Skip the heading lines
        for x in range(4):
            next(file)

        for row in csvfile:
            print(row[1])
            comments.append(row[1])

    return comments


if __name__ == '__main__':
    raw_comments = read_file(args.input_file)

