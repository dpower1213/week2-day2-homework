
numbers=[1,2,3,4,5]
def sum_two_smallest_numbers(numbers):
    print(numbers)
    newnumbers=sorted(numbers)
    print(newnumbers)
    print(newnumbers[1])
    
    number=newnumbers[0]+newnumbers[1]
    print(number) 
sum_two_smallest_numbers(numbers)   
