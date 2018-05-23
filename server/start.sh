#!/bin/sh

cd socket_server && \
npm install && \
cd .. && node socket_server/index.js & \
source rest_api/env/bin/activate && \
pip3 install -r rest_api/requirements.txt > /dev/null && \
python3 rest_api/manage.py runserver
