from efficieno.pipelines.tasks import TaskWrapper, task


@task(task_id="task_a_one", execution_timeout=300, retry=True, mode="Test")
def task_a_1(a: int, b: int):
    print("Executing Test Task A 1 ")
    return a + b


@task(task_id="task_a_two", execution_timeout=300, retry=True, mode="Test")
def task_a_2(a: int, b: int):
    print("Executing Test Task A 2 ")
    return a + b


@task(task_id="task_a_three", execution_timeout=300, retry=True, mode="Test")
def task_a_3(a: int, b: int):
    print("Executing Test Task A 3 ")
    return a + b


@task(task_id="task_a_four", execution_timeout=300, retry=True, mode="Test")
def task_a_4(a: int, b: int):
    print("Executing Test Task A 3 ")
    return a + b


@task(task_id="task_a_five", execution_timeout=300, retry=True, mode="Test")
def task_a_5():
    print("Executing Test Task A 3 ")
    return 10
