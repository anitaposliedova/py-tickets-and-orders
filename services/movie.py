from django.db import transaction

from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None, title=None):
    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)

    if title:
        queryset = queryset.filter(title__icontains=title)

    return queryset


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None
):
    with transaction.atomic():
        movie = Movie.objects.create(
            title=movie_title,
            description=movie_description
        )

        if genres_ids:
            movie.genres.set(genres_ids)

        if actors_ids:
            movie.actors.set(actors_ids)