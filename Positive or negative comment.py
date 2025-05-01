import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
review  = ["The product is excellent and works perfectly",    
           "The Product is not good or very dissaponting",
           "terrible Product and waste of money",
           "I love this product and it is amazing"]
sentements =np.array([1,0,0,1])
#we have to tokkenized  the review for this we import featured extraction.text
#Now we have to trained or test 
#We import Countvectorizer in which bydefault have featured of train or test so we dont need to Import seperatly
Tokens = CountVectorizer()
X = Tokens.fit_transform(review)
#apply model
Model = MultinomialNB()
Model.fit(X,sentements)
#Now make function for make o,1 to Text
def functioN(TakeVaraible):
    VectorizedTakeVaraible = Tokens.transform(TakeVaraible)
    prediction = Model.predict(VectorizedTakeVaraible)
    if prediction[0] == 1:
        return "Postive sentement"
    else:
        return "Negative sentement"
    
#Take users input and call function to solve
User_input = input("Enter your review")
Result  = functioN([User_input])
print(f"The review'{User_input}' is classified as '{Result}'")