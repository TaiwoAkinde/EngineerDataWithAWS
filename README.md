# EngineerDataWithAWS
###A simple project to demonstrate basic data engineering process with Python and AWS

# URL: https://realpython.com/pipenv-guide/#pipenv-introduction

-- create a corresponding repo on GitHub

-- pip install pipenv [Run this on your PC for package management like the "npm" in javascript]

-- create your project directory on local pc
   -> git init
   -> Open your IDE from within the project folder
   >> Shift + Right Click >> Open cmd or Open Powershell
     -> In your IDE terminal:
        # use pipenv to create a Python 3 (--three) virtualenv for our project
        >> pipenv --three
        # To activate this project's virtualenv, run pipenv shell.
        >> pipenv shell
        # install dependency(ies) on our project
        >> pipenv install ******
        # Let’s say you also have some unit tests for this awesome application, and you want to use pytest for running them. You don’t need pytest in production so you can specify that this dependency is only for development with the --dev argument
        >> pipenv install pytest --dev


-- link your local repo to GitHub
  -> https://docs.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line
  

----> Project Description:
-- Simple Data Engineering using:
    - Python
    - Boto3 (AWS SDK for Python)

    # Create a user and assign appropriate rights on AWS IAM for development purposed
    # get the :
      .. aws_access_key_id
      .. aws_secret_access_key
      store these securely and reference in your main app


-----> Moving to production
        # Okay, so let’s say you’ve got everything working in your local development environment and you’re ready to push it to production. To do that, you need to lock your environment so you can ensure you have the same one in production:
        >> pipenv lock
        # Now, once you get your code and Pipfile.lock in your production environment, you should install the last successful environment recorded:
        >> pipenv install --ignore-pipfile