n = int(input())
mydict = {}
if n in range(2,10):
    for line in range(n):
        info = input().split(" ")
        score = list(map(float, info[1:])) #changes x number of scores into floats
        mydict[info[0]] = sum(score) / float(len(score)) #inputs average of the entered scores into the dictionary with associated names
else: print("Error2")
print("%.2f" % mydict[input()])  #prints the pulled average value from the reference input name. %.2f = format float with 2 decimal places with period (instead of the normal one decimal place)