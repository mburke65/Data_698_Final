
import s1_analysis


def get_most_informative_features(nbclassifier, n=10):
    # Determine the most relevant features, and display them.
    cpdist = nbclassifier._feature_probdist
    flist = []
    for (fname, fval) in nbclassifier.most_informative_features(n):
        def labelprob(l):
            return cpdist[l, fname].prob(fval)

        labels = sorted(
            [l for l in nbclassifier._labels if fval in cpdist[l, fname].samples()],
            key=labelprob,
        )
        if len(labels) == 1:
            continue
        l0 = labels[0]
        l1 = labels[-1]
        if cpdist[l0, fname].prob(fval) == 0:
            ratio = 'INF'
        else:
            ratio = '%8.1f' % (
            cpdist[l1, fname].prob(fval) / cpdist[l0, fname].prob(fval)
            )
        flist.append(tuple((fname, l1)))
    return flist




s1 = s1_analysis.s1_analysis()
s1.train_load("s1_model_2.sav")
text1 = "Some keywords for sentiment classification: radiant funny"
features = s1.find_features(text1)
result = (s1.classifier.classify(features))
print(result)
text1 = "Some keywords for sentiment classification: turgid unfunny"
features = s1.find_features(text1)
result = (s1.classifier.classify(features))
print(result)

if1 =  get_most_informative_features(s1.classifier, 4)
print(if1)
