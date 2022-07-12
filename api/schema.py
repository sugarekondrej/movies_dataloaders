from graphene import List, ObjectType, Schema
from graphene_django import DjangoConnectionField, DjangoObjectType
from .models import Movie,Director


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        


class DirectorType(DjangoObjectType):
    movies = List(MovieType)

    class Meta:
        model = Director
        use_connection = True

    def resolve_movies(root, info, **kwargs):
        return info.context.comments_by_article_id_loader.load(root.id)


class Query(ObjectType):
    directors = DjangoConnectionField(DirectorType)

    def resolve_directors(root, info, **kwargs):
        return Director.objects.all()


schema = Schema(query=Query)