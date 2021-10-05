from math import sqrt
class PRECISION_RECALL:
    def answers(tp, tn, fp, fn):
        ppv = tp / (tp + fp)
        rcl = tp / (tp + fn)
        mcc = (tn * tp - fn * fp) / sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
        f1 = 2 * (ppv * rcl) / (ppv + rcl)

        return ppv, rcl, mcc, f1

    def Cohens_kappa(TP, TN, FP, FN):
        Po = (TP + TN) / (TP + TN + FP + FN)
        Pe = ((TP + FN) * (TP + FP) + (FP + TN) * (FN + TN)) / ((TP + TN + FP + FN) * (TP + TN + FP + FN))
        Kappa = (Po - Pe) / (1 - Pe)
        return Kappa 

    print("enter the value of true positive")
    _tp = input()
    print("enter the value of true negative")
    _tn = input()
    print("enter the value of false negative")
    _fn = input()
    print("enter the value of false positive")
    _fp = input()
    print("enter the value of true negative")
    print("PRECISION , RECALL , MATHEWS CORELATION COEFFICIENT FORMULA, F1 SCORE ")
    print(answers(int(_tp), int(_tn), int(_fp), int(_fp)))
    print("this is cohen's_kappa-->")
    print(Cohens_kappa(int(_tp), int(_tn), int(_fn), int(_fp)))