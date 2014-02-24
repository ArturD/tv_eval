# -*- coding: utf-8 -*-
from django.contrib import admin
from sony_tv.models import *

class EpisodeQueryAdmin(admin.ModelAdmin):
  pass
class RunAdmin(admin.ModelAdmin):
  pass
class ResultAdmin(admin.ModelAdmin):
  pass

admin.site.register(EpisodeQuery, EpisodeQueryAdmin)
admin.site.register(Run, RunAdmin)
admin.site.register(Result, ResultAdmin)
