#!/bin/bash

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_project_root="$(dirname "${dir_here}")"
dir_venv_bin="${dir_project_root}/venv/bin"
dir_lambda_app="${dir_project_root}/lambda_app"

rm -r "${dir_lambda_app}/vendor"
mkdir -p "${dir_lambda_app}/vendor"
${dir_venv_bin}/pip install --no-deps --target "${dir_lambda_app}/vendor" "${dir_project_root}"
${dir_venv_bin}/chalice --project-dir "${dir_lambda_app}" deploy --stage dev
