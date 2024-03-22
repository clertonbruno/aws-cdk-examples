from aws_cdk import aws_lambda as _lambda, App, RemovalPolicy, Stack


class LambdaLayerStack(Stack):
    def __init__(self, app: App, id: str) -> None:
        super().__init__(app, id)

        # create layer
        layer = lambda_.LayerVersion(
            self,
            "helper_layer",
            code=lambda_.Code.from_asset("layer"),
            description="Common helper utility",
            compatible_runtimes=[
                lambda_.Runtime.PYTHON_3_6,
                lambda_.Runtime.PYTHON_3_7,
                lambda_.Runtime.PYTHON_3_8,
            ],
            removal_policy=RemovalPolicy.DESTROY,
        )
        # create lambda function
        function = lambda_.Function(
            self,
            "lambda_function",
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="index.handler",
            code=lambda_.Code.from_asset("lambda"),
            layers=[layer],
        )


app = App()
LambdaLayerStack(app, "LambdaLayerExample")
app.synth()
