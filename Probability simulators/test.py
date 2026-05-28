from poisson_random_variable import poisson_pmf,binomial_pmf,prob_uni_rv
print(poisson_pmf(average_rate=3,event_to_find_probability=4))
#its tells that if 3persons/hr coming to a cafe then probability of 4 persons coming to a cafe is 
# other example is 
""" if i am doing 5 hours of work daily what is probability that i will do the work for 12 hours next day"""
print(poisson_pmf(average_rate=5,event_to_find_probability=12))#0.00343424028557
"""no we are testing for the probability of getting 2 heads out of 3 trials 
each time getting head we have a probability 0.5"""
print(binomial_pmf(2,3,0.5))#0.375
print("the prob is :",poisson_pmf(average_rate=50,event_to_find_probability=100))
def f(x):
    return 1 if True else 0
print(prob_uni_rv(f,0.3,0.5)) #0.2 in this uniform variable probability everywhere will be same