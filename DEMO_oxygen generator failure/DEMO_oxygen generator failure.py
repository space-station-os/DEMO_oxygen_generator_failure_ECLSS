import random
import numpy as np
import matplotlib.pyplot as plt
import math

# initial ｐarameters
ISS_VOLUME = 899    # Cubic meters   
second_backup_num_tanks = 200   # SFOGs
second_backup_supply = 600 # kg  SFOGs
M = 0.0058  # Mach number  (subsonic)
Cd = 0.6  # Discharge coefficient  [dimensionless number], an estimate for sharp-edged orifices in pressurized systems
T_in = 294.3  # Kelvin (21.15°C) Temperature inside ISS 
T_out = 283.15  # Kelvin (10°C)  Temperature outside ISS/average value 
airflow_velocity = 0.20  # m/s
leakage = 0.02 #kg/day air leakage rate per day (nominal)

#constants parameters 
INITIAL_OXYGEN_PRESSURE = 101325  # Pascals (1 atm)      standard pressure   178 mmHg for partial oxygen pressure
OXYGEN_DENSITY =  1.32    #kg/cubic meters,    value at standard  pressure and temperature 294.3 K 
OXYGEN_DINAMIC_VISCOSITY = 0.00002032     # Pa·s , value at standard  pressure  and temperature 294.3 K
EXTERNAL_PRESSURE = 0  # Pascals (vacuum)
OXYGEN_MOLECULAR_WEIGHT = 32  # g/mol
R_GAS_CONSTANT = 8.314  # J/(mol*K)
gamma = 1.4  # Adiabatic index 
delta_P = INITIAL_OXYGEN_PRESSURE - EXTERNAL_PRESSURE  
L =  73 # Meters (240 feet) Lenght ISS
pi= 3.1415926535897932384   # Mathematical constant


 
def calculate_oxygen_duration(initial_backup_oxygen_supply ,crew_size,second_backup_supply, second_backup_num_tanks, escape_rate_day):
   # Oxygen consumption rate per crew member (kg per day)
    oxygen_consumption_rate_per_person = 0.84  # kg/day

    
   # Calculate total oxygen consumption rate (kg per day) of crew
    total_consumption_rate = oxygen_consumption_rate_per_person * crew_size
    
   # Total oxygen loss rate (human pxygen consumption per day + Hole leak) kg per day + air leakage rate 
    total_oxygen_loss_rate =  (total_consumption_rate  + escape_rate_day + leakage)
    
    # Calculate oxygen consumption per day in the entered ISS 
    oxygen_consumption_day =(initial_backup_oxygen_supply +(second_backup_num_tanks*second_backup_supply)) / total_oxygen_loss_rate

    # Check for division by zero 
    if total_oxygen_loss_rate == 0:
        return 0, 0
      
    # Convert oxygen duration from minutes to hours and minutes
    days = oxygen_consumption_day
    total_minutes = days * 24 * 60
    hours = int(total_minutes //60)
    minutes = int(total_minutes % 60)

    return hours, minutes


# Calculate the initial oxygen mass in kg for the backup oxygen generator Vozdukh at the international space station
initial_backup_oxygen_supply = ((INITIAL_OXYGEN_PRESSURE * ISS_VOLUME) / (8.314 * T_in)) * OXYGEN_MOLECULAR_WEIGHT / 1000  # kg  Vozdukh backup oxygen generator ( backup generator in teh Russian Module)
 

# input the Hole size (in square meters) Located at the Zvezda module in the Russian side of the international space station
hole_area = float(input("Enter the hole area (square meters): ")) 

# input the angle between the hole and the direction of the oxygen flow (in degrees)
theta = float(input("Enter the angle and  direction at which the  oxygen flow is escaping  (Degrees): ")) 

# Hole diameter
d = 2 *math.sqrt (hole_area *pi)

#Flow coefficient (a dimensionless value that depends on the gas mixture and the microgravity environment)
alfa = (1 / (1 + delta_P/ INITIAL_OXYGEN_PRESSURE ))*  (1 + (T_in - T_out) / T_in)

# Dimensionless Factorβ for correction factor of the flow direction/orientation (depends on the location and size of the hole )
if L == 0:
    Beta = 0
else:
    Beta = (1 / (1 + (d / L)**2)) * (1 + (theta/ 90)**2)


# Calculate the escape rate (assuming a simple orifice flow/ unifor flow) 
 #escape_rate = (hole_area * math.sqrt(2 * INITIAL_OXYGEN_PRESSURE / (OXYGEN_MOLECULAR_WEIGHT / (8.314 * TEMPERATURE)))) / 1000   # kg/s  IDEAL GAS EQUATION 

#calculate the escape rate (considering the flow is non-uniform)
#escape_rate = Cd * hole_area *math.sqrt(2 * (INITIAL_OXYGEN_PRESSURE / (8.314 / OXYGEN_MOLECULAR_WEIGHT * T_in)) * (INITIAL_OXYGEN_PRESSURE - EXTERNAL_PRESSURE)) / 1000   # kg/s    Adjusts for pressure variation
#escape_rate = Cd * hole_area *math.sqrt(2 * (INITIAL_OXYGEN_PRESSURE / (8.314 / OXYGEN_MOLECULAR_WEIGHT * T_in)) * (delta_P* (1 + (gamma - 1) / 2 * M**2)**(-1/(gamma - 1)))  / 1000   # kg/s     including Compressibility effects
#escape_rate = Cd * hole_area *math.sqrt(2 * (INITIAL_OXYGEN_PRESSURE / (8.314 / OXYGEN_MOLECULAR_WEIGHT * T_in)) * (delta_P* (1 + (gamma - 1) / 2 * M**2)**(-1/(gamma - 1)))  * (1 + alfa *  delta_P/ INITIAL_OXYGEN_PRESSURE)  / 1000   # kg/s   including Temperature gradients (only having into account an average temperature outside)
#escape_rate = Cd * hole_area * math.sqrt(2 * (INITIAL_OXYGEN_PRESSURE / (8.314 / OXYGEN_MOLECULAR_WEIGHT * T_in)) * (delta_P * (1 + (gamma - 1) / 2 * M**2)**(-1/(gamma - 1))) * (1 + alfa * delta_P / INITIAL_OXYGEN_PRESSURE) * (1 + Beta * (d / L) * (theta / 90))) / 1000  # kg/s including Hole location and Hole size 
escape_rate = Cd * hole_area * math.sqrt(2 * (INITIAL_OXYGEN_PRESSURE / (8.314 / OXYGEN_MOLECULAR_WEIGHT * T_in)) * (delta_P * (1 + (gamma - 1) / 2 * M**2)**(-1/(gamma - 1))) * (1 + alfa * delta_P / INITIAL_OXYGEN_PRESSURE) * (1 + Beta * (d / L) * (theta / 90))) * (1 - (OXYGEN_DINAMIC_VISCOSITY * airflow_velocity) / (OXYGEN_DENSITY * delta_P * d))/ 1000  # kg/s including dynamic viscosity as a COMPRESSIBLE FLOW


# escape rate in terms of kg/day
escape_rate_day = escape_rate * 86400   #kg/day

# input the number of crew members
crew_size = int(input("Enter the number of crew members: "))

# Calculate oxygen duration (How long will last the oxygen inside the International Space Station)
hours,minutes = calculate_oxygen_duration (initial_backup_oxygen_supply ,crew_size, second_backup_supply,second_backup_num_tanks, escape_rate_day)

print(f"With {crew_size} crew members, the back-up oxygen will last approximately {hours} hours and {minutes} minutes.")
print(" Oxygen level/Oxygen Generator Failure")
print("CRITICAL: Oxygen levels have reached zero. Crew members are in danger.")

# Create a plot of oxygen consumption in the ISS over time
time_array = np.arange(0, hours+1, 1)
oxygen_level_array = initial_backup_oxygen_supply + (second_backup_num_tanks * second_backup_supply) - (0.84 * crew_size + escape_rate_day / 86400) * time_array

plt.plot(time_array, oxygen_level_array)
plt.xlabel('Time (hours)')
plt.ylabel('Oxygen Level (kg)')
plt.title('Oxygen Generator Failure')
plt.grid(True)
plt.show()