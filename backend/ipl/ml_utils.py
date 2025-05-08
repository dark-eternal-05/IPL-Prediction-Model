import random
from .models import Team, Match, Prediction
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def ensemble_predict(team_a, team_b):
    pred = {
        "predicted_winner": random.choice([team_a, team_b]),
        "team_a_score": random.randint(140,200),
        "team_b_score": random.randint(140,200),
        "confidence": round(random.uniform(0.6,0.9),2)
    }
    return pred

def explain_prediction(match_data, prediction):
    import requests, json
    OLLAMA_URL="http://localhost:11434/api/generate"
    payload={"model":"mistral","prompt":(
        f"{match_data['team_a']} vs {match_data['team_b']} on {match_data['date']}.\n"
        f"Predicted winner: {prediction['predicted_winner']} ({prediction['confidence']*100:.0f}%).\n"
        "Explain why this prediction."
    ),"stream":False}
    try:
        r=requests.post(OLLAMA_URL,json=payload); r.raise_for_status()
        return r.json().get("response","")
    except Exception as e:
        return f"LLM error: {e}"

def broadcast_update(data):
    layer=get_channel_layer()
    async_to_sync(layer.group_send)(
        "live_matches",{"type":"send_update","data":data}
    )
