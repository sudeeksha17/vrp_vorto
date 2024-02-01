# vrp_vorto
**Vehicle Routing Problem**

**Overview:**
This Python script _**(mysubmission_vrp.py)**_ solves a Vehicle Routing Problem (VRP) using a naive nearest neighbour greedy heuristic approach. The script takes an input file containing information about loads (id, pickup and dropoff locations) and outputs an optimal schedule for each driver as an ordered list of load_id  based on the 12-hour driving time constraint and minimization of the total cost.

The time required to drive from one point to another, in minutes, is the Euclidean distance between them. That is, to drive from (x1, y1) to (x2, y2) takes:
        _time_taken = sqrt((x2-x1)^2 + (y2-y1)^2) minutes_
The total cost of a solution is given by the formula:
        _total_cost = 500*number_of_drivers + total_number_of_driven_minutes _

**Goal:
Minimize the total cost for a given set of loads subject to constraint:
Each driver starts and ends his shift at a depot located at (0,0). A driver may complete multiple loads on his shift, but may not exceed 12 hours of total drive time**

**Problem Constraints:**
1. All problems are solvable. That is, all loads are possible to complete within the duration of one 12-hour shift. The program does not assess problem feasibility.
2. No problem will contain more than 200 loads

**File Structure:**
1. mysubmission_vrp.py: _Main Python script that contains the VRP solver. (Comments added to ease readability)_
2. Training Problems folder with problemX.txt files: _Sample input data files for testing the solver. (X=1 to 20)_
3. eval.py: _Evaluation script to check the correctness and cost of the generated schedules_
4. output.txt: _The sample output generated by running the VRP solver for the "problem20" input file in the Training Problems folder_
5. validation_output.txt: _The validation output generated by running the VRP solver for all the 20 input files in the Training Problems folder_

**Steps to Run:**
1. Ensure Python is installed on your system.
2. Open a command prompt terminal window and go to the directory containing mysubmission_vrp.py
3. Run the script by providing the path to the input file as an argument:
          python mysubmission_vrp.py {path_to_problem}
   For example, if your input file is "problem0.txt" and everything is in the same directory then run,
          python mysubmission_vrp.py problem0.txt
5. The script will output the optimal schedules for each driver

**Sample Input and Ouput for Reference:**

![image](https://github.com/sudeeksha17/vrp_vorto/assets/158252303/f87ef43a-f28c-4586-a502-767ffb6b19f9)


**Evaluation of Solver:**
To use the evaluation script, run the following in a shell:
      _python evaluateShared.py --cmd {command to run your program} --problemDir {folder containing training problems}_
      
_The script will load every problem in the training problem folder, and run the command on each file. The {command to run your program} should NOT include a file directory (as these will be read from the problemDir folder)._

For example, if your solution is a python script called "mySubmission_vrp.py", and you have downloaded the training problems to a folder called "Training Problems", then run
      python evaluateShared.py --cmd "python mysubmission_vrp.py" --problemDir "Training Problems"
      
_(Quotes are needed around "python mySubmission_vrp.py" and "Training Problems" because of the space.)_

**References:**
1. https://developers.google.com/optimization/routing/vrp#:~:text=One%20answer%20is%20the%20routes,same%20problem%20as%20the%20TSP.
2. https://fareye.com/resources/blogs/vehicle-routing-problem-how-to-solve-it
3. https://www.sciencedirect.com/science/article/pii/S0191261522001850
