# Vickerman_Assignment-5_Part-1.py

def recursiveCheck(List, start, largest, end):
    if start < end:
        if List[start] > largest:
            largest = List[start]
        recursiveCheck(List, start+1, largest, end)
    else:
        print(f'The largest number in the list is {largest}')

def main():
    numList = [15,20,300,187,10,44]
    recursiveCheck(numList, 0, 0, len(numList))


if __name__ == "__main__":
    main()

"""
The largest number in the list is 300
"""