from constructs import Construct
from aws_cdk import Stack, Duration
# from aws_cdk.aws_s3 import Bucket
from aws_cdk.aws_events import Rule, Schedule
from aws_cdk.aws_events_targets import LambdaFunction
from aws_cdk.aws_lambda import Function, Runtime, Code


# Read in the API key
secrets = open("secrets.txt")
SENDGRID_API_KEY = secrets.read()

class KindleNewsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Lambda function that scrapes and sends all data
        scraper_lambda = Function(self, "NewsScraper", runtime=Runtime.PYTHON_3_11, handler="scraper.handler", 
                                  code=Code.from_asset("lambda"), timeout=Duration.minutes(5), function_name="NewsScraper", environment={
                                      "SENDGRID_API_KEY": SENDGRID_API_KEY})

        # CloudWatch Scheduled Rule to invoke the above Lambda at 6am PST every day
        scraper_rule = Rule(self, "ScraperRule", schedule=Schedule.cron(hour="14",minute="0"), rule_name="ScraperRule")
        scraper_rule.add_target(LambdaFunction(scraper_lambda))

        # S3 bucket that stores all logs
        # TODO: setup logging
        # logging_bucket = Bucket(self, "LoggingBucket", versioned=True, bucket_name="logging-bucket")

