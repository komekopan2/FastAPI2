#!/bin/bash

# DBが起動するのを待つ
/wait-for-it.sh db:3306 --timeout=30

# python -m api.migrate_db
# ローカル用自動マイグレーション

python -m api.migrate_cloud_db
# クラウド用自動マイグレーション

uvicorn api.main:app --host 0.0.0.0 --reload
