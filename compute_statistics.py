"""
Compute Statistics
by A01330566

This code extracts the number from a text file
and returns a statistics report showing the
mean, mode, median, std deviation and variance
of the provided number list
"""
import time
import sys

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

def mean_calculator(num_list):
    """
    this function calculates the mean of the provided number list
    """
    if len(num_list) == 0:
        return 0
    return sum(num_list)/len(num_list)

def median_calculator(num_list):
    """
    This function calculates the median of the provided number list
    """
    if len(num_list) == 0:
        return None
    sort_list = sorted(num_list)
    len_list = len(sort_list)
    if len_list % 2 == 0:
        return (sort_list[len_list//2] + sort_list[len_list//2 -1])/2.0
    else:
        return sort_list[len_list//2]

def mode_calculator(num_list):
    """
    this function returns the mode of the provided number list
    """
    if len(num_list) == 0:
        return None
    dic_num = {}
    for item in num_list:
        if item in dic_num:
            dic_num[item] += 1
        else:
            dic_num[item] = 1

    max_count = max(dic_num.values())
    modes = []
    for key,value in dic_num.items():
        if value == max_count:
            modes.append(key)
    return modes

def variance_calculator(num_list):
    """
    this function returns the variance of the provided number list
    """
    if len(num_list) == 0:
        return None

    x_hat = mean_calculator(num_list)
    summatory = 0
    for x in num_list:
        summatory += (x-x_hat)**2
    variance = summatory/len(num_list)
    return variance

def std_dev_calculator(num_list):
    """
    this function returns the std deviation of the provided number list
    """
    if len(num_list) == 0:
        return None
    std_dev = variance_calculator(num_list)**0.5
    return std_dev

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py InputFile.txt")
        sys.exit(1)

    start_time = time.time()
    filename = sys.argv[1]
    file_data = extract_data(filename)
    file_mean = mean_calculator(file_data)
    file_mode = mode_calculator(file_data)
    file_median = median_calculator(file_data)
    file_variance = variance_calculator(file_data)
    file_std_dev = std_dev_calculator(file_data)
    elapsed_time = time.time() - start_time

    with open("StatisticsResults.txt", 'w', encoding="UTF-8") as results_file:
        results_file.write("Mean: " + str(file_mean) + "\n")
        results_file.write("Median: " + str(file_median) + "\n")
        results_file.write("Mode: " + str(file_mode) + "\n")
        results_file.write("Standard Deviation: " + str(file_std_dev) + "\n")
        results_file.write("Variance: " + str(file_variance) + "\n")
        results_file.write("Time elapsed: " + str(elapsed_time) + " seconds\n")

    print("Mean:", file_mean)
    print("Median:", file_median)
    print("Mode:", file_mode)
    print("Standard Deviation:", file_std_dev)
    print("Variance:", file_variance)
    print("Time elapsed:", elapsed_time, "seconds")
