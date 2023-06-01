#!/bin/bash

if [ ! -d venv ];then
    python3 -m venv venv
    pip install -r requirements.txt
fi

if [ -d venv ];then
    cd /Users/kzk/Dev/journey
    source venv/bin/activate
    cd py-AAA
    python3 journey_md.py
    python3 atosyori.py
fi