from ..tasks.task_set import task_a_5, task_a_1, task_a_2, task_a_3, task_a_4
from efficieno.pipelines.pipelines import PipelineBase, ResultCollection
from efficieno.pipelines.tasks import TaskWrapper, task


class Pipeline1(PipelineBase):
    schedule = "My Schedule"

    var_a = 1
    var_b = 1
    result_collection = ResultCollection(results_list=[])

    task1 = TaskWrapper(task_function=task_a_1, task_args={"a": var_a, "b": var_b})
    task2 = TaskWrapper(
        task_function=task_a_2,
        task_args={"a": result_collection.get_result("task_a_1"), "b": var_a},
    )

    pipeline_tasks = [(task1, task2), (task2, task_a_5)]

