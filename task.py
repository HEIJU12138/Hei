# The python task

import random
def div_and_write(L):
    new =[]
    # create a list of list
    new.append(L)
    count =1
    f = open('result.txt', 'a+', encoding='Utf-8')
    # while loop for reading and writing
    while len(new)!=0:
    # take the first list and delete it
     L3 = new[0]
     del new[0]
     # take min and max of the list
     m1 = min(L3)
     m2 = max(L3)
     d = (m1 + m2) / 2
     f.write('{}  min:{}  min:{}  length:{} \n'.format(count, m1, m2, len(L3)))
     count +=1
     # if length>5, the divide into two part(二分)
     if len(L3) > 5:
        L2 = []
        L1 = []
        # store the data in two list and initiate it
        for i in L3:
          if m1 <= i and i < d:
            L1.append(i)
          if m2 >= i and i >= d:
            L2.append(i)
        # first add the left node and then the second
        new.append(L1)
        new.append(L2)

    return
# create a random list
a=[ random.uniform(0,100) for i in range(100)]
div_and_write(a)
