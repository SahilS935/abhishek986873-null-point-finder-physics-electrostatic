print("\n * THINGS THAT WE CAN CALCULATE :-\n\n","G) NULLPOINT FOR LIKE CHARGES\n\n","I) NULLPOINT FOR UNLIKE CHARGES\n\n","K) AMOUNT OF CHARGE TO MAINTAIN STABILITY/EQUILIBRIUM FOR LIKE CHARGE (From Q1)\n\n","M) AMOUNT OF CHARGE TO MAINTAIN STABILITY/EQUILIBRIUM FOR UNLIKE CHARGES(FROM Q1)\n\n","O) DISTANCE BETWEEN TWO CHARGES IF NULL POINT IS GIVEN for Unlike (FROM Q1)\n\n","Q) DISTANCE BETWEEN TWO CHARGES IF NULL POINT IS GIVEN for like (FROM Q1)\n\n","S) AMOUNT OF 1ST CHARGE (if null point is given)\n\n","U) AMOUNT OF 2ND CHARGE (if null point is given)")
Z="G" #NULL POINT FOR LIKE
H="I" # NULLPOINT FOR UNLIKE CHARGES
J="K"# AMOUNT OF CHARGE TO MAINTAIN STABILITY/EQUILIBRIUM FOR LIKE CHARGE (From Q1
L="M"#AMOUNT OF CHARGE TO MAINTAIN STABILITY/EQUILIBRIUM FOR UNLIKE CHARGES(FROM Q1)
N="O"#DISTANCE BETWEEN TWO CHARGES IF NULL POINT IS GIVEN for Unlike (FROM Q1)
P="Q"#DISTANCE BETWEEN TWO CHARGES IF NULL POINT IS GIVEN for like (FROM Q1)
R="S"#AMOUNT OF 1ST CHARGE (if null point is given)
T="U"#AMOUNT OF 2ND CHARGE (if null point is given)
#print("* please do not put same value in 1st and 2nd charge \n\n"," 
# * AND\n\n","* please always put big charge on Q2\n\n")
print("--------------------------------------------------------------------------------------------- ")
print("* Instructions\n")
print('* Please do not put same charge in 1st and 2nd\n')
print("* Always put big charge in Q2")
print('---------------------------------------------------------------------------------------------')
a=float(input("• 1st charge Q1 (IF NOT KNOWN PLESE ENTER 1) = "))
print( )
b=float(input("• 2nd charge Q2 (IF NOT KNOWN PLESE ENTER 1) = "))
print( )
c=float(input("• Distance between two charge (IF NOT KNOWN PLESE ENTER 1) = "))
print( )
d=float(input("• Charge present in middle (IF NOT KNOWN PLESE ENTER 1) = "))
print( )
e=float(input("• Distance of null point (IF NOT KNOWN PLESE ENTER 1) = "))
print( )
# null point for like charge
import math
g=math. sqrt(a)
h=math. sqrt(b)
i=(g*c)
j=(g+h)
#####final null point for like chargefrom Q1 only
k=float((i/j))
#null point for unlike charge from Q1 only
l=(h-g)
####final null point for unlike charge
A=float((i/l))
#amount of charge to maintain stability
m=(a*b)
n=(j**2)
######amount of charge to maintain stability for like
o=(m/n)
#amount of charge to maintain stability for unlike
p=(l**2)
#######amount of charge to maintain stability for unlike
q=(m/p)
# DISTANCE BETWEEN TWO CHARGES IF NULL POINT IS GIVEN for like
r=(e*j)
s=(g)
##### DISTANCE BETWEEN TWO CHARGES IF NULL POINT IS GIVEN for like 
t=(r/s)
#DISTANCE BETWEEN TWO CHARGES IF NULL POINT IS GIVEN for unlike
u=(A*l)
v=(g)
#####DISTANCE BETWEEN TWO CHARGES IF NULL POINT IS GIVEN for unlike from Q1 only
w=(u/v)
#amount of 1st charge
x=(k*j)
y=(x/c)
######## amount of 1st charge
z=(y**2)
# amount of 2nd charge if null point is given
C=(c-e)
D=(g*C)
##### amount of 2nd charge if null point is given
E=(D/e)
F=input("* WHAT TO CALCULATE (please entre index number) = ")
print( )
if F==Z:print("• NULL POINT FOR LIKE CHARGES = ",k)
if F==H:print("• NULL POINT FOR UNLIKE CHARGES = ",A)
if F==J:print("• AMOUNT OF CHARGE TO MAINTAIN STABILITY/EQUILIBRIUM FOR LIKE CHARGE (From Q1) = ",o)
if F==L:print("• AMOUNT OF CHARGE TO MAINTAIN STABILITY/EQUILIBRIUM FOR UNLIKE CHARGES(FROM Q1) = ",q)
if F==N:print("• DISTANCE BETWEEN TWO CHARGES IF NULL POINT IS GIVEN for Unlike (FROM Q1)",w)
if F==P:print("• DISTANCE BETWEEN TWO CHARGES IF NULL POINT IS GIVEN for like (FROM Q1)",t)
if F==R:print("• AMOUNT OF 1ST CHARGE (if null point is given) = ",z)
if F==T:print("• AMOUNT OF 2ND CHARGE (if null point is given) = ",E)

