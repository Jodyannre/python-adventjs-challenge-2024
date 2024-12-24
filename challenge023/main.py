def main():
    print(find_missing_numbers([6,8]))
    pass

def find_missing_numbers(nums):
    max_index = max(nums)
    return [
        i for i in range(1,max_index) if i not in nums
    ]

if __name__ == '__main__':
    main()