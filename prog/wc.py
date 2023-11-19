import sys
import argparse
import re

def count_lines(text):
    # Use regular expressions to count lines
    return len(re.findall(r'.+', text))

def count_words(text):
    # Use regular expressions to count words
    return len(re.findall(r'\w+', text))

def count_characters(text):
    # The character count is a direct count of string length
    return len(text)

def wc(text, count_lines_flag, count_words_flag, count_characters_flag):
    num_lines = count_lines(text) if count_lines_flag else ""
    num_words = count_words(text) if count_words_flag else ""
    num_characters = count_characters(text) if count_characters_flag else ""
    
    return num_lines, num_words, num_characters

def main():
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='A Python implementation of the wc utility.')
    
    # Add arguments to the parser
    parser.add_argument('files', nargs='*', type=argparse.FileType('r'), default=[sys.stdin],
                        help='File(s) to read from. If omitted or "-", will read from STDIN.')
    parser.add_argument('-l', '--lines', action='store_true', help='Count the number of lines')
    parser.add_argument('-w', '--words', action='store_true', help='Count the number of words')
    parser.add_argument('-c', '--characters', action='store_true', help='Count the number of characters')

    # Parse the arguments
    args = parser.parse_args()

    # Determine which counts to perform
    count_lines_flag = args.lines or (not args.words and not args.characters)
    count_words_flag = args.words or (not args.lines and not args.characters)
    count_characters_flag = args.characters or (not args.lines and not args.words)

    # Process the files
    total_lines, total_words, total_characters = 0, 0, 0
    for file in args.files:
        text = file.read()
        counts = wc(text, count_lines_flag, count_words_flag, count_characters_flag)
        total_lines += counts[0] if counts[0] != "" else 0
        total_words += counts[1] if counts[1] != "" else 0
        total_characters += counts[2] if counts[2] != "" else 0
        
        output = [str(count) for count in counts if count != ""]
        print(f"{' '.join(output)} {file.name if file.name != '<stdin>' else ''}")
    
    # If more than one file, print the totals
    if len(args.files) > 1:
        total_output = [str(total) for total in (total_lines, total_words, total_characters) if total != ""]
        print(f"{' '.join(total_output)} total")

if __name__ == '__main__':
    main()
