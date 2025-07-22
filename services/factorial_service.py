

class FactorialService:
     def factorial(self,number):
         if number == 0:
             return 1
         prod=1
         for i in range(1,number+1):
             prod*=i
         return prod