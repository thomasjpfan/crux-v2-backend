from graphene import relay
from .nodes import TaskNode


class TaskQuery:
    task = relay.Node.Field(TaskNode)


class TaskMutations:
    pass
