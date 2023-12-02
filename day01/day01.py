word_to_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def extract_numbers(line):
    words = line.split()
    extracted_numbers = []
    for word in words:
        if word.isdigit():
            extracted_numbers.append(int(word))
        elif word.lower() in word_to_num:
            extracted_numbers.append(word_to_num[word.lower()])

    if extracted_numbers:
        return extracted_numbers[0], extracted_numbers[-1]
    else:
        return None, None

file_name = 'input.txt'
total_sum = 0

with open(file_name, 'r') as file:
    for line in file:
        first_num, last_num = extract_numbers(line)
        if first_num is not None and last_num is not None:
            total_sum += (first_num + last_num)

output_file = 'output.txt'
with open(output_file, 'w') as file:
    file.write(f"Total sum of first and last numbers found in the file: {total_sum}\n")

print(f"Total sum has been written to '{output_file}'")
