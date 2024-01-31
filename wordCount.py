"""
Word Count
by A01330566

This program shall identify all distinct words and the frequency of them
"""
import sys
import time
import re

def remove_non_alphanumeric(line):
    """
    This method removes all non alphanumeric values from the line
    """
    return re.sub(r'[^a-zA-Z0-9\s\']', '', line)

def extract_data(file_name):
    """
    this function reads the text file and returns
    the word list extracted from the file
    """
    dic_words = {}
    try:
        with open(file_name, 'r', encoding="UTF-8") as file:
            for line in file:
                clean_line = remove_non_alphanumeric(line.strip())
                line_split = clean_line.strip().split()
                for word in line_split:
                    if word.lower() in dic_words:
                        dic_words[word.lower()] += 1
                    else:
                        dic_words[word.lower()] = 1
    except FileNotFoundError:
        print("File not found:", file_name)
        sys.exit(1)
    except UnicodeDecodeError:
        print("Error decoding file. Please ensure the file is UTF-8 encoded.")
        sys.exit(1)

    return dic_words

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_count.py InputFile.txt")
        sys.exit(1)

    start_time = time.time()
    filename = sys.argv[1]
    file_data = extract_data(filename)
    with open("WordCountResults.txt", 'w', encoding="UTF-8") as results_file:
        for item in file_data.items():
            new_line = f"{item[0]} : {item[1]}"
            print(new_line)
            results_file.write(new_line +"\n")
        elapsed_time = time.time() - start_time
        print(f"Time elapsed:{elapsed_time} seconds")
        results_file.write(f"Time elapsed:{elapsed_time} seconds")
