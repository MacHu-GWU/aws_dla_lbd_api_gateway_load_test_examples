#!/bin/bash
# Build AWS Lambda layer in Amazon Linux docker container

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_project_root="$(dirname "${dir_here}")"

#---- change these config variables accordingly ---
app_name="aws_lambda_salesforce_objects"
compatible_runtime="python3.8"
lbd_deploy_bucket="sandbox-userhome"
#--------------------------------------------------

# clean up existing build files
rm -r "${dir_project_root}/build/lambda/python"
mkdir -p "${dir_project_root}/build/lambda/python"
rm -r "${dir_project_root}/build/lambda/layer.zip"

# build layer in Amazon Linux docker container
docker run -v "${dir_project_root}:/var/task" --rm lambci/lambda:build-python3.8 bash "/var/task/bin/container-only-build-lambda-layer.sh"

# upload the layer file to AWS S3
aws s3 cp "${dir_project_root}/build/lambda/layer.zip" "s3://${lbd_deploy_bucket}/lambda/artifacts/layer.zip"

# publish a lambda layer
s3_console_url="https://s3.console.aws.amazon.com/s3/object/${lbd_deploy_bucket}?prefix=lambda/artifacts/layer.zip"
echo "lambda layer upload to ${s3_console_url}"
aws lambda publish-layer-version \
    --layer-name "${app_name}" \
    --description "dependency layer for all functions in ${app_name}" \
    --content "S3Bucket=${lbd_deploy_bucket},S3Key=lambda/artifacts/layer.zip" \
    --compatible-runtimes "${compatible_runtime}"

# display useful information
lbd_layer_console_url="https://console.aws.amazon.com/lambda/home?#/layers/${app_name}"
echo "lambda layer deploy to ${lbd_layer_console_url}"

