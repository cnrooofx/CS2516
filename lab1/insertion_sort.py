def insertion_sort(mylist):
    n = len(mylist)
    i = 1
    while i < n:
        j = i - 1
        while mylist[i] < mylist[j] and j > -1:
            j -= 1
        #insert i in the cell after j
        temp = mylist[i]
        k = i - 1
        while k > j:
            mylist[k+1] = mylist[k]
            k -= 1
        mylist[k+1] = temp
        i += 1


def main():
    a_list = [1, 8, 3, 9, 5, 5, 2, 9, 0, 0, 0, 3, 5]
    insertion_sort(a_list)
    print(a_list)


if __name__ == "__main__":
    main()
