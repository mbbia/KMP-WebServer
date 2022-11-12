# helper function used to read and process the covid sequence needed by the kmp algorithm
def process_sequence(filename):
    stored_sequence = []
    with open('stored_sequences/'+filename) as f:
        _ = f.readline()
        for line in f:
            stored_sequence.append(line.strip())
    stored_sequence = "".join(stored_sequence).upper()

    return stored_sequence

# helper function that checks that the file contains only ATCG characters
def check_letters(string):
    MAX_DESIRED_LENGTH = 50
    a = string.count('A')
    t = string.count('T')
    g = string.count('G')
    c = string.count('C')
    sum = a+t+g+c
    if sum == len(string) and len(string) <= MAX_DESIRED_LENGTH:
        return True
    else:
        return False
