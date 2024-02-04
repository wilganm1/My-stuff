''' I want to make an AI program in the future that can take stored data
directly from the computer I'm on and parse information from it. It can
be a text file, .py file, or whatever'''

# For this I want to make a dictionary for each element on the periodic table

Hydrogen = {
    "appearance": "colorless gas",
    "atomic number": 1,
    "symbol": "H",
    "atomic weight": 63.546,
    "group": 11,
    "period": 1,
    "block": "s",
    "shells": 1,
    "electrons per shell": [1],
    "valence electrons": 1,
    "phase": "gas",
    "melting point (°F)": -434.49,
    "boiling ponit (°F)": -423.182,
    "density (g/L)": 0.08988,
    "liquid density (g/cm^3)": 0.07,
    "triple point": {
        "Kelvin": 13.8033,
        "kPa": 7.041},
    "criical point": {
        "Kelvin": 32.938,
        "MPa": 1.2858},
    "heat of fusion (H2)(kJ/mol)": 0.117,
    "heat of vaporization (H2)(kJ/mol)": 0.9047,
    "molar heat capacity (J/(mol*K)": 28.836,
    "vapor pressure": {
        "pressure (Pa)": [10000, 100000],
        "temperature (kelvin)": [15, 20]},
    "oxidation states": [-1, 0, 1],
    "electronegativity (Pauling scale)": 2.20,
    "ionization energies (kJ/mol)": [1312.0],
    "covalent radius (pm)": 31,
    "Van der Waals radius (pm)": 120,
    "thermal conductivity (W/(m⋅K))": 0.1805,
    "magnetic ordering": "diamagnetic",
    "molar magnetic susceptibility (cm^3/mol)": -3.98 * 10**-6}

Helium = {
    "appearance": "colorless gas",
    "atomic number": 2,
    "symbol": He,
    "atomic weight": 4.002602,
    "group": 18,
    "period": 1,
    "block": "s",
    "shells": 1,
    "electrons per shell": [2],
    "valence electrons": 2,
    "phase": "gas",
    "melting point (°F)": -457.96,
    "boiling ponit (°F)": -452.070,
    "density (g/L)": 0.1786,
    "liquid density": {
        "at melting point (g/cm^3)": 0.145,
        "at boiling point (g/cm^3)": 0.125},
    "triple point" : {
        "temperature (kelvin)": 2.177,
        "Pressure (kPa)": 5.043},
    "critical point": {
        "Temperature (Kelvin)": 5.1953,
        "Pressure (MPa)": 0.22746},
    "heat of fusion (kJ/mol)": 0.0138,
    "heat of vaporization (kJ/mol)": 0.0829,
    "molar heat capacity (J/(mol*K)": 20.78,
    "vapor pressure": {
        "pressure (Pa)": [100, 1000, 10000, 100000],
        "temperature (kelvin)": [1.23, 1.67, 2.48, 4.21]},
    "oxidation states": [0],
    "ionization energies (kJ/mol)": [2372.3, 5250.5],
    "covalent radius (pm)": 28,
    "Van der Waals radius (pm)": 140,
    "thermal conductivity (W/(m⋅K))": 0.1513,
    "magnetic ordering": "diamagnetic",
    "molar magnetic susceptibility (cm^3/mol)": -1.88 * 10**-6}

Lithium = {
    "appearance": "silvery-white",
    "atomic number": 3,
    "symbol": Li,
    "atomic weight": 6.94,
    "group": 1,
    "period": 2,
    "block": "s",
    "shells": 2,
    "electrons per shell": [2,1],
    "valence electrons": 1,
    "phase": "solid",
    "melting point (°F)": 356.90,
    "boiling ponit (°F)": 2426,
    "density (g/cm^3)": 0.534,
    "liquid density (at melting point) (g/cm^3)": 0.512,
    "critical point": {
        "Temperature (Kelvin)": 3220,
        "Pressure (MPa)": 67},
    "heat of fusion (kJ/mol)": 3,
    "heat of vaporization (kJ/mol)": 135,
    "molar heat capacity (J/(mol*K)": 24.860,
    "vapor pressure": {
        "pressure (Pa)": [1, 10, 100, 1000, 10000, 100000],
        "temperature (kelvin)": [797, 885, 995, 1144, 1337, 1610]},
    "oxidation states": [0, 1],
    "electronegativity (Pauling scale)": 0.98,
    "ionization energies (kJ/mol)": [520.2, 7298.8, 11815.0],
    "atomic radius (pm)": 152,
    "covalent radius (pm)": 128,
    "Van der Waals radius (pm)": 182,
    "thermal expansion (µm/(m⋅K) (at 25 °C))": 46, 
    "thermal conductivity (W/(m⋅K))": 84.8,
    "magnetic ordering": "paramagnetic",
    "molar magnetic susceptibility (cm^3/mol)": 14.2 * 10**-6,
    "Young's modulus (GPa)": 4.9,
    "shear modulus (GPa)": 4.2,
    "bulk modulus (GPa)": 11,
    "mohs hardness": 0.6,
    "brinell hardness (MPa)": 5,
    }

Beryllium = {
    "appearance": "white-gray metallic",
    "atomic number": 4,
    "symbol": "Be",
    "atomic weight": 9.0121831,
    "group": 2,
    "period": 2,
    "block": "s",
    "shells": 2,
    "electrons per shell": [2,2],
    "valence electrons": 2,
    "phase": "solid",
    "melting point (°F)": 2349,
    "boiling ponit (°F)": 4476,
    "density (g/cm^3": 1.85,
    "liquid density (at melting point) (g/cm^3)": 1.690,
    "critical point": {
        "Temperature (Kelvin)": 5205,
        "Pressure (MPa)": 1},
    "heat of fusion (kJ/mol)": 12.2,
    "heat of vaporization (kJ/mol)": 292,
    "molar heat capacity (J/(mol*K)": 16.443,
    "vapor pressure": {
        "pressure (Pa)": [1, 10, 100, 1000, 10000, 100000],
        "temperature (kelvin)": [1462, 1608, 1791, 2023, 2327, 2742]},
    "oxidation states": [0, 1, 2],
    "electronegativity (Pauling scale)": 1.57,
    "ionization energies (kJ/mol)": [899.5, 1757.1, 14848],
    "atomic radius (pm)": 112,
    "covalent radius (pm)": 96,
    "Van der Waals radius (pm)": 153,
    "thermal expansion (µm/(m⋅K) (at 25 °C))": 11.3,
    "thermal conductivity (W/(m⋅K))": 200,
    "electrical resistivity ( nΩ⋅m (at 20 °C)": 36,
    "magnetic ordering": "diamagnetic",
    "molar magnetic susceptibility (cm^3/mol)": -9 * 10**-6,
    "Young's modulus (GPa)": 287,
    "shear modulus (GPa)": 132,
    "bulk modulus (GPa)": 130,
    "poisson ratio": 0.032,
    "mohs hardness": 5.5,
    "vickers hardness (MPa)": 1670,
    "brinell hardness (MPa)": 1000}

Boron = {
    "appearance": "black-brown",
    "atomic number": 5,
    "symbol": "B",
    "atomic weight": 10.806,
    "group": 13,
    "period": 2,
    "block": "p",
    "shells": 2,
    "electrons per shell": [2,3],
    "valence electrons": 3,
    "phase": "solid",
    "melting point":{
        "°F": 3769,
        "°C": 2076,
        "Kelvin": 2349},        
    "boiling ponit": {
        "°F": 7101,
        "°C": 3927,
        "Kelvin": 4200},
    "density (g/cm^3)": 2.08,
    "heat of fusion (kJ/mol)": 50.2,
    "heat of vaporization (kJ/mol)": 508,
    "molar heat capacity (J/(mol*K)": 11.087,
    "vapor pressure": {
        "pressure (Pa)": [1, 10, 100, 1000, 10000, 100000],
        "temperature (kelvin)": [2348, 2562, 2822, 3141, 3545, 4071]},
    "oxidation states": [-5, -1, 0, 1, 2, 3],
    "electronegativity (Pauling scale)": 2.04, 
    "ionization energies (kJ/mol)": [800.6, 2427.1, 3659.7],
    "atomic radius (pm)": 90,
    "covalent radius (pm)": 84,
    "Van der Waals radius (pm)": 192,
    "thermal expansion (µm/(m⋅K) (at 25 °C))": 6,
    "thermal conductivity (W/(m⋅K))": 27.4,
    "electrical resistivity (Ω⋅m (at 20 °C))": 10**6,
    "magnetic ordering": "diamagnetic",
    "molar magnetic susceptibility (cm^3/mol)": -6.7 * 10**-6,
    "mohs hardness": 9.5,
    }

Carbon = {
    "appearance": "graphite: black, metallic-looking",
    "atomic number": 6,
    "symbol": "C",
    "atomic weight": 12.0096,
    "group": 14,
    "period": 2,
    "block": "p",
    "shells": 2,
    "electrons per shell": [2,4],
    "valence electrons": 4,
    "phase": "solid",
    "sublimation point": {
        "°F": 6588,
        "°C": 3642,
        "Kelvin": 3915},       
    "density (g/cm^3)": {
        "graphite": 2.266,
        "diamond": 3.515,
        "amorphous": 2.0},
    "triple point" : {
        "Temperature (Kelvin)": 4600,
        "Pressure (kPa)": 10800},
    "heat of fusion (kJ/mol)": 117,
    "molar heat capacity (J/(mol*K)": {
        "graphite": 8.517,
        "diamond": 6.155},
    "oxidation states": [-4,-3,-2,-1,0,1,2,3,4],
    "electronegativity (Pauling scale)": 2.55,
    "ionization energies (kJ/mol)": [1086.5, 2352.6, 4620.5],
    "covalent radius (pm)": [69, 73, 77],
    "Van der Waals radius (pm)": 170,
    "thermal expansion (µm/(m⋅K) (at 25 °C))": 0.8,
    "thermal conductivity (W/(m⋅K))": {
        "graphite": [140, 165],
        "diamond": [900, 2300]},
    "electrical resistivity (µΩ*m)": 7.837, 
    "magnetic ordering": "diamagnetic",
    "molar magnetic susceptibility (cm^3/mol)": -5.9*10**-6,
    "Young's modulus (GPa)": 1050,
    "shear modulus (GPa)": 478,
    "bulk modulus (GPa)": 442,
    "poisson ratio": 0.1,
    "mohs hardness": {
        "graphite": 1.5,
        "diamond": 10},
    }

Nitrogen = {
    "appearance": "colorless",
    "atomic number": 7,
    "symbol": "N",
    "atomic weight": 14.00643,
    "group": 15,
    "period": 2,
    "block": "p",
    "shells": 2,
    "electrons per shell": [2, 5],
    "valence electrons": 5,
    "phase": "gas",
    "melting point":{
        "Fahrenheit": -345.75,
        "Celsius": -209.86,
        "Kelvin": 63.23},        
    "boiling ponit": {
        "Fahrenheit": -320.431,
        "Celsius": -195.795,
        "Kelvin": 77.355},
    "density (g/L)": 1.2506,
    "liquid density": {
        "at boiling point (g/cm^3)": .808},
    "triple point" : {
        "Temperature (Kelvin)": 63.151,
        "Pressure (kPa)": 12.52},
    "critical point": {
        "Temperature (Kelvin)": 126.21,
        "Pressure (MPa)": 3.39},
    "heat of fusion (kJ/mol)": 0.72,
    "heat of vaporization (kJ/mol)": 5.57,
    "molar heat capacity (J/(mol*K)": 29.124,
    "vapor pressure": {
        "pressure (Pa)": [1, 10, 100, 1000, 10000, 100000],
        "temperature (kelvin)": [37, 41, 46, 53, 62, 77]},
    "oxidation states": [-3, -2.-1.0,1,2,3,4,5],
    "electronegativity (Pauling scale)": 3.04,
    "ionization energies (kJ/mol)": [1402.3, 2856, 4578.1],
    "covalent radius (pm)": 71,
    "Van der Waals radius (pm)": 155,
    "thermal conductivity (W/(m⋅K))": 25.83 * 10**-3,
    "magnetic ordering": "diamagnetic",
    }

Oxygen = {
    "appearance": "colorless gas. pale blue solid & liquid",
    "atomic number": 8,
    "symbol": "O",
    "atomic weight": 15.99903,
    "group": 16,
    "period": 2,
    "block": "p",
    "shells": 2,
    "electrons per shell": [2,6],
    "valence electrons": 6,
    "phase": "gas",
    "melting point":{
        "Fahrenheit": -361.82,
        "Celsius": -218.79,
        "Kelvin": 54.36},        
    "boiling ponit": {
        "Fahrenheit": -297.332,
        "Celsius": -182.962,
        "Kelvin": 90.188},
    "density (g/L)": 1.429,
    "liquid density": {
        "at boiling point (g/cm^3)": 1.141},
    "triple point" : {
        "Temperature (Kelvin)": 54.361,
        "Pressure (kPa)": 0.1463},
    "critical point": {
        "Temperature (Kelvin)": 154.581,
        "Pressure (MPa)": 5.043},
    "heat of fusion (kJ/mol)": 0.444,
    "heat of vaporization (kJ/mol)": 0.682,
    "molar heat capacity (J/(mol*K)": 29.378,
    "vapor pressure": {
        "pressure (Pa)": [1000, 10000, 100000],
        "temperature (kelvin)": [61, 73, 90]},
    "oxidation states": [-2,-1,0,1,2],
    "electronegativity (Pauling scale)": 3.44, 
    "ionization energies (kJ/mol)": [1313.9, 3388.3, 5300.5],
    "covalent radius (pm)": 66,
    "Van der Waals radius (pm)": 152,
    "thermal conductivity (W/(m⋅K))": 26.58*10**-3,
    "magnetic ordering": "paramagnetic",
    "molar magnetic susceptibility (cm^3/mol)": 3.449 *10**-3,
    }

Fluorine = {
    "appearance": "pale yellow gas, bright yellow liquid",
    "atomic number": 9,
    "symbol": "F",
    "atomic weight": 18.998403162,
    "group": 17,
    "period": 2,
    "block": "p",
    "shells": 2,
    "electrons per shell": [2,7],
    "valence electrons": 7,
    "phase": "gas",
    "melting point":{
        "Fahrenheit": -363.41,
        "Celsius": -219.67,
        "Kelvin": 53.48},        
    "boiling ponit": {
        "Fahrenheit": -306.60,
        "Celsius": -188.11,
        "Kelvin": 85.03},
    "density (g/L)": 1.696,
    "liquid density": {
        "at boiling point (g/cm^3)": 1.505},
    "triple point" : {
        "Temperature (Kelvin)": 53.48,
        "Pressure (kPa)": .252},
    "critical point": {
        "Temperature (Kelvin)": 144.41,
        "Pressure (MPa)": 5.1724},
    "heat of vaporization (kJ/mol)": 6.51,
    "molar heat capacity (J/(mol*K)": 31,
    "vapor pressure": {
        "pressure (Pa)": [1, 10, 100, 1000, 10000, 100000],
        "temperature (kelvin)": [38,44,50,58,69,85]},
    "oxidation states": [-1,0],
    "electronegativity (Pauling scale)": 3.98, 
    "ionization energies (kJ/mol)": [1681,3374,6147],
    "covalent radius (pm)": 64,
    "Van der Waals radius (pm)": 135,
    "thermal conductivity (W/(m⋅K))": 0.02591,
    "magnetic ordering": "diamagnetic",
    }

Neon = {
    "appearance": "colorless gas",
    "atomic number": 10,
    "symbol": "Ne",
    "atomic weight": 20.1797,
    "group": 18,
    "period": 2,
    "block": "p",
    "shells": 2,
    "electrons per shell": [2,8],
    "valence electrons": 8,
    "phase": "gas",
    "melting point":{
        "Fahrenheit": -415.46,
        "Celsius": -248.59,
        "Kelvin": 24.56},        
    "boiling ponit": {
        "Fahrenheit": -410.883,
        "Celsius": -246.046,
        "Kelvin": 27.104},
    "density (g/L)": 0.9002,
    "liquid density": {
        "at boiling point (g/cm^3)": 1.207},
    "triple point" : {
        "Temperature (Kelvin)": 24.556,
        "Pressure (kPa)": 43.37},
    "critical point": {
        "Temperature (Kelvin)": 44.4918,
        "Pressure (MPa)": 2.7686},
    "heat of fusion (kJ/mol)": 0.335,
    "heat of vaporization (kJ/mol)": 1.71,
    "molar heat capacity (J/(mol*K)": 20.79,
    "vapor pressure": {
        "pressure (Pa)": [1,10,10,1000,10000,100000],
        "temperature (kelvin)": [12,13,15,18,21,27]},
    "oxidation states": [0],
    "ionization energies (kJ/mol)": [2080.7, 3952.3, 6122],
    "covalent radius (pm)": 58,
    "Van der Waals radius (pm)": 154,
    "thermal conductivity (W/(m⋅K))": 49.1*10**-3,
    "magnetic ordering": "diamagnetic",
    "molar magnetic susceptibility (cm^3/mol)": -6.74*10**-6,
    "bulk modulus (GPa)": 654,
    }

Sodium = {
    "appearance": "silvery white metallic",
    "atomic number": 11,
    "symbol": "Na",
    "atomic weight": 22.98976928,
    "group": 1,
    "period": 3,
    "block": "s",
    "shells": 3,
    "electrons per shell": [2,8,1],
    "valence electrons": 1,
    "phase": "solid",
    "melting point":{
        "Fahrenheit": 208.029,
        "Celsius": 97.794,
        "Kelvin": 370.944},        
    "boiling ponit": {
        "Fahrenheit": 1621.292,
        "Celsius": 882.940,
        "Kelvin": 1156.090},
    "density (g/L)": 0.968,
    "liquid density": {
        "at melting point (g/cm^3)": 0.927},
    "critical point": {
        "Temperature (Kelvin)": 2573,
        "Pressure (MPa)": 35},
    "heat of fusion (kJ/mol)": 2.60,
    "heat of vaporization (kJ/mol)": 97.42,
    "molar heat capacity (J/(mol*K)": 28.230,
    "vapor pressure": {
        "pressure (Pa)": [1,10,100,1000,10000,100000],
        "temperature (kelvin)": [554,617,697,802,946,1153]},
    "oxidation states": [-1,0,1],
    "electronegativity (Pauling scale)": 0.93, 
    "ionization energies (kJ/mol)": [495.8, 4562, 6910.3],
    "atomic radius": 186,
    "covalent radius (pm)": 166,
    "Van der Waals radius (pm)": 227,
    "thermal expansion (µm/(m⋅K) (at 25 °C)) ": 71,
    "thermal conductivity (W/(m⋅K))": 142,
    "electrical resistivity (nΩ⋅m (at 20 °C))": 47.7,
    "magnetic ordering": "paramagnetic",
    "molar magnetic susceptibility (cm^3/mol)": 16.0 * 10**-6,
    "Young's modulus (GPa)": 10,
    "shear modulus (GPa)": 3.3,
    "bulk modulus (GPa)": 6.3,
    "mohs hardness": 0.5,
    "brinell hardness (MPa)": 0.69,
    }

Magnesium = {
    "appearance": "shiny grey solid",
    "atomic number": 12,
    "symbol": "Mg",
    "atomic weight": 24.304,
    "group": 2,
    "period": 3,
    "block": "s",
    "shells": 3,
    "electrons per shell": [2,8,3],
    "valence electrons": 3,
    "phase": "solid",
    "melting point":{
        "Fahrenheit": 1202,
        "Celsius": 650,
        "Kelvin": 923},        
    "boiling ponit": {
        "Fahrenheit": 1994,
        "Celsius": 1091,
        "Kelvin": 1363},
    "density (g/cm^3)": 1.738,
    "liquid density": {
        "at melting point (g/cm^3)": 1.584},
    "heat of fusion (kJ/mol)": 8.48,
    "heat of vaporization (kJ/mol)": 128,
    "molar heat capacity (J/(mol*K)": 24.869,
    "vapor pressure": {
        "pressure (Pa)": [1,10,100,1000,10000,100000],
        "temperature (kelvin)": [701,773,861,971,1132,1361]},
    "oxidation states": [0,1,2],
    "electronegativity (Pauling scale)": 1.31,
    "ionization energies (kJ/mol)": [737.7,1450.7,7732.7],
    "atomic radus (pm)": 160,
    "covalent radius (pm)": 141,
    "Van der Waals radius (pm)": 173,
    "thermal expansion (µm/(m⋅K) (at 25 °C))": 24.8,
    "thermal conductivity (W/(m⋅K))": 156,
    "electrical resistivity (nΩ⋅m (at 20 °C))": 43.9,
    "magnetic ordering": "paramagnetic",
    "molar magnetic susceptibility (cm^3/mol)": 13.1*10**-6,
    "Young's modulus (GPa)": 45,
    "shear modulus (GPa)": 17,
    "bulk modulus (GPa)": 35.4,
    "poisson ratio": 0.290,
    "mohs hardness": 1.75,
    "brinell hardness (MPa)": 151,
    }

Aluminum = {
    "appearance": "silvery gray metallic",
    "atomic number": 13,
    "symbol": "Al",
    "atomic weight": 26.9815384,
    "group": 13,
    "period": 3,
    "block": "p",
    "shells": 3,
    "electrons per shell": [2,8,3],
    "valence electrons": 3,
    "phase": "solid",
    "melting point":{
        "Fahrenheit": 1220.58,
        "Celsius": 660.32,
        "Kelvin": 933.47},        
    "boiling ponit": {
        "Fahrenheit": 4478,
        "Celsius": 2470,
        "Kelvin": 2743},
    "density (g/cm^3)": 2.70,
    "liquid density": {
        "at melting point (g/cm^3)": 2.375},
    "heat of fusion (kJ/mol)": 10.71,
    "heat of vaporization (kJ/mol)": 284,
    "molar heat capacity (J/(mol*K)": 24.20,
    "vapor pressure": {
        "pressure (Pa)": [1,10,100,1000,10000,100000],
        "temperature (kelvin)": [1482,1632,1817,2054,2364,2790]},
    "oxidation states": [-2,-1,0,1,2,3],
    "electronegativity (Pauling scale)": 1.61, 
    "ionization energies (kJ/mol)": [577.5, 1816.7, 2744.8],
    "atomic radius (pm)": 143, 
    "covalent radius (pm)": 121,
    "Van der Waals radius (pm)": 184,
    "thermal expansion (µm/(m⋅K) (at 25 °C))": 23.1,
    "thermal conductivity (W/(m⋅K))": 237,
    "electrical resistivity (nΩ⋅m (at 20 °C))": 26.5,
    "magnetic ordering": "paramagnetic",
    "molar magnetic susceptibility (cm^3/mol)": 16.5*10**-6,
    "Young's modulus (GPa)": 70,
    "shear modulus (GPa)": 26,
    "bulk modulus (GPa)": 76,
    "poisson ratio": 0.35,
    "mohs hardness": 2.75,
    "vickers hardness (MPa)": 255,
    "brinell hardness (MPa)": 355
    }

Silicon = {
    "appearance": "crystalline, reflective",
    "atomic number": 14,
    "symbol": "Si",
    "atomic weight": 28.084,
    "group": 14,
    "period": 3,
    "block": "p",
    "shells": 3,
    "electrons per shell": [2,8,4],
    "valence electrons": 4,
    "phase": "solid",
    "melting point":{
        "Fahrenheit": 2577,
        "Celsius": 1414,
        "Kelvin": 1687},        
    "boiling ponit": {
        "Fahrenheit": 5909,
        "Celsius": 3265,
        "Kelvin": 3536},
    "density (g/cm^3)": 2.3290,
    "liquid density": {
        "at melting point (g/cm^3)": 2.57},
    "heat of fusion (kJ/mol)": 50.21,
    "heat of vaporization (kJ/mol)": 383,
    "molar heat capacity (J/(mol*K)": 19.789,
    "vapor pressure": {
        "pressure (Pa)": [1,10,100,1000,10000,100000],
        "temperature (kelvin)": [1908,2102,2339,2636,3021,3537]},
    "oxidation states": [-4,-3,-2,-1,0,1,2,3,4],
    "electronegativity (Pauling scale)": 1.90,
    "ionization energies (kJ/mol)": [786.5, 1577, 3231.6],
    "atomic radius (pm)": 111, 
    "covalent radius (pm)": 111,
    "Van der Waals radius (pm)": 210,
    "thermal expansion (µm/(m⋅K) (at 25 °C))": 2.6,
    "thermal conductivity (W/(m⋅K))": 149,
    "electrical resistivity (nΩ⋅m (at 20 °C))": 2.3*10**3,
    "band gap (eV at 300K)": 1.12,
    "magnetic ordering": "diamagnetic",
    "molar magnetic susceptibility (cm^3/mol)": -3.9*10**-6,
    "Young's modulus (GPa)": 159,
    "shear modulus (GPa)": 65,
    "bulk modulus (GPa)": 97.6,
    "poisson ratio": 0.012,
    "mohs hardness": 6.5,
    }

Phosphorus = {
    "appearance": "can be white, a waxy red & violet, or black metal",
    "atomic number": 15,
    "symbol": "P",
    "atomic weight": 30.973761998,
    "group": 15,
    "period": 3,
    "block": "p",
    "shells": 3,
    "electrons per shell": [2,8,5],
    "valence electrons": 5,
    "phase": "solid",
    "melting point":{
        "white": {
            "Fahrenheit": 111.5,
            "Celsius": 44.15,
            "Kelvin": 317.3},
        "red": {
            "Fahrenheit": 1090,
            "Celsius": 590,
            "Kelvin": 860}},
    "boiling ponit": {
        "white": {
            "Fahrenheit": 536.9,
            "Celsius": 280.5,
            "Kelvin": 553.7}},
    "sublimation point": {
        "red": {
            "Fahrenheit": 900,
            "Celsius": 506,
            "Kelvin":740},
        "violet": {
            "Fahrenheit": 1148,
            "Celsius": 620,
            "Kelvin": 893}},
    "density (g/cm^3)": {
        "white": 1.823,
        "red": 2.27,
        "violet": 2.36,
        "black": 2.69},
    "heat of fusion (kJ/mol)": {
        "white": 0.66},
    "heat of vaporization (kJ/mol)": {
        "white": 51.9},
    "molar heat capacity (J/(mol*K)": {
        "white": 23.824},
    "vapor pressure": {
        "white": {
            "pressure (Pa)": [1,10,100,1000,10000,100000],
            "temperature (kelvin)": [279,307,342,388,453,549]},
        "red": {
            "pressure (Pa)": [1,10,100,1000,10000,100000],
            "temperature (kelvin)": [455,489,529,576,635,704]}},
    "oxidation states": [-3,-2,-1,0,1,2,3,4,5],
    "electronegativity (Pauling scale)": 2.19,
    "ionization energies (kJ/mol)": [1011.8, 1907, 2914.1],
    "covalent radius (pm)": 107,
    "Van der Waals radius (pm)": 180,
    "thermal conductivity (W/(m⋅K))": {
        "white": 0.236,
        "black": 12.1},
    "magnetic ordering": "diamagnetic",
    "molar magnetic susceptibility (cm^3/mol)": -20.8*10**-6,
    "bulk modulus (GPa)": {
        "white": 5,
        "red": 11},
    }

Sulfur = {
    "appearance": "Lemon yellow sintered microcrystals",
    "atomic number": 16,
    "symbol": "S",
    "atomic weight": 32.059,
    "group": 16,
    "period": 3,
    "block": "p",
    "shells": 3,
    "electrons per shell": [2,8,6],
    "valence electrons": 6,
    "phase": "solid",
    "melting point":{
        "Fahrenheit": 239.38,
        "Celsius": 115.21,
        "Kelvin": 388.36},        
    "boiling ponit": {
        "Fahrenheit": 832.3,
        "Celsius": 444.6,
        "Kelvin": 717.8},
    "density (g/cm^3)": {
        "alpha": 2.07,
        "beta": 1.96,
        "gamma": 1.92},
    "liquid density": {
        "at melting point (g/cm^3)": 1.819},
    "critical point": {
        "Temperature (Kelvin)": 1314,
        "Pressure (MPa)": 20.7},
    "heat of fusion (kJ/mol)": 1.727,
    "heat of vaporization (kJ/mol)": 45,
    "molar heat capacity (J/(mol*K)": 22.75,
    "vapor pressure": {
        "pressure (Pa)": [1,10,100,1000,10000,100000],
        "temperature (kelvin)": [375,408,449,508,591,717]},
    "oxidation states": [-2,-1,0,1,2,3,4,5,6],
    "electronegativity (Pauling scale)": 2.58,
    "ionization energies (kJ/mol)": [999.6, 2252,3357],
    "covalent radius (pm)": 105,
    "Van der Waals radius (pm)": 180,
    "thermal conductivity (W/(m⋅K))": 0.205,
    "electrical resistivity (nΩ⋅m (at 20 °C))": 2*10**15,
    "magnetic ordering": "diamagnetic",
    "molar magnetic susceptibility (cm^3/mol)": -15.5*10**-6,
    "bulk modulus (GPa)": 7.7,
    "mohs hardness": 2.0,
    }

Chlorine = {
    "appearance": "pale yellow-green",
    "atomic number": 17,
    "symbol": "Cl",
    "atomic weight": 35.446,
    "group": 17,
    "period": 3,
    "block": "p",
    "shells": 3,
    "electrons per shell": [2,8,7],
    "valence electrons": 7,
    "phase": "gas",
    "melting point":{
        "Fahrenheit": -1507,
        "Celsius": -101.5,
        "Kelvin": 171.6},        
    "boiling ponit": {
        "Fahrenheit": -29.27,
        "Celsius": -34.04,
        "Kelvin": 239.11},
    "density (g/L)": 3.2,
    "liquid density": {
        "at boiling point (g/cm^3)": 1.5625},
    "critical point": {
        "Temperature (Kelvin)": 416.9,
        "Pressure (MPa)": 7.991},
    "heat of fusion (kJ/mol)": 6.406,
    "heat of vaporization (kJ/mol)": 20.41,
    "molar heat capacity (J/(mol*K)": 33.949,
    "vapor pressure": {
        "pressure (Pa)": [1,10,100,1000,10000,100000],
        "temperature (kelvin)": [128,139,153,170,197,239]},
    "oxidation states": [-1,0,1,2,3,4,5,6,7],
    "electronegativity (Pauling scale)": 3.16,
    "ionization energies (kJ/mol)": [1251.2, 2298, 3822],
    "covalent radius (pm)": 102,
    "Van der Waals radius (pm)": 175,
    "thermal conductivity (W/(m⋅K))": 8.9*10**-3,
    "electrical resistivity (nΩ⋅m (at 20 °C))": 11,
    "magnetic ordering": "diamagnetic",
    "molar magnetic susceptibility (cm^3/mol)": -40.5*10**-6,
    }

Argon = {
    "appearance": "colorless",
    "atomic number": 18,
    "symbol": "Ar",
    "atomic weight": 39.792,
    "group": 18,
    "period": 3,
    "block": "p",
    "shells": 3,
    "electrons per shell": [2,8,8],
    "valence electrons": 8,
    "phase": "gas",
    "melting point":{
        "Fahrenheit": -308.81,
        "Celsius": -189.34,
        "Kelvin": 83.81},        
    "boiling ponit": {
        "Fahrenheit": -302.526,
        "Celsius": -185.848,
        "Kelvin": 87.302},
    "density (g/L)": 1.784,
    "liquid density": {
        "at boiling point (g/cm^3)": 1.3954},
    "triple point" : {
        "Temperature (Kelvin)": 83.8058,
        "Pressure (kPa)": 68.89},
    "critical point": {
        "Temperature (Kelvin)": 150.687,
        "Pressure (MPa)": 4.863},
    "heat of fusion (kJ/mol)": 1.18,
    "heat of vaporization (kJ/mol)": 6.53,
    "molar heat capacity (J/(mol*K)": 20.85,
    "vapor pressure": {
        "pressure (Pa)": [10,100,1000,10000,100000],
        "temperature (kelvin)": [47,53,61,71,87]},
    "oxidation states": [0],
    "ionization energies (kJ/mol)": [1520.6, 2665.8,3931],
    "covalent radius (pm)": 106,
    "Van der Waals radius (pm)": 188,
    "thermal conductivity (W/(m⋅K))": 17.72*10**-3,
    "magnetic ordering": "diamagnetic",
    "molar magnetic susceptibility (cm^3/mol)": -19.6*10**-6,
    }

Potassium = {
    "appearance": "silvery white, purple hue exposed to air",
    "atomic number": 19,
    "symbol": "K",
    "atomic weight": 39.0983,
    "group": 1,
    "period":4 ,
    "block": "s",
    "shells": 4,
    "electrons per shell": [2,8,8,1],
    "valence electrons": 1,
    "phase": "solid",
    "melting point":{
        "Fahrenheit": 146.3,
        "Celsius": 63.5,
        "Kelvin": 336.7},        
    "boiling ponit": {
        "Fahrenheit": 1395.75,
        "Celsius": 757.643,
        "Kelvin": 1030.793},
    "density (g/cm^3)": 0.8590,
    "liquid density": {
        "at melting point (g/cm^3)": 0.82948},
    "critical point": {
        "Temperature (Kelvin)": 2223,
        "Pressure (MPa)": 16},
    "heat of fusion (kJ/mol)": 2.33,
    "heat of vaporization (kJ/mol)": 76.9,
    "molar heat capacity (J/(mol*K)": 29.6,
    "oxidation states": [-1,1],
    "electronegativity (Pauling scale)": 0.82, 
    "ionization energies (kJ/mol)": [418.8, 3052,4420],
    "atomic radius": 227,
    "covalent radius (pm)": 203,
    "Van der Waals radius (pm)": 275,
    "thermal expansion (µm/(m⋅K) (at 25 °C))": 83.3,
    "thermal conductivity (W/(m⋅K))": 102.5,
    "electrical resistivity (nΩ⋅m (at 20 °C))": 72,
    "magnetic ordering": "paramagnetic",
    "molar magnetic susceptibility (cm^3/mol)": 20.8*10**-6,
    "Young's modulus (GPa)": 3.53,
    "shear modulus (GPa)": 1.3,
    "bulk modulus (GPa)": 3.1,
    "mohs hardness": 0.4,
    "brinell hardness (MPa)": 0.363,
    }

Calcium = {
    "appearance": "dull gray, silver with yellow tint",
    "atomic number": 20,
    "symbol": "Ca",
    "atomic weight": 40.078,
    "group": 2,
    "period": 4,
    "block": "s",
    "shells": 4,
    "electrons per shell": [2,8,8,2],
    "valence electrons": 2,
    "phase": "solid",
    "melting point":{
        "Fahrenheit": 1548,
        "Celsius": 842,
        "Kelvin": 1115},        
    "boiling ponit": {
        "Fahrenheit": 2703,
        "Celsius": 1484,
        "Kelvin": 1757},
    "density (g/cm^3)": 1.55,
    "liquid density": {
        "at melting point (g/cm^3)": 1.378},
    "heat of fusion (kJ/mol)": 8.54,
    "heat of vaporization (kJ/mol)": 154.7,
    "molar heat capacity (J/(mol*K)": 25.929,
    "vapor pressure": {
        "pressure (Pa)": [1,10,100,1000,10000,100000],
        "temperature (kelvin)": [864,956,1071,1227,1443,1755]},
    "oxidation states": [1,2],
    "electronegativity (Pauling scale)": 1.00,
    "ionization energies (kJ/mol)": [589.8,1145.4,4912.4],
    "atomic radius": 197,
    "covalent radius (pm)": 176,
    "Van der Waals radius (pm)": 231,
    "thermal expansion (µm/(m⋅K) (at 25 °C))": 22.3,
    "thermal conductivity (W/(m⋅K))": 201,
    "electrical resistivity (nΩ⋅m (at 20 °C))": 33.6,
    "magnetic ordering": "diamagnetic",
    "molar magnetic susceptibility (cm^3/mol)": 40*10**-6,
    "Young's modulus (GPa)": 20,
    "shear modulus (GPa)": 7.4,
    "bulk modulus (GPa)": 17,
    "poisson ratio": 0.31,
    "mohs hardness": 1.75,
    "brinell hardness (MPa)": 293,
    }

Helium = {
    "appearance": "",
    "atomic number": ,
    "symbol": "",
    "atomic weight": ,
    "group": ,
    "period": ,
    "block": "",
    "shells": ,
    "electrons per shell": [],
    "valence electrons": ,
    "phase": "",
    "melting point":{
        "Fahrenheit": ,
        "Celsius": ,
        "Kelvin": },        
    "boiling ponit": {
        "Fahrenheit": ,
        "Celsius": ,
        "Kelvin": },
    "density (g/L)": ,
    "liquid density": {
        "at melting point (g/cm^3)": ,
        "at boiling point (g/cm^3)": },
    "triple point" : {
        "Temperature (Kelvin)": ,
        "Pressure (kPa)": },
    "critical point": {
        "Temperature (Kelvin)": ,
        "Pressure (MPa)": },
    "heat of fusion (kJ/mol)": ,
    "heat of vaporization (kJ/mol)": ,
    "molar heat capacity (J/(mol*K)": ,
    "vapor pressure": {
        "pressure (Pa)": [],
        "temperature (kelvin)": []},
    "oxidation states": [],
    "electronegativity (Pauling scale)": 
    "ionization energies (kJ/mol)": [],
    "covalent radius (pm)": ,
    "Van der Waals radius (pm)": ,
    "thermal conductivity (W/(m⋅K))": ,
    "electrical resistivity (nΩ⋅m (at 20 °C))": ,
    "magnetic ordering": "diamagnetic",
    "molar magnetic susceptibility (cm^3/mol)": ,
    "Young's modulus (GPa)": ,
    "shear modulus (GPa)": ,
    "bulk modulus (GPa)": ,
    "poisson ratio": ,
    "mohs hardness": ,
    "vickers hardness (MPa)": ,
    "brinell hardness (MPa)": ,
    }



