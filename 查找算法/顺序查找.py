def seqsearch(seq:list, target):
    # 仅查找出第一个元素的位置 时间复杂度O(n )
    for index in range(seq.__len__()):
        if seq[index] == target:
            return index

if __name__ == '__main__':
    print(seqsearch([1,3,4,5], 5))