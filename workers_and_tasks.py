tasks = [2, 4, 6, 11]
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



