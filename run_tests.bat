coverage erase
coverage run --omit 'tests/*' --source . -m pytest -p no:cacheprovider
coverage report
coverage html