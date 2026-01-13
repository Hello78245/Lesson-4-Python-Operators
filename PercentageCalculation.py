#take marks as input of user
print("Enter marks obtained in 4 subjects:")
math=int(input("maths:"))
english=int(input("English:"))
Science=int(input("Science:"))
PE=int(input("PE:"))

#Calculating the percentage of the marks
sum=math+english+Science+PE
print("the sum of the 4 are:")
perc=(sum/400)*100
print(end="Percentage Mark=")
print(perc)