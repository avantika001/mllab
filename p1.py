import csv
filename='1-dataset.csv'
lines=csv.reader(open(filename))
data=list()

for row in lines:
	if(row[-1]=='Yes'):
		data.append(row)

noOfRows=len(data)
noOfCols=len(data[0])-1

hypothesis=['%' for _ in range(noOfCols)]

print("dataset:\n")

for x in data:
	print(x)

print("no of cols:",noOfCols)
print("no of rows:",noOfRows)
print("hypothesis:",hypothesis)

hypothesis=data[0][:-1]

for i in range(noOfRows):
	for j in range(noOfCols):
		if(hypothesis[j]!=data[i][j]):
			hypothesis[j]='?'
		else:
			None

print("final hypothesis:",hypothesis)
print("enter test case:")
testcase=input();
testcase=testcase.split(',')

flag=1;
for i in range(len(hypothesis)):
	if(hypothesis[i]!='?'):
		if(hypothesis[i]!=testcase[i]):
			flag=0
			break

if(flag==1):
	print("Accepted")
else:
	print("Rejected")