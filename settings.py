# Flask settings
FLASK_SERVER_NAME = 'localhost:8080'
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# MONGO settings
MONGO_URI = 'mongodb+srv://kenny:123Kehinde#@cluster0-mhdy8.mongodb.net/Alexlistings?retryWrites=true&w=majority'
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'AlexListings'
SQLALCHEMY_TRACK_MODIFICATIONS = False