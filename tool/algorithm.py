'''
algorithm task
'''

def multTable(numlist):
    if(len(numlist)<2):
        listresult = [numlist[0] * numlist[0]]
        # print (listresult)
        return listresult
    else:
        bynumber = numlist[0]
        list1 = [i*bynumber for i in numlist[1:]]
        # listresult = [bynumber] + list1
        print(list1)
        return [bynumber*bynumber] + list1
numlist = [5,2,6,3,5]
# testlist = [2,3]
# result = numlist + testlist
print(multTable(numlist))
# multTable(result)