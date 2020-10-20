from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
import helperfn
import pandas



def build_nbc_models(test_size=0.2, random_state=0):
    """Build and score naive bayse Bernoulli model

    :param test_size: the percentage of the sample size to test with, defaults to 0.2
    :type test_size: float, optional
    :param random_state: the random seed, defaults to 0
    :type random_state: int, optional
    :return: Tuple of all scores and classifer
    :rtype: Tuple
    """
    training_smpl = helperfn.get_data_noresults()
    raw_data_results = []

    train_test_data = []
    classifiers = []
    scores = []

    for i in range(-1, 10):
        raw_data_results = raw_data_results + [helperfn.get_results(i)]
        train_test_data = train_test_data + [train_test_split(training_smpl, raw_data_results[i], test_size=test_size, random_state=random_state)]
        classifiers = classifiers + [BernoulliNB().fit(train_test_data[i][0], train_test_data[i][2])]
        scores = scores + [(classifiers[i].score(train_test_data[i][0], train_test_data[i][2]),
                            classifiers[i].score(train_test_data[i][1], train_test_data[i][3]))]

    for i in range(len(scores)):
        print("Scores for dataset: ", i-1)
        print("Training data score: ", scores[i][0])
        print("Testing data score: ", scores[i][1])
        print("--------------------------------------")

    return classifiers, scores, train_test_data

def build_confusion_matrix(classifiers, data):
    
    confusionMatrixArr = []
    
    for i in range(len(classifiers)):
        cm = confusion_matrix(data[i][3], classifiers[i].predict(data[i][1]))
        confusionMatrixArr = confusionMatrixArr + [cm]
        
    return confusionMatrixArr

def show_confusion_matrix(confusionMatrixArr, index_range=(0,11)):
    """
    docstring
    """
    for i in range(index_range[0],index_range[1]):
        if i == 0:
            cmd = ConfusionMatrixDisplay(
                confusionMatrixArr[i], display_labels=['20','30','50','60','70','left','right','ped Xing', 'beware childer', 'cycle route'])
        else:
            cmd = ConfusionMatrixDisplay(confusionMatrixArr[i], display_labels=['yes', 'no'])
        cmd.plot()
        
        
def countRates(number):
    values = helperfn.get_results(number).to_numpy()
    countTrue = 0
    countFalse = 0
    
    for i in values:
        if i == 0:
            countTrue += 1
        else:
            countFalse += 1
            
    return countTrue, countFalse
    
    
    
