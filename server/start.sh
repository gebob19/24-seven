#!/bin/sh

cd socket_server && \
npm install && \
cd .. && node socket_server/index.js & \
source rest_api/venv/bin/activate && \
pip install -r rest_api/requirements.txt > /dev/null && \
python rest_api/manage.py runserver