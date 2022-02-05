AWS Lambda API Gat
==============================================================================
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:

Tags: ``AWS``, ``Microservice``, ``AWS Lambda``, ``AWS API Gateway``, ``Load Test``, ``Python``, ``AWS Cloud9``.


Overview
------------------------------------------------------------------------------
This is a tutorial demonstrate the development best practice for building many AWS Lambda powered microservices at scale, and expose microservice as a Rest API to serve external / internal request.

**Knowledge we covered in this tutorial**:

1. Leverage the AWS Cloud 9, the cloud native IDE that allow you to develop applications on your Web browser, and collaboratively writing code in the same environment.
2. The general Python project development best practice, using shell script to standardize your team development workflow. Plus unit test/code coverage test/integration test best practice for shipping high quality application.
3. The microservice development, testing deployment best practice using AWS Chalice. Allow you to focus on implementing the core logic, perform local testing without deployment, and one command to deploy mass amount of microservices and API gateway at scale.
4. The Microservices Architect best practice using API Gateway to provide simplicity and maintainability, advanced protection for your backend, improved throughput using request cache, and monitoring plus notification out of the box.
5. Simple strategy to run high concurrent load testing without needs of any complicate set up.


1. Set up Development Environment using AWS Cloud 9
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:


Why Cloud 9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. **You can use any poor hardware computer with any operational system. You just need a Web Browser**.
2. **Seamless collaborative coding experience** for engineering teams.
3. **Advanced System Security and Network Security** out of the box. Protect your files / code / network traffic never leave your AWS environment.
4. Native authentication support to use AWS CLI / SDK API.
5. First class Git support for source code version control.
6. The underlying OS and kernel is a Redhat liked Linux OS, and also similar to AWS Lambda container runtime. As a result, the installed python library can be directly used in AWS Lambda. If you build the Lambda dependencies on Windows, MacOS or other Linux, it may not work in AWS Lambda.


Create Cloud 9 Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The native of Cloud 9 environment is just a EC2 virtual machine in your AWS environment on VPC. Follow this document to create your environment.

- Creating an EC2 Environment: https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html


Use Cloud 9 IDE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Things to know:

- Top main menu: classic IDE liked menu.
- Left side tool menu: search anything, file explorer, SVC tool, AWS explorer.
- File explorer: create / edit / rename / move / delete file and folder, show hidden files.
- Code Editor: hot key for save / comment / close tab / etc ...
- Terminal: a local terminal with bash shell, you can use other shells too.
- AWS Credential Management: manage the AWS access for your Cloud 9 VM.
- Use EC2 instance Profile when using Cloud 9 in Private subnet: the AWS Managed credential won't work when Cloud 9 is on Private subnet. You should consider using EC2 instance profile.

Reference:

- Working with IDE: https://docs.aws.amazon.com/cloud9/latest/user-guide/ide.html


Use AWS Cloud 9 with Github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This tutorial shows how to securely pull and push a Private Github Repository on AWS Cloud 9.

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

4. Push to Remote:

    Just click the Git Sync ICON, or ``git push``

5. Manage branch:

    There's a Git Branch Icon on your left bottom tool bar. You can create / delete / switch branch in the branch menu.


2. General Python Project Development Best Practice
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:


Common Python Development Workflow Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- create Python virtual environment (virtualenv)to isolate your development python from the Linux system python.
- activate / deactivate python virtualenv.
- install your Python project in editable mode.
- install dependencies, for application / dev / test / documentation / etc ...
- run unit test / code coverage test / integration test.


Understand the Project file Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Python Library:

- ``/my_package/``:
- ``/MANIFEST.in``:
- ``/requirements.txt``:
- ``/requirements-dev.py``:
- ``/requirements-test.py``:
- ``/setup.py``:

Python virtualenv

- ``/venv/``: the Python virtual environment to use. we don't check in this folder to SVC. ``.gitignore`` will prevent that.

Python Unit test:

- ``/tests/all.py``:
- ``/tests/test_import.py``:
- ``/tests/other-test-cases.py``:

Integration test and load test:

- ``/tests_int/``
- ``/tests_load/``

Common development workflow action automation

- ``/bin/*.sh``: bin stands for binary, it is Linux convention folder to store executable files, such as shell script.


The Common Development Workflow Action Automation Best Practice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- ``bash ./bin/01-venv-up.sh``
- ``bash ./bin/02-venv-remove.sh``
- ``bash ./bin/03-pip-install.sh``
- ``bash ./bin/04-pip-install-everything.sh``
- ``bash ./bin/05-run-unit-test.sh``
- ``bash ./bin/06-run-coverage-test.sh``
- ``bash ./bin/07-run-integration-test.sh``
- ``bash ./bin/08-run-load-test.sh``
- ``bash ./bin/10-lbd-build-and-deploy-layer-in-container.sh``
- ``bash ./bin/11-lbd-build-and-deploy-layer.sh``
- ``bash ./bin/12-lbd-deploy.sh``
- ``bash ./bin/13-lbd-delete.sh``


3. AWS Lambda Development
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:


Prepare Python Development Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Create virtualenv:

.. code-block:: bash

    bash ./bin/01-venv-up.sh

2. Activate virtualenv:

.. code-block:: bash

    source ./venv/bin/activate

3. Install your app package and dependencies.

.. code-block:: bash

    bash ./bin/03-pip-install.sh

4. Install python dependencies for unit test.

.. code-block:: bash

    bash ./bin/04-pip-install-everything.sh

5. Run unit test.

.. code-block:: bash

    bash ./bin/05-run-unit-test.sh
    
6. Run code coverage test.

.. code-block:: bash

    bash ./bin/06-run-coverage-test.sh

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

    bash ./bin/11-lbd-build-and-deploy-layer.sh

8. Deploy Lambda functions.

.. code-block:: bash

    bash ./bin/12-lbd-deploy.sh

9. Delete Lambda functions.

.. code-block:: bash

    bash ./bin/13-lbd-delete.sh


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
