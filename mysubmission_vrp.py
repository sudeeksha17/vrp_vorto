
import sys
import math

#Function to read & convert the input load file information into required format for processing
def get_data(path):
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

#Function to calculate time taken to travel from one point to another based on Euclidean distance
def time_taken(pt1,pt2):
    return math.sqrt((pt2[0] - pt1[0])**2 + (pt2[1] - pt1[1])**2) #Euclidean distance,to drive from (x1, y1) to (x2, y2) takes sqrt((x2-x1)^2 + (y2-y1)^2) minutes.

#Function to calculate total driven minutes on each given path which is a dictionary of entire route for a driver
def tot_time_driven(path):
    driven_time = 0
    depot_loc=(0,0) #depot location where the driver starts/ends shift
    for j in range(len(path)): 
        driven_time += time_taken(path[j]['pickup'], path[j]['dropoff']) #adding the time taken between one points pickup and dropoff        
        if j <(len(path) - 1): #for paths with multiple loads
            driven_time += time_taken(path[j]['dropoff'], path[j+1]['pickup']) #adding the time taken between 1st points' dropoff and next points' pickup coordinates 

    driven_time += time_taken(depot_loc, path[0]['pickup']) #time to reach 1st pickup location from depot
    driven_time += time_taken(path[len(path)-1]['dropoff'], depot_loc) #time to reach back depot from last drop off

    return driven_time

#Function to solve the given VRP problem subject to driver travel time constraint and to minimize total cost
def vrp_solver(load_info):
    driver_list=[]
    depot_loc=(0,0) #depot location where the driver starts/ends shift
    driven_time_max=12*60 #12 hour constraint for each driver
    min_cost=float('inf') #initialized with inf so that the cost of 1st schedule found can be substitued for further comparisons
    
    #Naive solution:Solving the VRP problem using least distance from current location nearest neighbor, greedy approach
    while load_info:
        driven_path_crr = []
        driven_time_crr = 0
        pos_crr = depot_loc #initial location is of the depot
        
        while load_info:
            nearest_load = min(load_info, key=lambda load: time_taken(pos_crr, load['pickup']))#finding the load that's nearest to current location 
            pickup_time = time_taken(pos_crr, nearest_load['pickup']) #time to reach pickup location
            dropoff_time = time_taken(nearest_load['pickup'], nearest_load['dropoff']) #time to reach dropoff from pickup loc
            return_time = time_taken(nearest_load['dropoff'],depot_loc) #time to reach the depot back
            
            if driven_time_crr + pickup_time + dropoff_time + return_time <= driven_time_max: #to ensure the 12 hr constraint met
                driven_path_crr.append(nearest_load) #the nearest load is added to current driven path
                pos_crr = nearest_load['dropoff'] #the current driver is where the previous load dropped off
                driven_time_crr += pickup_time + dropoff_time #total time driven by current driver
                load_info.remove(nearest_load) #nearest load pickup-drop done so removed from next iteration
            else:
                break
        
        driver_list.append(driven_path_crr)
    
    total_cost=tot_cost(driver_list) #calculate total cost for current schedule
    if total_cost< min_cost: #if the calculated cost for current schedule is min then keep that instead of previous minimal value
        min_cost=total_cost
        optim_sched=driver_list #optimal schedule
    return optim_sched 
    
#Function to calculate total cost based on given formula for the VRP of input data given
def tot_cost(driver_list):
    drivers_no = len(driver_list) #Number of drivers
    driven_time_total  = sum(tot_time_driven(path) for path in driver_list) #Total time driven for all drivers
    total_cost = 500*drivers_no + driven_time_total 
    return total_cost
  
#Function to display the output as each driver’s ordered list of loads as a schedule
def output(optim_sched):
    for j,sched in enumerate(optim_sched):
        id=[] #list of load id for each driver
        for load in sched:
            id.append(load['id'])
        print(id)

if __name__ == "__main__":
    if len(sys.argv) != 2: #to ensure there's only input file path as the other argument besides the script name, as needed in problem else exits with error
        print("Retry with correct use: python mysubmission_vrp.py {path_to_problem}")
        sys.exit(1)
        
    filepath = sys.argv[1] #gets the path of input file
    #Calling all the functions defined above
    load_info = get_data(filepath) #getting load info from file in desired format using get_data function above
    optim_sched = vrp_solver(load_info) #running the solver for VRP problem to get the optimal schedule
    output(optim_sched) #to display the output as list of ordered loads for each driver in separate lines
    
