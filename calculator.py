class Calculator:
    def sum(self ,a,b):
        result = a + b
        return result
    
    def sub ( self ,a , b):
        result = a - b
        return result
    
    def mul (self ,a , b): # умножение multiplay
        return a*b
    
    def div (self , a , b) : # деление
        if ( b==0 ):
            raise ArithmeticError("на ноль делить нельзя")
        return a / b
    
    def pow (self ,a , b = 2): # возведение в степень

        return a**b # а возводится в степень b
    
    def avg(self , nums):# нахождение среднего - работа со списком nums - надо же среднее
        if (len(nums) == 0):
            return 0
        
        s = 0 
        for num in nums:
            s = self.sum(s,num)

        l = len (nums)
        return self.div ( s, l)