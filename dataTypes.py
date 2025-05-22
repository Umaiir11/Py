# Modern Python mai nullable variable bananay k liye Optional[int] use hota hai
from typing import Optional

# 💡 Optional ka matlab: ya to value hogi (int) ya None (khaali)

# 🔸 Ye dono integer numbers hain
a: Optional[int] = 35
b: Optional[int] = 26

# 🔸 Total ka variable banaya, abhi koi value nahi di (matlab None hai)
total: Optional[int] = None

# ✅ Yeh print karega dono numbers ko
print("Integers hain:", a, b)

# ➕ Add kar rahe hain dono numbers ko
totalAdd: Optional[int] = a + b
print("Total Add hai:", totalAdd)

# ➖ Subtract kar rahe hain
totalSubtract: Optional[int] = a - b
print("Total Subtract hai:", totalSubtract)

# ✖️ Multiply kar rahe hain
totalMultiply: Optional[int] = a * b
print("Total Multiply hai:", totalMultiply)

# ➗ Divide kar rahe hain
totalDivide: Optional[float] = a / b
print("Total Divide hai:", totalDivide)

#2. Float (float)

# Float ka matlab: decimal numbers hain
# 🔸 Ye dono float numbers hai
c: Optional[float]=33.5
d: Optional[float]=55.3
totalFloat: Optional[float] = None


totalAddFloat: Optional[float] = c + d
print("Here's float Total: ",totalFloat)

#String (str)
# String ka matlab: text ya characters hain
# 🔸 Ye dono string hai nullable

e : Optional [str]="Umair"
f: Optional [str]="Hashmi"
print("Strings are : ", e,f)
print("Hello " + e + " " + f + " welcome to Python!")

#boolean (bool)
# Boolean ka matlab: True ya False hai
# 🔸 Ye dono boolean ha

age :Optional[int]= 25
hasLogin: Optional[bool]=None
hasLogin = age>24
print("Has Login:", hasLogin)

a: Optional[int] =112
b: Optional[int] = 45
isGreater: Optional[bool]=None
isGreater = a > b
print("Is "+str(a)+" Greater than "+str(b)+"  :", isGreater)

#list
# List ka matlab: ek list hai jisme multiple values ho sakti hain
# 🔸 Ye dono list hai

rollnumbers : Optional[list[int]] =[1,2,3,4,5,6] ; print(" Length: ",len(rollnumbers), " Roll Numbers: ", rollnumbers)    
names: Optional[list[str]] = ["Umair","Hashmi","Ali","Ahmed","Salman"] ; print (" Length: ",len(names), "  Names: ", names)
developers : Optional[list[str]]= ["Moeen","Atif","Ali","Ahmed","Zain"] ; print ("  Length: ",len(developers)," Developers: ", developers)


#print value from list index
print("Developer: ", developers[3]) # print value from list index
#print index of Ali from list 
print("Developer: ", developers.index("Ali")) 

