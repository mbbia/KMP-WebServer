def compute_lps_array(pattern):
    pat_len = len(pattern)
    lps_array = [0 for x in range(0, pat_len)]

    i = 0
    j = 1

    # untill index on pattern reaches the end of the pattern
    while j < pat_len:
        # if there is a match
        if pattern[i] == pattern[j]:
            # increment the value on the lps array
            lps_array[j] = i + 1
            i += 1
            j += 1
        # if there is not a match
        else:
            # if on the beginning of the string
            if i == 0:
                # set the position of the letter compared to zero
                # and increment j to compare the next letter
                lps_array[j] = 0
                j += 1
            else:
                i = lps_array[i-1]

    return pat_len, lps_array

def kmp_search(string, pattern):
    results = []

    # compute the lps array of the pattern
    pat_len, lps_array = compute_lps_array(pattern)
    str_len = len(string)

    i = 0
    j = 0

    # untill index on string reaches the end of the string
    while i < str_len:
        # if there is a match, increment both indexes
        if string[i] == pattern[j]:
            i += 1
            j += 1

        # if, keeping incrementing the indexes,
        # the end of the pattern is reached
        # then, a result has been found
        if j == pat_len:
            results.append(str(i-j))
            j = lps_array[j-1]

        # if the index is inside the string
        # and the pattern doesn't match the string
        elif i < str_len and string[i] != pattern[j]:
            # if j is not on the beginning of the pattern
            if j != 0:
                # set j to the right value on the lps array
                j = lps_array[j-1]
            # if it's on the beginning of the pattern
            else:
                # increment i by one
                i += 1

    # compute the number of matches between the string and the pattern
    num_matches = len(results)

    return results, num_matches
