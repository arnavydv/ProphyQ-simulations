import math 
def poisson_rv(lam:float,event:float)->float:
    """poisson random variable tells us about 
    somethings is happening at an average rate 
    so it tell probability of an event based on average rate"""
    exp= (math.e**(-lam))
    secondterm=(lam**event)/math.factorial(event)
    return exp*secondterm


