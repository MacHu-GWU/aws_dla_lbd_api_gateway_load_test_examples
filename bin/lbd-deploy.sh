#!/bin/bash

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_project_root=$(dirname "${dir_here}")
dir_venv_bin="${dir_project_root}/venv/bin"

cd "${dir_project_root}"
rm -r "${dir_project_root}/vendor"
mkdir -p "${dir_project_root}/vendor"
${dir_venv_bin}/pip install --no-deps --target "${dir_project_root}/vendor" .
${dir_venv_bin}/chalice deploy
