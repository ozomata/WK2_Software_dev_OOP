class Sales:
 
    def __init__(self, amt, year):
        self.year =int(year)
        self.amt=amt
        
    def profit(self, year):
        yearSales=self.amt+(self.amt*(int(year)-1)*0.05)
        return float (yearSales*0.23)
    
   
    
user_amt= float(input("input the sales: "))
#user_year= input("input the  year of  sales: ")
user_year= input("input the  Number of years you you want reported: ")
userSales = Sales (user_amt, user_year)

#print("The profit for year", userSales.year , " : " ,   userSales.profit(int(user_year)))
for i in range(int(user_year)):
    print("The profit for year",i+1, " : " ,   userSales.profit(i))