# Author: CAM (AMDG) 9/26/2020

current_pop = 332786110

growth_per_year = (60 * 60 * 24 * 7 * 52) / 25

growth_per_day = (60 * 60 * 24) / 25

future_pop = current_pop + growth_per_year + growth_per_day

print("The estimated population on 9/24/2021 will be " + str(future_pop) + ".")
