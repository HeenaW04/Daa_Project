# main.py
# ======================================================================
# Smart Job Scheduler & Profit Optimizer
# Design and Analysis of Algorithms (DAA) Advanced Project
# Algorithm Used: Greedy Method (Job Sequencing with Deadlines & Profits)
# ======================================================================

import os, time, datetime, pandas as pd
from urllib.request import urlopen
from job_scheduler import Job, schedule_jobs
from report_utils import display_results, plot_profit_distribution, load_jobs_from_csv

# ----------------------------------------------------------------------
# Global: Algorithm Reference Links (for report section)
# ----------------------------------------------------------------------
REFERENCE_URLS = [
    "https://www.geeksforgeeks.org/job-sequencing-problem/",
    "https://www.tutorialspoint.com/greedy_algorithm/greedy_algorithm_overview.htm",
    "https://en.wikipedia.org/wiki/Greedy_algorithm",
    "https://www.researchgate.net/publication/370719345_Job_Scheduling_Algorithms_in_Cloud_Computing"
]

# ----------------------------------------------------------------------
# Function: Create results directory if not exists
# ----------------------------------------------------------------------
def ensure_results_dir():
    if not os.path.exists("results"):
        os.makedirs("results")

# ----------------------------------------------------------------------
# Function: Download dataset from URL
# ----------------------------------------------------------------------
def download_csv_from_url(url, save_as="Greedy_Job_Scheduling_Dataset.csv"):
    try:
        print("\n🌐 Downloading dataset from URL...")
        data = urlopen(url).read().decode("utf-8")
        with open(save_as, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"✅ Dataset downloaded and saved as {save_as}")
        return save_as
    except Exception as e:
        print(f"❌ Error downloading dataset: {e}")
        return None

# ----------------------------------------------------------------------
# Function: Save output in CSV + text report + JSON
# ----------------------------------------------------------------------
def save_results(jobs, job_sequence, total_profit, runtime_ms):
    ensure_results_dir()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    df = pd.DataFrame([{
        "Job ID": job.job_id,
        "Deadline": job.deadline,
        "Profit": job.profit,
        "Scheduled": "Yes" if job.job_id in job_sequence else "No"
    } for job in jobs])

    csv_path = f"results/Run_{timestamp}.csv"
    df.to_csv(csv_path, index=False)

    with open(f"results/Run_{timestamp}_Report.txt", "w") as rep:
        rep.write("=== DAA PROJECT REPORT SUMMARY ===\n")
        rep.write(f"Timestamp: {timestamp}\n")
        rep.write(f"Jobs Processed: {len(jobs)}\n")
        rep.write(f"Total Profit: {total_profit}\n")
        rep.write(f"Execution Time: {runtime_ms:.3f} ms\n")
        rep.write(f"Optimal Sequence: {job_sequence}\n")
        rep.write("\nAlgorithm References:\n")
        for url in REFERENCE_URLS:
            rep.write(f" - {url}\n")
    print(f"📁 Report saved to: {csv_path} and results/Run_{timestamp}_Report.txt")

# ----------------------------------------------------------------------
# Function: Display main menu
# ----------------------------------------------------------------------
def show_menu():
    print("\n===== SMART JOB SCHEDULER MENU =====")
    print("1️⃣  Load dataset from local CSV")
    print("2️⃣  Load dataset from URL")
    print("3️⃣  Enter jobs manually")
    print("4️⃣  View algorithm references")
    print("5️⃣  Exit")
    return input("Choose an option (1-5): ").strip()

# ----------------------------------------------------------------------
# Function: Manual job entry
# ----------------------------------------------------------------------
def get_jobs_from_user():
    jobs = []
    try:
        n = int(input("\nEnter number of jobs: "))
        for i in range(n):
            print(f"\n--- Job {i+1} ---")
            job_id = input("Job ID: ").upper()
            deadline = int(input("Deadline: "))
            profit = int(input("Profit: "))
            jobs.append(Job(job_id, deadline, profit, "User entry"))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
    return jobs

# ----------------------------------------------------------------------
# MAIN DRIVER
# ----------------------------------------------------------------------
def main():
    print("===================================================")
    print("🧠 Smart Job Scheduler & Profit Optimizer")
    print("📘 Greedy Algorithm Implementation (DAA Project)")
    print("===================================================\n")

    ensure_results_dir()

    while True:
        choice = show_menu()
        jobs = []

        if choice == '1':
            path = "Greedy_Job_Scheduling_Dataset.csv"
            if os.path.exists(path):
                jobs = load_jobs_from_csv(path)
                print(f"✅ Loaded {len(jobs)} jobs from local CSV.")
            else:
                print("⚠️ File not found. Try option 2 to download from URL.")

        elif choice == '2':
            url = input("Enter CSV URL (e.g. https://raw.githubusercontent.com/.../data.csv): ").strip()
            saved = download_csv_from_url(url)
            if saved:
                jobs = load_jobs_from_csv(saved)

        elif choice == '3':
            jobs = get_jobs_from_user()

        elif choice == '4':
            print("\n🌐 Algorithm Reference Links:")
            for ref in REFERENCE_URLS:
                print("🔗", ref)
            continue

        elif choice == '5':
            print("\n👋 Exiting Smart Job Scheduler. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice! Please select 1–5.")
            continue

        if not jobs:
            print("⚠️ No jobs loaded. Try again.")
            continue

        print("\n📋 Jobs Loaded:")
        print("Job ID | Deadline | Profit")
        print("----------------------------")
        for job in jobs:
            print(f"{job.job_id:^6} | {job.deadline:^8} | {job.profit:^6}")

        print("\n⚙️ Running Greedy Algorithm...\n")
        start = time.perf_counter()
        job_sequence, total_profit = schedule_jobs(jobs)
        end = time.perf_counter()

        runtime_ms = (end - start) * 1000

        display_results(job_sequence, total_profit)
        print(f"⏱️ Runtime: {runtime_ms:.3f} ms")
        plot_profit_distribution(jobs)
        save_results(jobs, job_sequence, total_profit, runtime_ms)

if __name__ == "__main__":
    main()
