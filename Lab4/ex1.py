import matplotlib.pyplot as plt
from sklearn import datasets, svm, model_selection, metrics


# a)
iris = datasets.load_iris()
x_train, x_test, y_train, y_test = model_selection.train_test_split(
    iris.data, iris.target, train_size=100, test_size=50, shuffle=True
)

kernels = ["rbf", "linear"]

for ker in kernels:
    model = svm.SVC(kernel=ker)

    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    conf_matr = metrics.confusion_matrix(y_test, predictions)
    acc = metrics.accuracy_score(y_test, predictions)

    print(f'Accuracy for {ker}: {acc*100}%')

    disp = metrics.ConfusionMatrixDisplay(confusion_matrix=conf_matr,
                                  display_labels=model.classes_)
    disp.plot()
    plt.title(ker)
plt.show()
