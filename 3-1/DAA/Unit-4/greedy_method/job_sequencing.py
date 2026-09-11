def job_sequencing(jobs):
    """
    Solves the Job Sequencing with Deadlines problem using a greedy approach.
    Each job is represented as a tuple: (job_id, deadline, profit)
    """
    # Sort all jobs in decreasing order of their profit
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    # Find the maximum deadline to determine the size of the time slots array
    max_deadline = max(job[1] for job in jobs)
    
    # Track time slots (initialized to None/False) and the result sequence
    result = [False] * (max_deadline + 1)
    job_sequence = [''] * (max_deadline + 1)
    
    total_profit = 0
    
    # Iterate through all sorted jobs
    for job in jobs:
        job_id, deadline, profit = job
        
        # Find a free slot for this job (starting from its deadline backwards)
        for j in range(min(max_deadline, deadline), 0, -1):
            if not result[j]:
                result[j] = True
                job_sequence[j] = job_id
                total_profit += profit
                break
                
    # Filter out empty slots from the final sequence
    scheduled_jobs = [j for j in job_sequence if j != '']
    return scheduled_jobs, total_profit

# Example usage:
if __name__ == "__main__":
    # Format: (Job_ID, Deadline, Profit)
    sample_jobs = [
        ('A', 2, 100),
        ('B', 1, 19),
        ('C', 2, 27),
        ('D', 1, 25),
        ('E', 3, 15)
    ]
    
    sequence, profit = job_sequencing(sample_jobs)
    print("Scheduled Jobs:", sequence)
    print("Total Profit:", profit)
