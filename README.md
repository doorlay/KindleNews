
# KindleNews
A simple microservice to deliver news to your Kindle every morning, deployed via CDK.
# Setup
1. Create and source a virtual environment.
2. Ensure your AWS credentials are properly configured for deployment. This looks something like this on Linux or MacOS:
```
export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
export AWS_SESSION_TOKEN=your_session_token
```
and this on Windows:
```
set AWS_ACCESS_KEY_ID=your_access_key_id
set AWS_SECRET_ACCESS_KEY=your_secret_access_key
set AWS_SESSION_TOKEN=your_session_token
```
3. Ensure your AWS account has been bootstrapped. If it hasn't been, do so by running `cdk bootstrap`.
4. Run `python3 -m pip install -r requirements.txt` to install all CDK dependencies.
5. Run `./package_lambda.sh` to install all Lambda dependencies.
6. Change the email on line 16 in `lambda/scraper.py` to the email address associated with your Kindle (if you're unsure what the email address associated with your Kindle is, give this a read: https://www.amazon.com/sendtokindle/email).
7. Get an API key from SendGrid and update the environment variable on line 16 in `kindle_news/kindle_news_stack.py` to your API key: https://app.sendgrid.com/guide

# Deploying

When you're ready to deploy, ensure your virtual environment is active. Then run `cdk diff` to compare the deployed stack with the current state. If all looks as expected, run `cdk synth` and `cdk deploy` to deploy.

Delete requirements-dev.txt?