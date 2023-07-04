#!/usr/bin/env bash
mkdir package
pip install --target ./package beautifulsoup4
pip install --target ./package sendgrid
pip install --target ./package requests
cd package
zip -r ../deployment_package.zip .
cd ..
zip deployment_package.zip lambda_function.py