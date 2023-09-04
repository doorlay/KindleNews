# KindleNews

This is a microservice to send a personalized news feed to my Kindle every morning; at the moment, this includes just Associated Press world news. My plan for the future is to expand the scraping capability to other sources that I read regularly.

## Design
The design is straightforward; an AWS Cloudwatch scheduled rule invokes an AWS Lambda function every morning at 6am PST. This Lambda function scrapes news data from my desired sources via BeautifulSoup, creates a text file of this news data, and uses the SendGrid API to send this file to my Kindle.

## Deployment

To deploy this microservice, you must package all dependencies into a Zip file for Lambda to execute properly. To do so, ensure there is not already a folder named "package" at the root of your project directory, and run `./deploy.sh`; this will create a zip file named `deployment_package.zip`.

Navigate to the Lambda console and create a new Python Lambda function with a basic execution role. Once created, click "Upload From" and upload the `deployment_package.zip` you previously created. Once this Zip file is uploaded to Lambda, click the "Configure" tab and choose the "environment variable" sub-tab. Add an environment variable named `SENDGRID_API_KEY` with your SendGrid API key. Under the "General configuration" sub-tab, increase the Lambda timeout to 5 minutes. Under the "Triggers" sub-tab, click "Add trigger". Type in "EventBridge" to create a new CloudWatch scheduled rule with your chosen send-time. For example, a rule of 4am UTC every day would have the cron rule `cron(0 4 * * ? *)`.