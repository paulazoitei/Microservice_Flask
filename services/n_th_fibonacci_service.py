
class FibonacciService:

    def fibo(self,n):
         if n ==0:
             return 0
         elif n ==1:
             return 1
         else:
             return self.fibo(n - 1)+ self.fibo(n - 2)

