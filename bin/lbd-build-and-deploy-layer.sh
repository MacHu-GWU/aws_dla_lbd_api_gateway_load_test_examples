#!/bin/bash

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_project_root=$(dirname "${dir_here}")
dir_venv_bin="${dir_project_root}/venv/bin"

#---- change these config variables accordingly ---
app_name="my_package"
compatible_runtime="python3.7"
lbd_deploy_bucket="aws-data-lab-sanhe-for-everything"
#--------------------------------------------------

# clean up existing build files
rm -r "${dir_project_root}/build/lambda/python"
mkdir -p "${dir_project_root}/build/lambda/python"

# install dependencies to build dir
${dir_venv_bin}/pip install -t "${dir_project_root}/build/lambda/python" -r "${dir_project_root}/requirements.txt"

# clean up existing layer file
rm -r "${dir_project_root}/build/lambda/layer.zip"
cd "${dir_project_root}/build/lambda"

# zip the layer file
zip "${dir_project_root}/build/lambda/layer.zip" * -r -9 -q -x python/boto3\* python/botocore\* python/s3transfer\* python/setuptools\* python/pip\* python/wheel\* python/twine\* python/_pytest\* python/pytest\*;

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

