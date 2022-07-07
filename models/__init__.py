#!/usr/bin/python3
""" File that creates a unique file storage instance for the application"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
