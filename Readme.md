==========
Last Update: June 26 2024, 3:24 AM EST, blaze
==========

**Before typing anything in CMD (command prompt), open the command prompt of the directory (unless advised otherwise). Do that by:
- Open File Explorer
- Open directory of where you've saved the folder of the website
- On the left side of the search bar, there's a bar showing you the Path. Click in there and type "cmd" then hit ENTER


## OVERALL:
These commands are for overall use (whole file/folder).

- **rebase**: `git rebase [file hash]` --> (*Need more info about this command) (Go back in the past)
```py
print("love you Soth")
```
-stash: `git stash` --> holds your unsaved changes temporary. Kinda works like copy and paste.
    -    `git stash apply` --> applies your held changes.


BRANCHES:
Create:
- Write "git branch [name]" in cmd

Delete:
- Write "git branch -d [name]" in cmd

Switch between branches:
- Write "git switch [branch name]" in cmd

Merge a branch to the *main* branch:
- Change back to main branch, in cmd
- Write "git merge -m <message of choice, optional> [branch name]" in cmd

Merge the main branch to a *different* branch:
- Write "git checkout [branch name] && git merge main" in cmd (not tested)
or
- Go to Github website and select "Pull Requests"
- Select "New Pull Request"
- 'base' means *where you want to merge it to* and 'compare' means *what you're merging into the 'base'*. So choose accordingly --> base: ['branch name'] and compare: [main]
- Write a title (if empty or you can write your own title) and write a description for clarity of merge and purpose
- You (if branches can merge auotmatically) or Owner (Ali) can confirm the pull request in order to merge the 2 branches
- Switch to the branch (not main) and do "git pull" in cmd

Check which branch you're in and see all your branches:
- Write "git branch" in cmd

PULLS:
To receive the saved changes from Github to your device:
- Write "git pull" in cmd

CLONE:
An easy and clean way to clone repository from github to your pc is:
- Go to Github website
- Select the correct repository
- Click on green button that says "code" and select "Open  with Github Desktop"
- When Github desktop is installed, select the repository you desire to clone
- Select in which folder you want to install the cloned repository
- Hit "Clone"

WEBSITE:
To start the website using cmd commands (env commands) do:
- Write "flask run"
    For Ali:
        -Write "python -m flask run" in cmd

To start the website using python script, make sure to have [__name__ = '__main__'] set in your code (bottom):
- Write "python [file name]". It should run smoothly


----------

INFO:

- set FLASK_APP=[file name]: This means that you're creating an environment variable for your website.

- set FLASK_DEBUG=[file name]: This will make it so you don't have to stop and restart your website everytime you make a change. With this you can reload the page in your browser and the changes will be applied.