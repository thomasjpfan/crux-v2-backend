import graphene
import graphql_social_auth


class TokenMutation(graphene.ObjectType):
    social_auth = graphql_social_auth.relay.SocialAuthJWT.Field()
