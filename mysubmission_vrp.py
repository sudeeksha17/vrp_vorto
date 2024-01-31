
import sys
import math

#Function to read & convert the input load file information into required format for processing

def get_data(path)
    with open(path, 'r') as file: #reading the input file
        lines = file.readlines()

    load_info = []
    for l in lines:
        if l.startswith('loadNumber'): #skipping the file's header line 
            continue

        id_load, pickup_loc, dropoff_loc = l.strip().split() #separating the load id, pickup and drop locations for each load; strip func not necessary but put in case any input file has extra spaces
        #index :[1:-1] is taken from the locations to remove the brackets
        x_pickup, y_pickup = map(float, pickup_loc[1:-1].split(','))  # Extract pickup co-ordinates and convert to float
        x_dropoff, y_dropoff = map(float, dropoff_loc[1:-1].split(','))  # Extract dropoff co-ordinates and convert to float

        load_info.append({'id': int(id_load), 'pickup': (x_pickup, y_pickup), 'dropoff': (x_dropoff, y_dropoff)}) # combining the final load info as a list with a nested dict    

    return load_info

# def vrp_solver(load_info):

# def output(vrp_sol):

if __name__ == "__main__":
    if len(sys.argv) != 2: #to ensure there's only input file path as the other argument besides the script name, as needed in problem else exits with error
        print("Retry with correct use: python mysubmission_vrp.py {path_to_problem}")
        sys.exit(1)
        
    filepath = sys.argv[1] #gets the path of input file
    load_info = get_data(filepath) #getting load info from file in desired format using get_data function above
    
#     vrp_sol = vrp_solver(load_info) #running the solver for VRP problem
#     output(vrp_sol) #to display the output as required
