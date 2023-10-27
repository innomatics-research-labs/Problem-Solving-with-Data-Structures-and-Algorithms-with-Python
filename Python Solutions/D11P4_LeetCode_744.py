def next_greatest_letter(letters, target):
    start_index = 0
    end_index = len(letters) - 1

    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index) // 2

        if target < letters[middle_index]:
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1

    return letters[start_index % len(letters)]


if __name__ == "__main__":
    letters = ['c', 'f', 'j']
    print(next_greatest_letter(letters, 'c'))
