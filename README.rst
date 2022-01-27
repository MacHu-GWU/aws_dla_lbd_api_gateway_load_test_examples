AWS Lambda + API Gateway + Load Test Examples
==============================================================================
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:


Overview
------------------------------------------------------------------------------
In this tutorial, I will cover how to set up a development environment in a few clicks using AWS Cloud 9 the AWS Native IDE. So you can develop from anywhere using any OS with just a web browser. Also I will cover the best practice to develop, test, deploy lambda function powered Rest API using Chalice, the AWS Lambda Microservice framework for Python. It allow you to focus on your application code rather than any DevOps scripts. In addition, I will walk through a load testing strategy that simulate thousands of concurrent request to test our API..


Set up Development Environment
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:


Why Cloud 9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. You can use any computer with any operational system. You just need a Web Browser.
2. The underlying OS and kernel is a Redhat liked Linux OS, and also similar to AWS Lambda container runtime. As a result, the installed python library can be directly used in AWS Lambda. If you build the Lambda dependencies on Windows, MacOS or other Linux, it may not work in AWS Lambda.
3. Native authentication support to use AWS CLI / SDK API.


Create Cloud 9 Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Creating an EC2 Environment: https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html


Use Cloud 9 IDE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Things to know:

- Top main menu
- Left side tool menu
- File explorer
- Code Editor
- Terminal
- AWS Credential Management

Reference:

- Working with IDE: https://docs.aws.amazon.com/cloud9/latest/user-guide/ide.html


AWS Lambda Development
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:


How to Use AWS Cloud 9 with Github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Generate a GitHub personal access token (GitHub recommended way) for Authentication:

    Go to GitHub -> Settings -> Developer Settings -> Personal access token -> Create one token -> grant the token Repo Read / Write access -> Store it securely.

2. Clone the Repo:

.. code-block:: bash

    # Store token in a variable, so you don't need to copy and paste it insecurely
    GH_TOKEN="abcd1234...."

    # Clone the Repo with the Token
    git clone https://${GH_TOKEN}@github.com/your-github-account-name/your-repo-name.git

3. Pull latest Code (Skip this if you prefer git cmd):

    There's a Git VCS ICON on your left top tool bar. You can see the cloned repo there.

    There's a Git Sync ICON on your left bottom tool bar. You can click to sync (Push and Pull) the code to / with remote.

3. Make change and Commit (Skip this if you prefer git cmd):

    Go to Git VCS menu, click on the ``+`` near the ``Change`` menu to add changes to git. It is ``git add`` equivalent.

    Enter commit message in the message box, click on the icon near your repo name, choose commit. Or you can just go to terminal and do ``git commit -m "your commit message"``

4. Push to Remove:

    Just click the Git Sync ICON

5. Manage branch:

    There's a Git Branch Icon on your left bottom tool bar. You can create / delete / switch branch in the branch menu.


Prepare Python Development Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Create virtualenv:

.. code-block:: bash

    bash ./bin/venv-up.sh

2. Activate virtualenv:

.. code-block:: bash

    source ./venv/bin/activate

3. Install your app package and dependencies.

.. code-block:: bash

    pip install -e .

4. Install python dependencies for unit test.

.. code-block:: bash

    pip install -r requirements-test.txt

5. Run unit test.

.. code-block:: bash

    pip install -r requirements-test.txt

Define Custom Runner, run python script in virtualenv.

6. Configure Runner to use virtualenv python.

Cloud 9 top menu -> Run -> Run With -> New Runner

.. code-block:: javascript

    // Create a custom Cloud9 runner - similar to the Sublime build system
    // For more information see http://docs.aws.amazon.com/console/cloud9/create-run-config
    {
        "cmd" : ["/home/ec2-user/environment/venv/bin/python", "$file", "$args"],
        "info" : "Started $project_path$file_name",
        "env" : {},
        "selector" : "source.ext"
    }

7. Build and publish a new version of AWS Layer.

.. code-block:: bash

    bash ./bin/lbd-build-and-deploy-layer.sh

8. Deploy Lambda functions.

.. code-block:: bash

    bash ./bin/lbd-deploy.sh

9. Delete Lambda functions.

.. code-block:: bash

    bash ./bin/lbd-delete.sh


Understand the Project file Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Python Library:

- ``/my_package/``:
- ``/MANIFEST.in``:
- ``/requirements.txt``:
- ``/requirements-test.py``:
- ``/setup.py``:
- ``/app.py``:

Python virtualenv

- ``/venv/``

Python Unit test:

- ``/tests/all.py``:
- ``/tests/test_import.py``:
- ``/tests/test_lbd_hello.py``:

Integration test and load test:

- ``/tests_int/``
- ``/tests_all/``

AWS Chalice Microservice framework for Python:

- ``/.chalice/``:
- ``/.chalice/config.json``:
- ``/.chalice/deployed/``:
- ``/.chalice/deployments/``:


What we Learned?
------------------------------------------------------------------------------
1. Cloud9, the AWS native, collaborative development environment.
2. Python project skeleton minimal viable example.
3. AWS Lambda best practice, development, testing, deployment strategy.
4. Chalices Microservices Framework.
5. API Gateway integration with AWS Lambda to power your microservices.
6. Load testing best practice.



An error occurred (AccessDeniedException) when calling the CreateFunction
operation: User: arn:aws:iam::871070586944:user/ER_buildlab is not authorized
to perform: iam:PassRole on resource:
arn:aws:iam::871070586944:role/er_buildlab_lambda because no identity-based
policy allows the iam:PassRole action