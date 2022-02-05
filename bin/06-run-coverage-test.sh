#!/bin/bash
# Run code coverage test

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_project_root="$(dirname "${dir_here}")"
dir_pytest_cache="${dir_project_root}/.pytest_cache"
dir_coverage_annotate="${dir_project_root}/.coverage.annotate"

python_lib_name="my_package"

# remove existing coverage annotate
rm -r "${dir_pytest_cache}"
rm -r "${dir_coverage_annotate}"

# execute code coverage test
${dir_project_root}/venv/bin/pytest "${dir_project_root}/tests" -s "--cov=${python_lib_name}" "--cov-report" "term-missing" "--cov-report" "annotate:${dir_coverage_annotate}"
