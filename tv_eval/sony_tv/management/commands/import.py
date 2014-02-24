from django.core.management.base import BaseCommand, CommandError
from sony_tv.models import EpisodeQuery

import random
def random_subset( iterator, K ):
  result = []
  N = 0
  for item in iterator:
    N += 1
    if len( result ) < K:
      result.append( item )
    else:
      s = int(random.random() * N)
      if s < K:
        result[ s ] = item
  return result

class Command(BaseCommand):
  args = '<file_to_import subset_size>'
  help = 'imports given episodes queries'

  def handle(self, *args, **options):
    file_name = args[0]
    size = int(args[1])

    with open(file_name) as f:
      lines = f.readlines()
      lines = random_subset(lines, size)
      for l in lines:
        (series_name, episode_title) = (x.strip() for x in l.split('\t'))
        eq = EpisodeQuery(series_name=series_name, episode_title=episode_title)
        eq.save()

