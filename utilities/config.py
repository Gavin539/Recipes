import os

class Config:
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_default_secret_key') # Secret key for Flask app
    FLASK_ENV = 'development'  # Cwhen deploying # Set to 'development' for debugging


    # Load Crawlbase API key from environment variables
    CRAWLBASE_API_KEY = os.getenv("CRAWLBASE_API_KEY")



    # Model paths
    MODEL_PATH = 'model/saved_model/model.pkl'
   

    

  

 