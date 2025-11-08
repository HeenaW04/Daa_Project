Ramdeobaba University, Nagpur
Department of Computer Science and Engineering
Session: 2025-26

Subject: Design and Analysis of Algorithms (DAA) Lab Project
III Semester
LAB PROJECT REPORT

Group Members with Roll number and Section:

Anannya Mahajan – A5 – 53
Heens Wadhwani - A5 - 22
Purval Neware - A5 - 52


GITHUB link of Project repo and deployment link (if website):
https://heenaw04.github.io/Daa_Project



TITLE: Optimal Resource Allocation System using Greedy Algorithm


Objectives: 
1.	To design and implement a Greedy-based job scheduling system that maximizes total profit within deadline constraints.
2.	To integrate real-time and CSV-based data input, simulating real-world resource scheduling environments.
3.	To analyze time–space complexity and visualize algorithm performance through charts.
4.	To demonstrate data persistence, report generation, and external algorithm references.
5.	To understand the impact of greedy decision-making on global optimization.

Introduction:

Resource allocation and job scheduling play a crucial role in fields like cloud computing, manufacturing, and process automation. These problems involve assigning jobs to limited time slots to maximize overall profit or efficiency.
The Greedy Job Scheduling Algorithm is an efficient approach to such optimization challenges. It operates on a simple principle — at each step, choose the locally optimal option (highest profit job that can still meet its deadline), hoping this leads to a globally optimal solution.
This project, Smart Job Scheduler & Profit Optimizer, enhances the traditional greedy algorithm by:
•	Integrating CSV-based and URL-based datasets.
•	Automatically saving reports and runtime statistics.
•	Using Matplotlib to visualize profit distributions.
•	Comparing theoretical efficiency with practical runtime.


Algorithms/Technique used:

AGreedy Job Scheduling Algorithm

Algorithm Steps:
1.	Sort all jobs in descending order of profit.
2.	Initialize an array to represent available time slots.
3.	For each job (in sorted order):
o	Assign it to the latest available slot before its deadline.
4.	If a slot is occupied, skip to the next available slot.
5.	Stop when all jobs are checked or slots filled.
6.	Compute total profit and output job sequence.

Pseudocode:

Sort all jobs by decreasing profit
Initialize result array of size = max_deadline
For each job in sorted list:
    For j = min(max_deadline, job.deadline) - 1 down to 0:
        If result[j] is empty:
            result[j] = job
            total_profit += job.profit
            break
Display total_profit and job sequence

Explanation:
The greedy algorithm chooses the job with the highest profit first and assigns it to the latest possible available slot before its deadline.
This ensures that high-profit jobs are given priority while still meeting time constraints.

Diagram (Conceptual):
Jobs:  A(2,100), B(1,19), C(2,27), D(1,25), E(3,15)

Slots: [ _ , _ , _ ]

After Scheduling:
Slot 1 -> C
Slot 2 -> A
Slot 3 -> E

Total Profit = 142


Time Complexity and its explanation:

Step No.	Operation / Task	Explanation	Time Complexity	Space Complexity
1	Sorting Jobs by Profit	Jobs are sorted in descending order of profit using an efficient sorting algorithm (like Tim Sort in Python).	O(n log n)	O(1) (in-place sort)
2	Finding Maximum Deadline	Finds the largest deadline value among all jobs to define slot array size.	O(n)	O(1)
3	Slot Allocation for Jobs	For each job, the algorithm searches backward to find an available time slot.	O(n × m) where m = max deadline	O(n) (for result array)
4	Total Profit Calculation	Sum of profits for scheduled jobs.	O(n)	O(1)
—	➡ Overall Complexity	The sorting step dominates total runtime. Hence, final complexity is:	O(n log n)	O(n)


Results:
Job ID	Deadline	Profit	Description
J1	3	80	Cloud Resource Allocation
J2	1	35	Urgent System Update
J3	2	60	Batch Data Processing
J4	2	25	Reporting & Logging
J5	1	20	Routine Backup
J6	3	100	Server Maintenance
J7	2	45	Data Compression
J8	3	30	Notification Job


Sample Input:

Job A | Deadline: 2 | Profit: 100
Job B | Deadline: 1 | Profit: 19
Job C | Deadline: 2 | Profit: 27
Job D | Deadline: 1 | Profit: 25
Job E | Deadline: 3 | Profit: 15

Output:
 <img width="450" height="162" alt="image" src="https://github.com/user-attachments/assets/b3499ff5-e6d6-4a82-a54f-4ba8639cb17c" />


Graph:

<img width="979" height="572" alt="image" src="https://github.com/user-attachments/assets/b5650a57-79b0-40c6-875d-1f6c58839f40" />



Conclusion and future scope:

The developed system demonstrates how Greedy algorithms can efficiently optimize resource allocation by focusing on local decisions with global impact.
It also integrates data engineering concepts like CSV I/O, runtime measurement, visualization, and reporting, bridging the gap between theoretical and applied computing.

Future Scope :
•	Integrate Dynamic Programming or Genetic Algorithms for comparison.
•	Develop a web dashboard using Streamlit for interactive scheduling.
•	Extend to cloud-based or real-time job arrivals.
•	Include machine learning for predictive job prioritization.


