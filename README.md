# Ops manager Github app


## Amplify app setup

```bash
amplify add auth
Using service: Cognito, provided by: awscloudformation

 The current configured provider is Amazon Cognito.

 Do you want to use the default authentication and security configuration? Default configuration
 Warning: you will not be able to edit these selections.
 How do you want users to be able to sign in? Email
 Do you want to configure advanced settings? No, I am done.
Successfully added auth resource opsmanager2956ee3a locally

```

```bash
amplify push
```

```bash
amplify add function
```

```bash
? Select which capability you want to add: Lambda function (serverless function)
? Provide an AWS Lambda function name: OpsManagerEventProcessor
? Choose the runtime that you want to use: Python
Only one template found - using Hello World by default.

Available advanced settings:
- Resource access permissions
- Scheduled recurring invocation
- Lambda layers configuration
- Environment variables configuration
- Secret values configuration

? Do you want to configure advanced settings? Yes
? Do you want to access other resources in this project from your Lambda function? No
? Do you want to invoke this function on a recurring schedule? Yes
? At which interval should the function be invoked: Hourly
? Enter the rate in hours: 1
? Do you want to enable Lambda layers for this function? No
? Do you want to configure environment variables for this function? No
? Do you want to configure secret values this function can access? Yes
? Enter a secret name (this is the key used to look up the secret value): GITHUB_GHAPP_KEY
? Enter the value for GITHUB_GHAPP_KEY: [hidden]
? What do you want to do? I'm done
Use the AWS SSM GetParameter API to retrieve secrets in your Lambda function.
More information can be found here: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html
? Do you want to edit the local lambda function now? No
Successfully added resource OpsManagerEventProcessor locally.
```

```bash
amplify push
```

```bash
amplify add api
? Please select from one of the below mentioned services: REST
? Provide a friendly name for your resource to be used as a label for this category in the project: OpsManagerApi
? Provide a path (e.g., /book/{isbn}): /github/webhook/events
? Choose a Lambda source Use a Lambda function already added in the current Amplify project
? Choose the Lambda function to invoke by this path OpsManagerEventProcessor
? Restrict API access No
? Do you want to add another path? No
Successfully added resource OpsManagerApi locally

```