from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Sarthak'}}

@app.get('/about')  # Corrected syntax
def about():
    return {'data': 'about page'}
