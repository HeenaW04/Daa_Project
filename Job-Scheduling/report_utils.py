# report_utils.py
# Visualization and reporting utilities

import matplotlib.pyplot as plt

def display_results(job_sequence, total_profit):
    print("\n✅ Optimal Job Sequence:", [job for job in job_sequence if job != -1])
    print(f"💰 Total Profit: {total_profit}")

def plot_profit_distribution(jobs):
    job_ids = [job.job_id for job in jobs]
    profits = [job.profit for job in jobs]
    
    plt.bar(job_ids, profits)
    plt.title("Job Profit Distribution")
    plt.xlabel("Job ID")
    plt.ylabel("Profit")
    plt.show()
