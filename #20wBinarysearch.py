#Element Search
#Exercise 20
#Solution with Binary search

def binary_search(list,target):
    firstIndex = 0
    lastIndex = len(list)-1
    result=False

    while firstIndex<=lastIndex and not result:
        mid = (firstIndex + lastIndex)//2

        if list[mid] == target:
            result = True
        elif target < list[mid]:
            lastIndex = mid-1
        else:
            firstIndex = mid+1

    return result

if  __name__ == '__main__':
    #Creating a list
    l = []

    #Getting the number of elements in the list from user
    num_element = int(input('Enter the number of the element in the list:'))

    #Getting the input from user
    for x in range(num_element):
        l.append(int(input('Enter the %d. number:'%(x+1))))

    #Sorting the unordered list
    l = sorted(l)

    #User decides the target number to search in the list
    searchNum=int(input('Enter a number to see if it is present in the list:'))

print(binary_search(l,searchNum))
