# I really don't know python very well...
# I just finished problem 10 and i'm just now realizing that i can do this in swift so I'm going to do problem 11 onward in swift

'''
 fizzbuzz( start , end ):
   for number in end - start:
        print number
       if divisible by five and three:
           print fizzbuzz
           continue
        if divisible by five:
            print buzz
            continue
        if divisible by three:
            print fizz
            continue
'''


def fizzbuzz(start, end):
    for num in range(start,end):
        if num % 5 == 0 and num % 3 == 0:
            print("fizzbuzz")
            continue
        if num % 3 == 0:
            print("fizz")
            continue
        if num % 5 == 0:
            print("buzz")
            continue
        print(num)


fizzbuzz(6,41)