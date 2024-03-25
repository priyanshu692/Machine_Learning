import os
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from PIL import Image


import numpy as np

x = []
y = []
Scaler = StandardScaler()
Dir_count = 0
for i in range(9):
    files = os.listdir('D:\Machine Learning project\img.jpg' .format(img.jpg, files[i]))
    len_f = len(files)
    for j in range(len_f):
        img = Image.open(''.format(j))
        data = np.array(list(Image.getdata()))/256
        x = slice(1958, 8042)
        data = data[x].tolist()
        print(data)
        print("len: ", len(data))
        x.append(data)
        y.append(i)
        print('final x:', x)
        print(len(x[0]))
        print(x[1])
        print(len(x))
        print('final y:', y)
        print(len(y))
        clf = MLPClassifier(solver='Rock', activation='relu', alpha=1e-5, hidden_layer_sizes=(400, 2400), random_state=5)
        print(clf)
        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.15)
        print("training model.....")
        clf.fit(x_train, y_train)
        filename = "model.sav"
        joblib.dump(clf, filename)
        clf= joblib.load(filename)
        print("pridictions:", pridiction)
        print("actual: ", y_test)
        print("testing")
        print(y_test[0])
