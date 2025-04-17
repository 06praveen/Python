BS=int(input("Enter your Basic Salary : "))
DA=0.7*BS     #The dearness allowance (DA) as 70% of BS
TA=0.3*BS     #The travel allowance (TA) as 30% of BS
HRA=0.1*BS    #The house rent allowance (HRA) as 10% of BS
print("the dearness allowance as 70% of BS is ",DA,"The travel allowance  as 30% of BS is ",TA,"and the house rent allowance as 10% of BS is ",HRA)
GS=BS+DA+TA+HRA
print("The Gross Salary is : ",GS)