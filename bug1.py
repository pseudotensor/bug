def get_last_elements(lst, n):
    return lst[-n:]

def main():
    test_list = [1, 2, 3]
    print(get_last_elements(test_list, 5))

if __name__ == '__main__':
    main()