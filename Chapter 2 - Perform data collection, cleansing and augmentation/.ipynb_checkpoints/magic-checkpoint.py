# This script downloads and plots monthly mean co2 values from https://datahub.io/core/co2-ppm#data

import pandas as pd
import matplotlib.pyplot as plt
import requests
import io

# Basic plotting
print("Performing super difficult data analysis..........")

url="https://datahub.io/core/co2-ppm/r/co2-mm-mlo.csv"
s=requests.get(url).content
carbon_dioxide=pd.read_csv(io.StringIO(s.decode('utf-8')))

#carbon_dioxide = pd.read_csv('https://datahub.io/core/co2-ppm/r/co2-mm-mlo.csv')
plt.plot(carbon_dioxide['Date'],carbon_dioxide['Average'])
plt.xlabel('Time')
plt.ylabel('CO2 concentration in ppm')
plt.show()
