'''
Server of the Emotion Detector Application.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the emotional tone of input text provided via a query parameter.
    Returns:
        str: A formatted string containing the emotion scores and the dominant emotion,
            or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)

    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    ans = f"For the given statement, the system response \
        is 'anger': {res['anger']}, 'disgust': {res['disgust']}, \
        'fear': {res['fear']}, 'joy': {res['joy']} and 'sadness': \
        {res['sadness']}. The dominant emotion is {res['dominant_emotion']}."

    return ans

@app.route("/")
def render_index_page():
    """
    Render the main index page of the application.
    Returns:
        The rendered HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
