a = int(input())
A = set(map(int,input().split()))
if len(A) == a:
    n= int(input())
else: "Your set is missing numbers"
commands = []

#inputs the number of actions with their set numbers as lists within a list
for i in range(n*2):
    commands.append(input().split())
#changes the numbers from strings to integers. Step = 2 because the 2nd line is the string of numbers which are in spot 1,3,etc
for x in range(0, len(commands),2):
    if int(commands[x][1]) == len(commands[x+1]):
        for i in range(1,len(commands),2):
	        commands[i] = set(map(int,commands[i]))
    else: "Your data isn't matching", quit()
#reading strings in spot 0,2,4,etc for these types of sets, and affecting spots 1,3,5, etc accordingly.
for i in range(0,len(commands),2):
	if commands[i][0] == 'intersection_update':
		A.intersection_update(commands[i+1])
	elif commands[i][0] == 'update':
		A.update(commands[i+1])
	elif commands[i][0] == 'symmetric_difference_update':
		A.symmetric_difference_update(commands[i+1])
	elif commands[i][0] == 'difference_update':
		A.difference_update(commands[i+1])
print(sum(A))