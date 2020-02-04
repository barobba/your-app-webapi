#!/usr/bin/env bash

# TIP: Manually install private repositories in the base directory

pip install --no-deps -t ./ git+https://github.com/barobba/your-app-library.git#egg=your_app
