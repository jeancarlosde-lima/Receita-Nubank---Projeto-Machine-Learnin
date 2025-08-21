#!/bin/sh
source .venv/bin/activate
# O argumento --host=0.0.0.0 é importante para que o servidor seja acessível
# a partir do painel de preview do IDX.
python -u -m flask run --host=0.0.0.0 --port=$PORT
