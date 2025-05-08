from django.contrib import admin
from .models import Team, Player, Match, PlayerPerformance, Prediction
admin.site.register([Team, Player, Match, PlayerPerformance, Prediction])
