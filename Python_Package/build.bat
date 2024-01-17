@echo off
py -m build
twine upload dist/*
