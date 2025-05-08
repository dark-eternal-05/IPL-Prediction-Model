from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.cache import cache
from .models import Team, Player, Match, PlayerPerformance, Prediction
from .serializers import (
    TeamSerializer, PlayerSerializer, MatchSerializer,
    PlayerPerformanceSerializer, PredictionSerializer
)
from .ml_utils import ensemble_predict, explain_prediction

class TeamViewSet(viewsets.ModelViewSet):
    queryset=Team.objects.all(); serializer_class=TeamSerializer; permission_classes=[IsAuthenticated]

class PlayerViewSet(viewsets.ModelViewSet):
    queryset=Player.objects.all(); serializer_class=PlayerSerializer; permission_classes=[IsAuthenticated]

class MatchViewSet(viewsets.ModelViewSet):
    queryset=Match.objects.all(); serializer_class=MatchSerializer; permission_classes=[AllowAny]

class PlayerPerformanceViewSet(viewsets.ModelViewSet):
    queryset=PlayerPerformance.objects.all(); serializer_class=PlayerPerformanceSerializer; permission_classes=[IsAuthenticated]

class PredictionViewSet(viewsets.ModelViewSet):
    queryset=Prediction.objects.all(); serializer_class=PredictionSerializer; permission_classes=[IsAuthenticated]

from rest_framework.views import APIView

class PredictAPIView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        ta=request.data.get("team_a"); tb=request.data.get("team_b")
        mid=request.data.get("match_id"); dt=request.data.get("date")
        if not(ta and tb and mid and dt):
            return Response({"error":"missing fields"},status=400)
        key=f"pred:{mid}"
        cached=cache.get(key)
        if cached: return Response(cached)
        pred=ensemble_predict(ta,tb)
        expl=explain_prediction({"team_a":ta,"team_b":tb,"date":dt},pred)
        res={"match_id":mid,**pred,
             "confidence_interval":[round(pred["confidence"]-0.05,2),pred["confidence"]],
             "explanation":expl}
        cache.set(key,res,900)
        # store
        ta_obj, _=Team.objects.get_or_create(name=ta,defaults={"short_code":ta[:3].upper()})
        tb_obj, _=Team.objects.get_or_create(name=tb,defaults={"short_code":tb[:3].upper()})
        m,_=Match.objects.get_or_create(match_id=mid,defaults={"date":dt,"team_a":ta_obj,"team_b":tb_obj})
        Prediction.objects.update_or_create(match=m,defaults={
            "predicted_winner":ta_obj if pred["predicted_winner"]==ta else tb_obj,
            "predicted_team_a_score":pred["team_a_score"],
            "predicted_team_b_score":pred["team_b_score"],
            "confidence_interval":res["confidence_interval"],
            "explanation":expl
        })
        return Response(res)
