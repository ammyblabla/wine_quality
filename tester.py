from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.metrics.scorer import make_scorer
from sklearn.metrics import recall_score
from sklearn.model_selection import cross_validate

def sse(est, real):
    sse = 0
    # est = [2,2,2,2]
    # real = [1,1,1,1]

    if len(est) != len(real):
        print('length not equal')
        return float('inf')

    n = len(est)

    for i in range(n):
        sse += (est[i] - real[i]) ** 2
    return sse

def accurency(est, real):
    count = 0
    if len(est) != len(real):
        print('length not equal')
        return float('inf')

    n = len(est)

    for i in range(n):
        if est[i] == real[i]:
            count += 1
    return count

def evaluate(y_predict, y_test):
    sse_val = sse(list(y_predict), real=list(y_test))
    accuracy_val = accuracy_score(y_test, y_predict,normalize=False)
    accuracy_precent_val = accuracy_score(y_test, y_predict,normalize=True)
    print(f'SSE = {sse_val}')
    print(f'Accuracy = {accuracy_val}')
    print(f'Accuracy percent = {accuracy_precent_val * 100}%')
#     print(sse_val, accuracy_val, accuracy_precent_val)
    return [sse_val, accuracy_val, accuracy_precent_val]

def cross_val(clf, df, y, cv=10):
    predicted = cross_val_predict(clf, df, y, cv=10)
    return metrics.accuracy_score(y, predicted) 

def cross_val_accuracy(clf, df, y, cv=10):
    scores = cross_val_score(clf, df, y, cv=10)
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

def cross_val_full_scores(clf, df, y, cv=10):
    scoring = {'prec_macro': 'precision_macro',
            'rec_micro': make_scorer(recall_score, average='macro')}
    scores = cross_validate(clf, df, y, scoring=scoring,cv=10, return_train_score=True)