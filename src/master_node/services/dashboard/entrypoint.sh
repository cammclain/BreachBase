#!/bin/bash

exec uvicorn asgi:app --host 127.0.0.1 --port 8000