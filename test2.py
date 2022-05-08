#### Lists



def test_1():
    print("basic python lists")

    nums = [1,2,3,89,56,3456,1234,123,435]

    # read
    print(nums[0])
    print(nums[3])

    # add 
    nums.append(42)
    nums.append(-1)

    # remove by element
    nums.remove(56)

    # remove by index
    del nums [0]

    print(nums)



    # loop 
    for n in nums:
        print (n)




def test_2():
    print("Sum numbers")

    prices = [12.23,345,123.2,542,65,123.2,0.223,-23, 123.2,6,171,5678]


    # for and print every number
    # q1 - print the sum of all number
    total = 0
    for num in prices:
        total += num 

        print(total)

    # call 
    #test_1()
    test_2()