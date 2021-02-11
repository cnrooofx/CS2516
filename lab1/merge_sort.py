from random import randint

def merge_sort(mylist):
    n = len(mylist)
    if n > 1:
        list1 = mylist[:n//2]
        list2 = mylist[n//2:]
        merge_sort(list1)
        merge_sort(list2)
        merge(list1, list2, mylist)


def merge(list1, list2, mylist):
    f1 = 0
    f2 = 0
    while f1 + f2 < len(mylist):
        if f1 == len(list1):
            mylist[f1+f2] = list2[f2]
            f2 += 1
        elif f2 == len(list2):
            mylist[f1+f2] = list1[f1]
            f1 += 1
        elif list2[f2] < list1[f1]:
            mylist[f1+f2] = list2[f2]
            f2 += 1
        else:
            mylist[f1+f2] = list1[f1]
            f1 += 1


def main():
    to_sort = []
    for i in range(20):
        to_sort.append(randint(i, 100))
    merge_sort(to_sort)
    print(to_sort)


if __name__ == "__main__":
    main()
