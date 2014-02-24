from django.core.management.base import BaseCommand, CommandError
from sony_tv.models import Run

class Command(BaseCommand):
  args = '<base_url comment>'
  help = 'Closes the specified poll for voting'

  def handle(self, *args, **options):
    (base_url, comment) = args
    self.stdout.write('it works!')
