# This code is based on https://github.com/ControlEverythingCommunity/SI7020-A20/blob/master/python/SI7020_A20.py
# For device specs, go to: https://s3.amazonaws.com/controleverything.media/controleverything/Production%20Run%205/12_SI7020-A20_I2CS/Datasheets/Si7020-A20.pdf
# It is designed to work with the SI7020-A20 and the Onion Omega 2 plus
# Note that you may need to install an other I2C implementation for the Onion Omega 2 plus, since the original did not see my temperature/humidity sensor

from OmegaExpansion import onionI2C
import time
import sys

# Get I2C bus
i2c = onionI2C.OnionI2C(1)

# ------ Humidity measurement ------ #

# SI7020_A20 address, 0x40(64)
#		0xF5(245)	Select Relative Humidity NO HOLD MASTER mode
i2c.write(0x40, [0xF5])

time.sleep(0.5)

# SI7020_A20 address, 0x40(64)
# Read data back, 2 bytes, Humidity MSB first
data = i2c.read(0x40, 2)

# Convert the data
humidity = (125.0 * (data[0] * 256.0 + data[1]) / 65536.0) - 6.0

# ------ Temperature measurement ------ #

# SI7020_A20 address, 0x40(64)
#		0xF3(243)	Select temperature NO HOLD MASTER mode
i2c.write(0x40, [0xF3])

time.sleep(0.5)

# SI7020_A20 address, 0x40(64)
# Read data back, 2 bytes, Temperature MSB first
data = i2c.read(0x40, 2)

# Convert the data
cTemp = (175.72 * (data[0] * 256.0 + data[1]) / 65536.0) - 46.85
fTemp = cTemp * 1.8 + 32

# ------ Output the data ------ #

# Output data to screen
print "Relative Humidity is : %.2f %%RH" %humidity
print "Temperature in Celsius is : %.2f C" %cTemp
print "Temperature in Fahrenheit is : %.2f F" %fTemp
