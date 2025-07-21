

class FactorialService:
     def factorial(self,number):
         prod=1
         for i in range(1,number+1):
             prod*=i
         return prod