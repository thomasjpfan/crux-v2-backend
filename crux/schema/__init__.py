import graphene

from .dataset import DatasetQuery
from .dataset import DatasetMutations
from .analysis import AnalysisQuery
from .analysis import AnalysisMutations
from .task import TaskQuery
from .task import TaskMutations
from .jwt_token import TokenMutation

from .nodes import DatasetNode
from .nodes import DatasetTagNode
from .nodes import AnalysisTagNode
from .nodes import AnalysisNode
from .nodes import TaskNode
from .nodes import UserNode


class Query(
        DatasetQuery,
        AnalysisQuery,
        TaskQuery,
        graphene.ObjectType,
):
    pass


class Mutations(
        DatasetMutations,
        AnalysisMutations,
        TaskMutations,
        TokenMutation,
        graphene.ObjectType,
):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutations,
    types={
        DatasetNode,
        DatasetTagNode,
        UserNode,
        AnalysisTagNode,
        AnalysisNode,
        TaskNode,
    })
