#add two numnbers
from typing import Optional


#add twoi numbers
a: Optional[int] = 5
b: Optional[int] = 7
c = a + b
print("Sum of a and b is:", c)

# find area of rectangle
leftSidee : Optional[int] = 10
rightSidee : Optional[int] = 5
area = leftSidee * rightSidee
print("Area of rectangle is:", area)

# find days from age
age: Optional [int] = 27
days = age * 365
print("Age in days is:", days)

#find percentage
optainedMarks: Optional[int] = 40
totalMarks : Optional[int] = 100
percentage = (optainedMarks / totalMarks) * 100
print("Percentage is:", percentage) 

#calculate simplke interest

principal: Optional[int] = 1000
rate: Optional[int] = 5
time: Optional[int] = 2
simpleInterest = (principal * rate * time) / 100
print("Simple Interest is:", simpleInterest)

#km to miles
kilometers: Optional[float] = 5.0
miles : Optional[float]= kilometers * 0.621371
print("Miles: ", miles)


#find quotient
number1 : Optional[float] =20.1
number2 : Optional[float] =30.2
quotient: Optional[float] = (number1/number2)
print ("Quotient: ", quotient)

#liters into gallons
liters : Optional[float] = 39.9
gallons: Optional[float] = (liters* 0.264172)
print("Gallons: ",gallons)


#print full name
firstName: Optional[str] ='Umair'
lastName: Optional[str] = 'Hashmi'

print("Hey "+firstName +" "+lastName+" How are You , Here is your full name "+firstName+ " "+lastName+"")


#character count
sentence : Optional[str] = "Hey my namew is Umair Hashmi"
char_count = len(sentence.replace(" ", ""))
print("Number of characters (excluding spaces):", char_count)


#palindrome

word = "madam"
is_palindrome = word == word[::-1]
print(f"Is '{word}' a palindrome? {is_palindrome}")



#upper leters
user_word: Optional[str] = "hi i am umair"
print("Uppercase:", user_word.upper())

#boolean even number
number : Optional[int] =11
isEvenNumber:Optional[bool] =None
isEvenNumber = number % 2 == 0
print(number, "is Even Number : " + str(isEvenNumber) + "  ")


#bolean greater then age
age : Optional[int] = 18
isAgeGreatyer : Optional [int] = age >= 18
print(f"Age: {age} | Is Age ≥ 18? {isAgeGreatyer}")

password : Optional[str] = "12345"
confirmPassword : Optional[str] = "12345ss"
hasMatched : Optional[bool] = None

hasMatched = password  == confirmPassword
print(f"password: {password} | Is equals to {confirmPassword}  ==  {hasMatched}")

#lists
#Add 3 Items to List
fruits : Optional[list[str]] = ['Kewi', 'Apple', 'Banana']
print("Fruits: ", fruits)

#Ask user for 3 numbers, store in list, print sum.

numbers :Optional[list[int]] =[22,32,91]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)

#Replace Item in List
newFruits : Optional[list[str]]= ['apple','banana','cherry']
index: Optional[int] = newFruits.index('banana')  # find index of item
newFruits[index] = 'orange'   
print(" New Fruits", newFruits)

#Take list of 4 numbers from user, sort and print.
listnumbers: Optional[list[int]] = [98, 32, 21, 72]
sorted_numbers = sorted(listnumbers)
print("Sorted numbers:", sorted_numbers)