#!/usr/bin/env python3

from totus import Totus

t = Totus()
reference = t.Reference()

print("Any shop nearby:")
print(reference.GeoPOI(gh='69y7pkxfc', distance=1000, what='shop', limit=2))

print("Any shop nearby, but prividing lat/lon instead of geohash:")
print(reference.GeoPOI(lat=-34.60362, lon=-58.3824, what='shop', limit=2))

print("Only bookshops, 2km around:")
print(reference.GeoPOI(gh='69y7pkxfc', distance=2000, what='shop', filter={'shop': 'books'}, limit=2))

print("Only bookshops, 2km around, name includes the word 'libro' in any case:")
print(reference.GeoPOI(gh='69y7pkxfc', distance=2000, what='shop', filter={'shop': 'books', 'name': '~*libro*'}, limit=2))

