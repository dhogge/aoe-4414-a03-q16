# sez_to_ecef.py
#
# Usage: python3 script_name.py arg1 arg2 ...
# Text explaining script usage
# Parameters:

# ...
# Output:
# ecef x y z coords
#
# Written by Dylan Hogge
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
# import Python modules

# e.g., import math # math module
import sys # argv
import math
#import numpy as np

# "constants"
# e.g., R_E_KM = 6378.137

R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions

## calculated denominator
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))


# initialize script arguments
if len(sys.argv)==7:
    o_lat_deg = float(sys.argv[1])
    o_lon_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])
    s_km = float(sys.argv[4])
    e_km = float(sys.argv[5])
    z_km = float(sys.argv[6])
else:
    print(\
    'Usage: '\
    'python3 sez_to_ecef.py r_x_km r_y_km r_z_km'\
    )
    exit

# write script below this line
lat_rad = o_lat_deg * math.pi/180
lon_rad = o_lon_deg * math.pi/180

ry_ecef_x = math.sin(lat_rad)*s_km + z_km*math.cos(lat_rad)
ry_ecef_y = e_km
ry_ecef_z = z_km*math.sin(lat_rad) - s_km * math.cos(lat_rad)

r_ecef_x = ry_ecef_x * math.cos(lon_rad) - ry_ecef_y * math.sin(lon_rad)
r_ecef_y = ry_ecef_x * math.sin(lon_rad) + ry_ecef_y * math.cos(lon_rad)
r_ecef_z = ry_ecef_z

denom = calc_denom(E_E, lat_rad)
C_E = R_E_KM / denom
S_E = (R_E_KM * (1-E_E**2))/denom
r_x = (C_E + hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y = (C_E + hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z = (S_E + hae_km)*math.sin(lat_rad)

ecef_x_km = r_ecef_x + r_x
ecef_y_km = r_ecef_y + r_y
ecef_z_km = r_ecef_z + r_z

print((round(ecef_x_km, 3)))
print((round(ecef_y_km, 3)))
print((round(ecef_z_km, 3)))
