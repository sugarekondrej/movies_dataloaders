from django.utils.functional import cached_property
from api.loaders import Movies_by_director_id


class GQLContext:

    def __init__(self, request):
        self.request = request

    @cached_property
    def user(self):
        return self.request.user

    @cached_property
    def comments_by_article_id_loader(self):
        return Movies_by_director_id()