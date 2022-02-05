#!/bin/bash

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_project_root="$(dirname "${dir_here}")"
dir_load_test="${dir_project_root}/tests_load"

${dir_project_root}/venv/bin/locust -f "${dir_load_test}/locustfile_slow.py" --headless --users 100 --spawn-rate 10 --stop-timeout 10
