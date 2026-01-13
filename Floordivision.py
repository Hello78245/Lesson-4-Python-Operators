#Taking the total amount from user
Amount=int(input("How much do you take"))
#Calculating the number of notes taken by different denominations
note_1=Amount//10
note_2=(Amount%10)//50
note_3=((Amount%10)%50)//10

print("notes of 100 dollars",note_1)
print("notes of 50 dollars",note_2)
print("notes of 10 dollars",note_3)
