import numpy as np
import matplotlib.pyplot as plt

def get_initial_values(K,m_tot,ds):
    inital_value = np.empty(m_tot+2)
    inital_value[0] = 0
    inital_value[-1] = 0
    for i in range(1,m_tot+1):
        inital_value[i] = max(K-ds*i,0)
    return inital_value

def BS_difference_method_solver(T,s_2,K,sigma,m_tot,ds,dt):
    solution = np.zeros((m_tot+2,T))
    initial_values = get_initial_values(K,m_tot,ds)
    top_boundary_values = np.zeros(T)
    top_boundary_values.fill(K)
    bottom_boundary_values = np.zeros(T)
    bottom_boundary_values.fill(0)
    
    solution[:,-1] = initial_values
    solution[-1,:] = bottom_boundary_values
    solution[0,:] = top_boundary_values
    for t in range(T-1,0,-1):
        for s in range(1 ,m_tot+1):
            solution[s,t-1] = solution[s,t] + ((s/ds)*sigma**2)/2*(solution[s+1,t] - 2*solution[s,t] + solution[s-1,t])
            print(solution)
    return solution

price_steps = 10                            #m_tot
fixed_price = 1                             #k
upper_price_limit = 1.5*fixed_price         #s_2
fixed_time = 5                              #T
volatility  = 0.2                           #sigma
delta_s = upper_price_limit/price_steps     #ds
delta_t =  (1/(price_steps*volatility))**2   #dt

solution = BS_difference_method_solver(fixed_time,upper_price_limit,fixed_price,volatility,price_steps,delta_s,delta_t)