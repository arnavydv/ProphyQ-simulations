import math 
import numpy as np 
from scipy.integrate import quad
def poisson_pmf(average_rate:float,event_to_find_probability:float)->float:
    """poisson random variable tells us about 
    somethings is happening at an average rate 
    so it tell probability of an event based on average rate"""
    exp= (math.e**(-average_rate))
    secondterm=(average_rate**event_to_find_probability)/math.factorial(event_to_find_probability)
    return exp*secondterm

def binomial_pmf(success:float,number_of_trails:float,proability:float)->float:
    """binomial random variable tells about the 
    probability of success only like what is the probability of two heads 
    out of theree trials"""
    choosing=math.factorial(number_of_trails)/(math.factorial(success)*math.factorial(number_of_trails-success))
    second_term=proability**success
    third_term=(1-proability)**(number_of_trails-success)
    return choosing*second_term*third_term

def prob_uni_rv(f, ll: float, ul: float):
    return quad(f, ll, ul)


