
# The python task

import random
def div_and_write(L):
    new =[]
    new.append(L)
    count =1
    f = open('result.txt', 'a+', encoding='Utf-8')
    # the while loop
    while len(new)!=0:
    # take the list and delete it
     L3 = new[0]
     del new[0]
     m1 = min(L3)
     m2 = max(L3)
     d = (m1 + m2) / 2
     f.write('{}  min:{}  min:{}  length:{} \n'.format(count, m1, m2, len(L3)))
     count +=1
     # if length>5, the divide into two part
     if len(L3) > 5:
        L2 = []
        L1 = []
        for i in L3:
          if m1 <= i and i < d:
            L1.append(i)
          if m2 >= i and i >= d:
            L2.append(i)
        new.append(L1)
        new.append(L2)

    return
a=[ random.uniform(0,100) for i in range(100)]
div_and_write(a)
