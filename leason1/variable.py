# Legal Variable names

name = "Dita"
n = "Afif"
fullName = "Pradita Dwi Rahman" #Camel case
FullName= "Pradita D.R" #Pascal case
_umur = 19
nomer_rumah = "87" #snake case

#ilegal variable names

# -name = "haram"
# 1d = "dita"
# full-name = "Pradita D R"
# Full Name = "PDR"

#Data Types
"String"

"1. Single quote (' ')"
a = 'a'
description = 'Learn Python Basic'
ten = '10'


'2. Double quote (" ")'

address = "Mataram"


print(fullName)
print(19)
print("My name is "+ fullName)
print("My name is ", fullName)
print(f"My name is {fullName}, i live in {address}")

"Integer (int)"

x = 10
print(x+5)

p = 12
l = 3
large = p*l
print("Luas segitiga diatas adalah : ",large)


"Float (float)"

phi = 3.14
print(f"This is float : {phi}")


"Boolean"

maried = False
men = True

print(f"This is boolean : {maried}")


"Range"

d = range(10)
print(f"This is range : {d}")

"---- Array -----"
"List ( [] )"

game = ["Dota", "Valoran", "CS Go"]
campur = ["Jeruk",12, True, 3.14, [1,2,3]]

print(f"This is list : {game}")

"Dictionary ( {} )"

person = {
    "name": "Dita",
    "age" : 19,
    "address" : "Labuapi"
}
print(f"This is dictionary : {person}")


"Tuple ()"
fruits = ("Banana", "Mango", "Aple")
print(f"This is tuple : {fruits}")


