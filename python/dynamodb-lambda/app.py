#!/usr/bin/env python3

from aws_cdk import App

from dynamodblambda_.dynamodb_lambda_stack import DynamodbLambdaStack


app = App()
DynamodbLambdaStack(app, "dynamodb-lambda")

app.synth()
