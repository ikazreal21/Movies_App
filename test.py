import requests
import json


movie = []

# APIKEY = 'pk_ktvqwjdsbowaoqnrf'
# APIKEY = 'k_8q318v4f'
APIKEY = '1a4cb261'
pk = 'tt0133093'
title = 'matrix'

movieSearch = requests.get(
    url='http://www.omdbapi.com/?apikey={}&i={}&plot=full'.format(APIKEY, pk)
)

# movieSearch = requests.get(
#     url='http://www.omdbapi.com/?apikey={}&s={}'.format(APIKEY, title)
# )

movieSearch = movieSearch.json()
# movieSearch = json.loads(movieSearch)
context = {"movie": movieSearch}

print(context["movie"]["Title"])


# context = {"movies": []}


# for i in movieSearch["Search"]:
#     context['movies'].append(
#         {
#             "id": i["imdbID"],
#             "image": i["Poster"],
#             "title": i["Title"],
#             "year": i["Year"],
#         }
#     )

# for i in context['movies']:
#     print(i['id'])

# context = {
#     "id": movieSearch["id"],
#     "title": movieSearch["title"],
#     "fulltitle": movieSearch["fullTitle"],
#     "year": movieSearch["year"],
#     "image": movieSearch["image"],
#     "release": movieSearch["releaseDate"],
#     "plot": movieSearch["plot"],
#     "directors": movieSearch["directors"],
#     "contentRating": movieSearch["contentRating"],
#     "imDbRating": movieSearch["imDbRating"],
# }


# print(context["id"])


# for i in movieSearch:
#     movie.append(
#         {
#             "id": i["id"],
#             "title": i["title"],
#             "fulltitle": i["fulltitle"],
#             "year": i["year"],
#             "image": i["image"],
#             "release": i["releaseDate"],
#             "plot": i["plot"],
#             "directors": i["directors"],
#             "contentRating": i["contentRating"],
#             "imDbRating": i["imDbRating"],
#         }
#     )

# for i in movie:
#     print(i)
