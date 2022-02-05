import keyboard  
import pyperclip,time
import pyttsx3
engine = pyttsx3.init()


given="Numpy, Pandas, Matplotlib, Pytorch, Tensorflow, Keras, Scikit Learn, OpenCV, NLTK, Scikit Multiflow, Deep Learning, Generalized Linear Models, Dimensionality Reduction, Model Optimization, Neural Networks, Transformers, GANs, Ensemble Methods, Long-Tailed Recognition, Time Series Analysis, Python, Arduino, C++, SQL,Regex, AWS, Spark, Git, Flask, REST APIs, React, Flutter, Firebase, Docker, Kubernetes ,3D printing, rapid prototyping, digital fabrication, web designing, Design Thinking, product management, product prototyping, documentation, technical writing, leadership, presentation, intrapreneurship, entrepreneurship, people management, team player, initiative, proactiveness, automation, CNNs, python scripting, Autohotkey scripting"
given_list=given.split(",")
given_list=list(map(lambda a: a.strip(),given_list))

time.sleep(2)
for item in given_list:
    pyperclip.copy(item)
    engine.say(item)
    print(item)
    engine.runAndWait()
    while True:
        if keyboard.read_key() == "shift":
            time.sleep(1)
            break