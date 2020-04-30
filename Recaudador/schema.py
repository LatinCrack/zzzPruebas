import graphene
import msMantenimientos.schema

class Query(msMantenimientos.schema.Query, graphene.ObjectType):
    pass

class Mutation(msMantenimientos.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)