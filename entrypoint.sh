#!/bin/bash

python -m api.migrate_cloud_db

uvicorn api.main:app --host 0.0.0.0 --reload
