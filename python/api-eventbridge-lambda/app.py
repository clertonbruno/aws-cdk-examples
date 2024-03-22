#!/usr/bin/env python3

from aws_cdk import App

from api_eventbridgelambda_.api_eventbridge_lambda import ApiEventBridgeLambdaStack


app = App()
ApiEventBridgeLambdaStack(app, "ApiEventBridgeLambdaStack")

app.synth()
