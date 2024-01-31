"""
Convert Numbers
by A01330566

This code extracts the number from a text file
and returns them converted to binary and hexadecimal
base
"""
import sys
import time

def extract_data(file_name):
    """
    this function reads the text file and returns
    the number list extracted from the file
    """
    num_list = []
    try:
        with open(file_name, 'r', encoding="UTF-8") as file:
            for line in file:
                try:
                    num_list.append(float(line.strip()))
                except ValueError:
                    print("Invalid data found in the file:", line.strip())
    except FileNotFoundError:
        print("File not found:", file_name)
        sys.exit(1)
    except UnicodeDecodeError:
        print("Error decoding file. Please ensure the file is UTF-8 encoded.")
        sys.exit(1)

    return num_list

def convert_num(num, base):
    """
    this function converts fractional or full numbers to base 16 or 2
    """
    if base == 2:
        digits = "01"
    elif base == 16:
        digits = "0123456789ABCDEF"
    else:
        print("Invalid base. Please verify")

    sign = ""
    if num < 0:
        sign = "-"
        num = num * -1
    int_part = int(num)
    flt_part = num-int_part
    result = ""

    while int_part > 0:
        result = digits[int_part % base] + result
        int_part //= base

    if flt_part > 0:
        flt_conv = ""
        for _ in range(8):
            flt_part *= base
            flt_conv += digits[int(flt_part)]
            flt_part -= int(flt_part)

        result = result + "." + flt_conv

    return sign + result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py InputFile.txt")
        sys.exit(1)

    start_time = time.time()
    filename = sys.argv[1]
    file_data = extract_data(filename)
    new_file_data = []
    for item in file_data:
        new_file_data.append(f"DEC: {item}")
        new_file_data.append(f"HEX: {convert_num(item, 16)}")
        new_file_data.append(f"BIN: {convert_num(item, 2)}")
        new_file_data.append("="*5)
    elapsed_time = time.time() - start_time
    new_file_data.append(f"Time elapsed:{elapsed_time} seconds")
    with open("ConvertionResults.txt", 'w', encoding="UTF-8") as results_file:
        for new_line in new_file_data:
            print(new_line)
            results_file.write(new_line +"\n")
