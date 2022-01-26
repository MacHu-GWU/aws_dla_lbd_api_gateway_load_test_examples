#!/bin/bash

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_project_root=$(dirname "${dir_here}")

${dir_project_root}/venv/bin/pytest "${dir_project_root}/tests" -s
