# job_scheduler.py
# Core Greedy Algorithm Implementation

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

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
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if result[j] == -1:
                result[j] = job.job_id
                total_profit += job.profit
                break

    return result, total_profit
