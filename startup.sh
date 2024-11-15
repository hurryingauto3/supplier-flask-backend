#!/bin/bash

# Install dependencies (if needed)
if [ ! -d "venv" ]; then
    pip install -r requirements.txt
fi

# flask db init
# flask db migrate
# # Run database migrations only if they haven't been applied
flask db upgrade

# Start the Gunicorn server
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
