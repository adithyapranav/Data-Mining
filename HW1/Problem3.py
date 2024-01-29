import math
box=[]
print("Enter length and width of first box seperated by \",\" :",end="")
box.append(list(map(int,input().split(','))))
print("Enter length and width of second box seperated by \",\" :",end="")
box.append(list(map(int,input().split(','))))
print("Enter length and width of second box seperated by \",\" :",end="")
box.append(list(map(int,input().split(','))))
print("Enter length and width of second box seperated by \",\" :",end="")
box.append(list(map(int,input().split(','))))
print("-------------------------------")
print("Box 1 length is",box[0][0], "width is",box[0][1])
print("Box 2 length is",box[1][0], "width is",box[1][1])
print("Box 3 length is",box[2][0], "width is",box[2][1])
print("Box 4 length is",box[3][0], "width is",box[3][1])
X=[box[0][0],box[1][0],box[2][0],box[3][0]]
Y=[box[0][1],box[1][1],box[2][1],box[3][1]]
X_mean=sum(X)/len(X)
Y_mean=sum(Y)/len(Y)
X_sd=[i-X_mean for i in X]
Y_sd=[i-Y_mean for i in Y]
#print(X_sd,Y_sd)
numerator=[X_sd[i]*Y_sd[i] for i in range(4)]
numerator=sum(numerator)
denomenator_1=(sum([i**2 for i in X_sd]))
#print(denomenator_1)
denomenator_2=(sum([i**2 for i in Y_sd]))
corelation=numerator/((denomenator_1**(1/2))*(denomenator_1**(1/2)))
print("Correlation",corelation)