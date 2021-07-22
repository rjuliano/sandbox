To deploy the python lambda function, we need to manually copy some of the native dependencies over to the site-packages directory of the current virtual environment. This is because those dependencies are compiled for OSX locally, but need to be compatible with Amazon Linux inside the lambda container.

```
cd amplify/backend/function/OpsManagerEventProcessor
```

```
# Run the following and comment out the line starting with -e in requirements.txt
pipenv run pip freeze > ./src/requirements.txt
```

```
sam build "LambdaFunction" -t ./OpsManagerEventProcessor-cloudformation-template.json --use-container --build-image amazon/aws-sam-cli-build-image-python3.8
```

```
pipenv install
```

```shell
cp .aws-sam/build/LambdaFunction/nacl/_sodium.abi3.so $(pipenv --venv)/lib/python3.8/site-packages/nacl
cp .aws-sam/build/LambdaFunction/_cffi_backend.cpython-38-x86_64-linux-gnu.so $(pipenv --venv)/lib/python3.8/site-packages

mkdir -p $(pipenv --venv)/lib/python3.8/site-packages/cffi.libs
cp .aws-sam/build/LambdaFunction/cffi.libs/* $(pipenv --venv)/lib/python3.8/site-packages/cffi.libs
# copy entire cffi.libs directory
```

```
amplify push
```

## Running the function locally

Use .env file to store aws credentials for testing (DO NOT CHECK IT IN)

```
amplify mock function AndroidOpsEventHandler --event ./events/pr_sync.json
```