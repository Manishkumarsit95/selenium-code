# Ask to enter the number
Num = int(input("Enter the Number: "))

# initiate value to null

revr_Num = 0

# loop
while (Num>0):
 # Logic

    reminder = Num%10
    revr_Num = (revr_Num*10) + reminder
    Num = Num//10
 # print he value
print("The reverse num is :{}".format(revr_Num))
#############


n = int(input("please give a number : "))
print("before reverse your numeber is : %d" %n)
reverse = 0
while n>0:
    reverse = reverse*10 + n%10
    n = (n//10)
print("After reverse : %d" %reverse)

#Reminder = number %10
#Reminder = 12345%10 = 5
#Reverse = Reverse *10 + Reminder Initial value of revs_number is null
#Reverse = 0 * 10 + 5 = 0 + 5 = 5
#Number = Number //10
#Number = 1234 //10 = 1234 // Now loop will iterate on this number.