# main.py
# ------------------------------------------
# Optimal Resource Allocation System
# Greedy Algorithm (Job Scheduling)
# ------------------------------------------

from job_scheduler import Job, schedule_jobs
from report_utils import display_results, plot_profit_distribution

def get_jobs_from_user():
    """Takes job details as user input."""
    jobs = []
    try:
        n = int(input("Enter the number of jobs: "))
        for i in range(n):
            print(f"\n--- Enter details for Job {i+1} ---")
            job_id = input("Job ID (e.g., A, B, C): ").strip().upper()
            deadline = int(input("Deadline (in time units): "))
            profit = int(input("Profit: "))
            jobs.append(Job(job_id, deadline, profit))
    except ValueError:
        print("❌ Invalid input. Please enter numeric values for deadline and profit.")
    return jobs

def show_menu():
    """Displays the main menu."""
    print("\n==== Optimal Resource Allocation System ====")
    print("1. Use Sample Dataset")
    print("2. Enter Jobs Manually")
    print("3. Exit")
    return input("Choose an option (1/2/3): ").strip()

def main():
    while True:
        choice = show_menu()

        if choice == '1':
            jobs = [
                Job('A', 2, 100),
                Job('B', 1, 19),
                Job('C', 2, 27),
                Job('D', 1, 25),
                Job('E', 3, 15)
            ]
        elif choice == '2':
            jobs = get_jobs_from_user()
        elif choice == '3':
            print("\n👋 Exiting the program. Thank you!")
            break
        else:
            print("⚠️ Invalid choice. Please select 1, 2, or 3.")
            continue

        if not jobs:
            print("⚠️ No jobs entered! Please try again.")
            continue

        print("\nAvailable Jobs:")
        print("Job ID | Deadline | Profit")
        print("---------------------------")
        for job in jobs:
            print(f"  {job.job_id}     |    {job.deadline}     |   {job.profit}")

        job_sequence, total_profit = schedule_jobs(jobs)
        display_results(job_sequence, total_profit)
        plot_profit_distribution(jobs)

        print("\n✅ Job scheduling completed successfully!\n")

if __name__ == "__main__":
    main()
