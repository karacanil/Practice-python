#Element Search
#Exercise 20
#Solution with Linear search

def present(list,num):
    for eachElement in list:
        if eachElement == num:
            return True

    return False


if __name__ == '__main__':

    #Creating a list
    l = []

    #Getting the number of elements in the list from user
    num_element = int(input('Enter the number of the elements in the list:'))

    #Getting the input from user
    for x in range(num_element):
        l.append(int(input('Enter the %d. number:'%(x+1))))

    #Sorting the unordered list
    l = sorted(l)

    #User decides the number to search in the list
    searchNum=int(input('Enter a number to see if it is present in the list:'))

print(present(l,searchNum))
