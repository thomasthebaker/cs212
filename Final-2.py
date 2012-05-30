"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
one is Wilkes and the other is Hamming.
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""
import itertools

def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    names = {1:'Hamming', 2:'Wilkes', 3:'Minsky', 4:'Knuth', 5:'Simon'}
    keys = [1,2,3,4,5]
    orderings = list(itertools.permutations(keys))
    indexes = next(sorted([(Hamming, 'Hamming'), (Wilkes,'Wilkes'), (Minsky, 'Minsky'), (Knuth,'Knuth'), (Simon, 'Simon')])
                for (Monday, Tuesday, Wednesday, Thursday, Friday) in orderings
                for (laptop, droid, iphone, tablet, _) in orderings
                if laptop is Wednesday #1
                and tablet is not Friday #8
                for (Wilkes, Hamming, Minsky, Knuth, Simon) in orderings
                if after(Knuth, Simon) #6
                for (programmer, writer, designer, manager, _) in orderings
                if programmer is not Wilkes #2
                and writer is not Minsky #4
                and manager is not Knuth and manager is not tablet #5
                and designer is not Thursday #7
                and designer is not droid #9
                and after(Knuth, manager) #10
                and ((laptop is Monday and Wilkes is writer) or (laptop is writer and Wilkes is Monday))#11
                and (iphone is Tuesday or tablet is Tuesday) #12
                and ((programmer is Wilkes and droid is Hamming) or (programmer is Hamming and droid is Wilkes)) #3
                    )
    return [name for (_,name) in indexes]

def after(a, b):
    return a-b==1

print logic_puzzle()
print 'Expect: [Wilkes, Simon, Knuth, Hamming, Minsky]'
