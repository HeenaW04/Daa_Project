# job_scheduler.py
# -------------------------------------------------------
# Implements the Greedy Job Scheduling Algorithm
# -------------------------------------------------------

class Job:
    def __init__(self, job_id, deadline, profit, description="No description"):
        """
        Represents a job with an ID, deadline, profit, and an optional description.
        """
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit
        self.description = description  # ✅ added to match CSV data

def schedule_jobs(jobs):
    """
    Schedule jobs to maximize total profit using a greedy approach.
    Sorts jobs by descending profit, then assigns each to the latest possible slot.
    """
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = max(job.deadline for job in jobs)
    result = [-1] * n
    total_profit = 0

    for job in jobs:
        # Try to find a free slot for this job (starting from its deadline)
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if result[j] == -1:
                result[j] = job.job_id
                total_profit += job.profit
                break

    return result, total_profit
