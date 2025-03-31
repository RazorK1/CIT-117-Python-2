#  Kyle Harris
#  CIT-117/117L Python
#  Inter Planetary Weights (2nd edition) Using Dictionaries and Pickling

def main(): ###################### Start of Main Function
    conversion_factors = {     ########## Solar System Conversion factors
        'Mercury': 0.38,
        'Venus': 0.91,
        'Moon': 0.165,
        'Mars': 0.38,
        'Jupiter': 2.34,
        'Saturn': 0.93,
        'Uranus': 0.92,
        'Neptune': 1.12,
        'Pluto': 0.066
    }
    
    import pickle ############ Get that pickle
    
    try:
        with open('bcPlanetaryWeights.db', 'rb') as file: ##################### looks for 'bcPlanetaryWeights.db'
            dictPlanetHistory = pickle.load(file)  ############# Pickle finder
    except FileNotFoundError:
        dictPlanetHistory = {}
    
    view_history = input("Do you want to see the history? (y/n): ").lower() ############### Desire to open up "bcPlanetaryWeights.db"
    if view_history == 'y': ########### 'y' for yes
        for person_name, history in dictPlanetHistory.items():  
            print(f"\n{person_name}\'s Solar System’s weights:") ############# Repeats Name 
            for planet_name, weight in history.items(): ################### Nested for loops are fun
                print(f"{planet_name:7}: {weight}") ################## Repeats planetary weights

    
    while True:
        name = input("\nEnter a unique name (or press Enter to exit): ").strip().lower() ########### Input Name
        if not name:
            break
        if name in dictPlanetHistory: ########### Checks for duplicate names.
            print("\nName already exists. Please enter another unique name.") 
            continue
    
        while True:
            try:
                earth_weight = float(input("\nEnter your Earth weight: ")) ################ Input weight
                break
            except ValueError: ######## Checks for float values 
                print("\nInvalid input. Please enter a numeric value.") ################## Input proper weight float value plz
    
        dictPersonWeights = {}
        for planet, factor in conversion_factors.items(): ########### For loop for conversion
            planet_weight = earth_weight * factor  ###################### Calculates weights
            dictPersonWeights[planet] = f"{planet_weight:10.2f}" ############ Formats weights
    
        dictPlanetHistory[name] = dictPersonWeights
        print(f"{name}\'s Solar System’s weights:")
        for planet, weight in dictPersonWeights.items():   ########### For loop for list of plantes 
            print(f"{planet:7}: {weight}") ###################### Prints weights by planet mass
    
    with open('bcPlanetaryWeights.db', 'wb') as file: ################## Dump the pickle in here: 'bcPlanetaryWeights.db'
        pickle.dump(dictPlanetHistory, file) #################### Pickle dump!

if __name__ == "__main__":
    main() ################# Main function
