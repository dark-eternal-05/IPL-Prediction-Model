from rest_framework import serializers
from .models import Team, Player, Match, PlayerPerformance, Prediction

class TeamSerializer(serializers.ModelSerializer):
    class Meta: model = Team; fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta: model = Player; fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta: model = Match; fields = '__all__'

class PlayerPerformanceSerializer(serializers.ModelSerializer):
    class Meta: model = PlayerPerformance; fields = '__all__'

class PredictionSerializer(serializers.ModelSerializer):
    class Meta: model = Prediction; fields = '__all__'
