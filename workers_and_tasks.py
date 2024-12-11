tasks = [2, 4, 6, 8]
workers = [3, 5, 7,10,]

def tasks_can_complete(tasks, workers):
    completed_tasks = []
    for task in tasks:
        for worker in workers:
            if task <= worker:
                if task not in completed_tasks:
                    completed_tasks.append(task)
    
    return len(completed_tasks)

print(tasks_can_complete(tasks, workers))


def task_can_complete_(tasks, workers):
    tasks.sort()
    workers.sort()
    
    task_pointer = 0
    worker_pointer = 0
    completed_tasks = 0
    
    while  task_pointer < len(tasks) and worker_pointer < len(workers):
        if tasks[task_pointer] <= workers[worker_pointer]:
            completed_tasks += 1
            task_pointer += 1
            worker_pointer += 1
    return completed_tasks
    
print(task_can_complete_(tasks, workers))
                