''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:8080.
'''
# Import Flask, render_template, request from the flask pramework package :
# Import the emotion_detector function from the package created:

#Initiate the flask app :

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detection()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text = request.args.get('textToAnalyze') # Get the text to analyze from the html form
    emotion = emotion_detector(text) # Pass the text to the emotion_detector function
    emotion_dom = max(emotion[0], key=emotion[0].get) # Get the key with maximum value
    e_code = emotion[1] # Get the status_code
    if e_code == 200:
        return f"For the given statement, the system response is {emotion[0]}." \
        f"The dominant emotion is {emotion_dom}."
    if emotion[0]['joy'] == "None":
        return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    '''This function initiates the rendering of the main application
    page over the Flask channel'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
