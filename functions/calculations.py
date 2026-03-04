import math

def calculate_bacterial_growth(n0,t,g):
    if g <= 0:
        return 0
    
    n_gen= t /g 
    nt = n0* (2**n_gen)

    return nt, n_gen

def get_growth_steps(n0,t,g, steps=10):

    times_points = []
    counts = []

    for i in range(steps + 1 ):
        current_t = (t/steps) * i 
        nt_step,_ = calculate_bacterial_growth(n0,current_t,g)
        times_points.append(int(current_t))
        counts.append(int(nt_step))
        