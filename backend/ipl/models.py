from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_code = models.CharField(max_length=10, unique=True)
    def __str__(self): return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    role = models.CharField(max_length=50)
    def __str__(self): return self.name

class Match(models.Model):
    match_id = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField()
    team_a = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    team_b = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    team_a_score = models.IntegerField(null=True, blank=True)
    team_b_score = models.IntegerField(null=True, blank=True)
    winner = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, related_name='wins')
    def __str__(self): return f"{self.team_a} vs {self.team_b} on {self.date.date()}"

class PlayerPerformance(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='performances')
    runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    economy_rate = models.FloatField(default=0.0)
    class Meta:
        indexes = [models.Index(fields=['player', 'match'])]

class Prediction(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE, related_name='prediction')
    predicted_winner = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='predicted_wins')
    predicted_team_a_score = models.IntegerField()
    predicted_team_b_score = models.IntegerField()
    confidence_interval = models.JSONField(null=True, blank=True)
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
