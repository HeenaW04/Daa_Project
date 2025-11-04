# main.py
# Entry point for the Greedy Job Scheduling project

from job_scheduler import Job, schedule_jobs
from report_utils import display_results, plot_profit_distribution

def main():
    print("==== Optimal Resource Allocation System ====\n")

    # Sample dataset
    jobs = [
        Job('A', 2, 100),
        Job('B', 1, 19),
        Job('C', 2, 27),
        Job('D', 1, 25),
        Job('E', 3, 15)
    ]

    print("Available Jobs:")
    for job in jobs:
        print(f"Job {job.job_id} | Deadline: {job.deadline} | Profit: {job.profit}")

    job_sequence, total_profit = schedule_jobs(jobs)
    display_results(job_sequence, total_profit)
    plot_profit_distribution(jobs)

if __name__ == "__main__":
    main()
