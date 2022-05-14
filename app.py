from flask import Flask, request, jsonify
import pickle
import numpy as np

model = pickle.load(open('companion-app\model.pkl', 'rb'))

app = Flask(__name__)

#comment to check

@app.route('/')
def home():
    return "Hello World"

@app.route('/predict', methods = ['POST'])
def predict():
    nervous = request.form.get('feeling.nervous')
    panic = request.form.get('panic')
    breathing = request.form.get('breathing.rapidly')
    sweating = request.form.get('sweating')
    concentration = request.form.get('trouble.in.concentration')
    sleeping = request.form.get('having.trouble.in.sleeping')
    work = request.form.get('having.trouble.with.work')
    hopelessness = request.form.get('hopelessness')
    anger = request.form.get('anger')
    react = request.form.get('over.react')
    eating = request.form.get('change.in.eating')
    suicidal = request.form.get('suicidal.thought')
    tired = request.form.get('feeling.tired')
    friend = request.form.get('close.friend')
    socialmedia = request.form.get('social.media.addiction')
    weight = request.form.get('weight.gain')
    material = request.form.get('material.possessions')
    introvert = request.form.get('introvert')
    stressful = request.form.get('popping.up.stressful.memory')
    nightmares = request.form.get('having.nightmares')
    avoids = request.form.get('avoids.people.or.activities')
    negative = request.form.get('feeling.negative')
    concentrating = request.form.get('trouble.concentrating')
    blamming = request.form.get('blamming.yourself')

    input_query = np.array([[nervous, panic, breathing, sweating, concentration, sleeping, work, hopelessness, anger, react, eating, suicidal, tired, friend, socialmedia, weight, material, introvert, stressful, nightmares, avoids, negative, concentrating, blamming]])

    result = model.predict(input_query)[0]
    return jsonify({'Disorder': str(result)})

if __name__ == "__main__":
    app.run(debug=True)