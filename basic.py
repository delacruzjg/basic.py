'''Python: Basic

15 points

This assignment will develop your familiarity with doing simple computations in Python.
'''



def savings(gross_pay, tax_rate, expenses):
    import math
    after_tax = math.floor((1 - tax_rate) * gross_pay)
    take_home_pay = after_tax - expenses
    
    return take_home_pay



def material_waste(total_material, material_units, num_jobs, job_consumption):
    import math
    job_waste = total_material - (num_jobs * job_consumption)
    return str(job_waste) + material_units




def interest(principal, rate, periods):
    import math
    simple_interest = math.floor((principal * rate * periods) + principal)
    
    return simple_interest
