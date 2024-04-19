'''Python: Basic

15 points

This assignment will develop your familiarity with doing simple computations in Python.
'''

import math

def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    5 points.

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''  
    after_tax = math.floor((1 - tax_rate) * gross_pay)
    take_home_pay = after_tax - expenses
    
    return take_home_pay

import math

def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    5 points.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''

    job_waste = total_material - (num_jobs * job_consumption)
    return str(job_waste) + material_units

import math

def interest(principal, rate, periods):
    '''Interest.
    5 points.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''

    simple_interest = math.floor((principal * rate * periods) + principal)
    
    return simple_interest
