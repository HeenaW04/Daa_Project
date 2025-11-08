# report_utils.py
# -------------------------------------------------------
# Visualization and Reporting Utilities
# -------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
from job_scheduler import Job

def display_results(job_sequence, total_profit):
    """Display optimal job sequence and total profit."""
    print("\n✅ Optimal Job Sequence:", [job for job in job_sequence if job != -1])
    print(f"💰 Total Profit: {total_profit}")

def plot_profit_distribution(jobs):
    """Plot a bar chart of job profits."""
    job_ids = [job.job_id for job in jobs]
    profits = [job.profit for job in jobs]
    
    plt.figure(figsize=(8, 4))
    plt.bar(job_ids, profits, color='skyblue', edgecolor='black')
    plt.title("Job Profit Distribution", fontsize=14)
    plt.xlabel("Job ID")
    plt.ylabel("Profit")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def load_jobs_from_csv(filepath):
    """Load jobs from a CSV file and return as Job objects."""
    df = pd.read_csv(filepath)
    jobs = []
    for _, row in df.iterrows():
        jobs.append(Job(row["Job ID"], int(row["Deadline"]), int(row["Profit"]), row.get("Description", "")))
    return jobs
