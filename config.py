import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'IASUDhaudIHdIDaidiihfe384'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/uploads/'
    ALLOWED_IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png']
    ALLOWED_VIDEO_EXTENSIONS = ['mp4', 'avi', 'mov']
