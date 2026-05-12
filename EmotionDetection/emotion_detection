import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    e_code = response.status_code
    if e_code == 200:
        emotion = json.loads(response.text)
        emotion = emotion['emotionPredictions'][0]
        emotion = emotion['emotion']
        return [emotion, e_code]
    elif e_code == 400:
        text = "Blank"
        myobj = { "raw_document": { "text": "Blank" } }
        response = requests.post(url, json = myobj, headers=header)
        emotion = json.loads(response.text)
        emotion = emotion['emotionPredictions'][0]
        emotion = emotion['emotion']
        keys = emotion.keys()
        emotion = emotion.fromkeys(keys, "None")
        return [emotion, e_code]
'''

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    response = json.loads(response.text)
    response = response['emotionPredictions'][0]
    response = response['emotion']
    return response
    
'''
