from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
import pickle
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
pc=PorterStemmer()
no_stop=stopwords.words('english')
app=FastAPI()




@app.post('/predict')
def prediction(data:str):

    model=pickle.load(open('review_model.pkl','rb'))
    result=model.predict([data])[0]
    return JSONResponse(status_code=200,content={'prediction':result})