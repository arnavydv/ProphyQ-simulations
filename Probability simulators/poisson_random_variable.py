import math 
def poisson_pmf(average_rate:float,event_to_find_probability:float)->float:
    """poisson random variable tells us about 
    somethings is happening at an average rate 
    so it tell probability of an event based on average rate"""
    exp= (math.e**(-average_rate))
    secondterm=(average_rate**event_to_find_probability)/math.factorial(event_to_find_probability)
    return exp*secondterm


