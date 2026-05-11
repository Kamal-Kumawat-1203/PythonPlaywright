from playwright.sync_api import Page

def test_group_a_list_data_by_length(page):
    words = ["bat", "cat", "apple", "dog", "banana", "orange", "cucumber", "watermelon"]
    length_map = {}

    # 1: Group world by length
    for word in words:
        length = len(word)

        if length not in length_map:
            length_map[length] = []
        length_map[length].append(word)

    # 2: Print in sorted order of length

    for length in sorted(length_map):
        print(length_map[length])
