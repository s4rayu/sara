# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    },
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.

def print_star_names(targets_dict):
	print("Star Names:")
	for target_name in targets_dict:
		print(target_name)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.

def print_stars_spectal_type(target_dict):
	print("Stars and spectral types:")
	for target_name, target_data in target_dict.items():
		print(f"{target_name}: {target_data['Spectral Type']}")

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.

def find_bright(targets_dict):
    print("\nTargets brighter than 0.1 magnitude:")
    for target_name, target_data in targets_dict.items():
        if target_data['Magnitude'] < 0.1: 
            print(f"{target_name}: {target_data['Magnitude']}")

# 4) Look up another target, add all the necessary information to the targets list. 
def add_new_target():
	targets["Arcturus"] = {
		"RA": "14h 15m 39.7s",
        "Dec": "+19° 10′ 57″",
        "Magnitude": -0.05,
        "Spectral Type": "K1.5III"
    }
     
	

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def find_brightest(targets_dict):
    def parse_declination(dec_string):
        try:
            degrees_part = dec_string.split('°')[0]
            return float(degrees_part)
        except:
            return None
    
    brightest_star = None
    brightest_magnitude = float('inf')
    
    for target_name, target_data in targets_dict.items():
        dec = parse_declination(target_data['Dec'])
        if dec is not None:
            distance_from_20 = abs(dec - 20)
            if distance_from_20 < 30 and target_data['Magnitude'] < brightest_magnitude:
                brightest_star = target_name
                brightest_magnitude = target_data['Magnitude']
    
    if brightest_star:
        star_data = targets_dict[brightest_star]
        print(f"Brightest star near +20°: {brightest_star}")
        print(f"Declination: {star_data['Dec']}")
        print(f"Magnitude: {star_data['Magnitude']}")
        return brightest_star
    else:
        print("No suitable star found near +20° declination.")
        return None
    

print_star_names(targets)
print_stars_spectal_type(targets)
find_bright(targets)
add_new_target()
# print(targets)
find_brightest(targets)

# 6) What is your favorite constellation?
print("Andromeda!")




