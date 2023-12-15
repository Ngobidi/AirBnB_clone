#!/usr/bin/python3
"""__init__ magic methods for the directorymodels"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
