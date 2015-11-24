# course_mgt_sys
Web app for managing course grades and students interactions within/outside of class

# Setup Instructions
1. clone the repository
2. run `cd course_mgt_sys` to make the project your working directory
3. run `pip install -r requirements.txt` to install all required libraries
4. run `python manage.py migrate`
5. run `python manager.py runserver`
6. Open browser to http://localhost:8000/

# Teams
- Red team is responsible for the students app
- Green team is responsible for the courses app
- Blue team is responsible for the instructors app

# Process description
- Be sure to *fork* the project in your github repository
- Create new branch to work on from *dev* branch
- Push changes to *your* github repository fork
- Send pull request when you push an update, and choose the branch you worked on
- *ALWAYS* work on a new branch for every new feature

# sending a pull request
- After forking the original project, clone your forked project to your local machine
- *ALWAYS* start from branch dev, switch to it using `git checkout dev`
- Create a new branch from branch dev by running `git checkout -b newbranchname`
- After completing and testing your work, commit it
- finally, push your new branch to your forked project using `git push origin newbranchname`
- Got ot github, issue a pull request to the almarzouq/course_mgt_sys (branch dev)

# Working with the most recent copy of the dev branch
- *IMPORTANT* after forking the project, create a remote called upstream:
      git remote add upstream https://github.com/almarzouq/course_mgt_sys.git
- Before creating any branch, switch to branch dev, and run `git pull upstream dev`
  This will update the dev to match what is on the project dev repository so
  you can work on a fresh copy

hello from monia
