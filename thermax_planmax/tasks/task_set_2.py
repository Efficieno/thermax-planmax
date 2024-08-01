from efficieno.pipelines.tasks import TaskWrapper, task


@task(task_id="task_b_one", execution_timeout=300, retry=True, mode="Test")
def task_b_1(a: int, b: int):
    print("Executing Test Task A 1 ")
    return a + b


@task(task_id="task_b_two", execution_timeout=300, retry=True, mode="Test")
def task_b_2(a: int, b: int):
    print("Executing Test Task A 2 ")
    return a + b


@task(task_id="task_b_three", execution_timeout=300, retry=True, mode="Test")
def task_b_3(a: int, b: int):
    print("Executing Test Task A 3 ")
    return a + b


@task(task_id="task_b_four", execution_timeout=300, retry=True, mode="Test")
def task_b_4(a: int, b: int):
    print("Executing Test Task A 3 ")
    return a + b


@task(task_id="task_b_five", execution_timeout=300, retry=True, mode="Test")
def task_b_5():
    print("Executing Test Task A 3 ")
    return 10
