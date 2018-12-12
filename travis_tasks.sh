#!/usr/bin/env bash
python run.py > /dev/null &
nosetests --verbosity=2 application --with-coverage
