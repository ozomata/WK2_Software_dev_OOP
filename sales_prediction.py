class Sales:
 
    def __init__(self, amt, year):
        self.year =int(year)
        self.amt=amt
        
    def profit(self, year):
        yearSales=self.amt+(self.amt*(int(year)-1)*0.05)
        return float (yearSales+yearSales*0.23)
    
   
    
user_amt= float(input("input the sales: "))
user_year= input("input the  year of  sales: ")

userSales = Sales (user_amt, user_year)

print("The profit for year", userSales.year , " : " ,   userSales.profit(int(user_year)))
