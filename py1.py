WORKING_LIST_1 = [1, 2, 3, 1, 2, 5, 6]

def double_items(work_list: list) -> list:
    return list(set([i for i in work_list if work_list.count(i) > 1]))


def main():
    print(f"{WORKING_LIST_1} - {double_items(WORKING_LIST_1)}")


if __name__ == "__main__":
    main()