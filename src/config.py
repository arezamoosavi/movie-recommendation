SECRET_KEY='sthSecret'
DEBUG=True
HOST='0.0.0.0'
PORT=5000
DEBUG=True
UPLOAD_FOLDER='/src/data'
MONGODB_HOST='dbhost'
MONGODB_USER='root'
MONGODB_PASS='rootpassword'
MONGODB_DB='admin'

CELERY_BROKER_URL = "amqp://rabbitmq"
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'