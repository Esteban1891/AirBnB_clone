#!/usr/bin/python3
"""Creates a unique FileStorage instance for the application"""

from models.engine.file_storage import FileStorage


"""Variable 'storage' is an instance of FileStorage"""
storage = FileStorage()
storage.reload()
