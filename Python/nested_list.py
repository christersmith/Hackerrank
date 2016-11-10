n1 = int(input())
if ((n1 > 1) and (n1 < 6)):
    n2 = [[input(), float(input())] for i in range(n1)] #shows a nested list of the four lists
    second_lowest = sorted(list(set([score for name, score in n2])))[1] #shows a single list with the four scores only
    print('\n'.join([a for a,b in sorted(n2) if b == second_lowest])) #sorted(n2) is necessary if there is a tie so alphabetically
    #this print statement matches the value of b and gives the value of a
else: quit()