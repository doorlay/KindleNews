# KindleNews

This is a simple microservice to send a personalized news feed to my Kindle every morning; at the moment, this includes Associated Press world news and NBA news.

The design is straightforward; an AWS Cloudwatch scheduled rule invokes an AWS Lambda function every morning at 6am PST. This Lambda function scrapes news data from my desired websites, creates a Kindle-readable EPUB file of this news data, and uses the Gmail API to send this file to my Kindle.
