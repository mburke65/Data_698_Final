
import s1_analysis

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

