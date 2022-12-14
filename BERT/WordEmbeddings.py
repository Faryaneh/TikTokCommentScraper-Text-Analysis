import argparse
import csv
from transformers import BertTokenizer

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


def tokenize_text(sentences):
    tokenized = []
    indexed = []

    for sentence in sentences:
        marked_text = "[CLS] " + sentence + " [SEP]"

        tokenized_text = tokenizer.tokenize(marked_text)
        tokenized.append(tokenized_text)

        indexed.append(tokenizer.convert_tokens_to_ids(tokenized_text))

    return tokenized, indexed


if __name__ == '__main__':
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    raw_comments = read_file(args.input_file)

    tokenized_texts, indexed_texts = tokenize_text(raw_comments)

