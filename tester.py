from sklearn.metrics import accuracy_score

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
    print(f'Accuracy percent = {accuracy_precent_val}')
#     print(sse_val, accuracy_val, accuracy_precent_val)
#     return sse_val, accuracy_val