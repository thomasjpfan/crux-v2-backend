import graphene
from graphene import relay
from graphql_jwt.decorators import login_required
from graphql_relay import from_global_id

from .nodes import TaskNode
from ..models import Task


class TaskQuery:
    task = relay.Node.Field(TaskNode)


class CreateTask(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        dataset_id = relay.GlobalID(required=True)

    task = graphene.Field(TaskNode)

    @staticmethod
    @login_required
    def mutate_and_get_payload(self,
                               info,
                               name,
                               dataset_id,
                               client_mutation_id=None):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('Authentication credentials were not provided')

        _type, _id = from_global_id(dataset_id)
        graphene_type = info.schema.get_type(_type).graphene_type
        dataset_obj = graphene_type.get_node(info, _id)

        if dataset_obj.created_by != user:
            raise Exception('User did not create dataset')

        task, _ = Task.objects.get_or_create(name=name,
                                             dataset=dataset_obj,
                                             created_by=user)
        return CreateTask(task=task)


class EditTask(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        task_id = relay.GlobalID(required=True)

    task = graphene.Field(TaskNode)

    @staticmethod
    @login_required
    def mutate_and_get_payload(self,
                               info,
                               name,
                               task_id,
                               client_mutation_id=None):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('Authentication credentials were not provided')

        _type, _id = from_global_id(task_id)
        graphene_type = info.schema.get_type(_type).graphene_type
        task_obj = graphene_type.get_node(info, _id)
        task_obj.name = name
        task_obj.save()

        return EditTask(task=task_obj)


class TaskMutations:
    create_task = CreateTask.Field()
    edit_task = EditTask.Field()
