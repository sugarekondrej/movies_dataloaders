from collections import defaultdict
from promise import Promise
from promise.dataloader import DataLoader
from .models import Movie


class Movies_by_director_id(DataLoader):
    def batch_load_fn(self, director_ids):
        movies_by_directors_ids = defaultdict(list)

        for movie in Movie.objects.filter(director_id__in=director_ids).iterator():
            movies_by_directors_ids[movie.director_id].append(movie)

        return Promise.resolve([movies_by_directors_ids.get(director_id, [])
                                for director_id in director_ids])