# The Official CodeWithAli Website Repo

## Instructions to run the code
1. Run `git clone https://github.com/aalibrahimi/CodewithAli.git` in the folder where you want the project to be
2. Run `cd CodewithAli`
3. Run `python -m venv .venv`
4. Run `.\.venv\Scripts\activate`
5. Run `pip install -r requirements.txt`
6. Run `python website.py`


# **Important**

```
Make sure to ALWAYS have you branches up to date when you log on!

Before typing anything in CMD (command prompt), open the command prompt of the directory (unless advised otherwise). Do that by:

- Open File Explorer
- Open directory of where you've saved the folder of the website
- On the left side of the search bar, there's a bar showing you the Path. Click in there and type `cmd` then hit ENTER
```

## OVERALL:
These commands are for overall use (whole file/folder).

- **rebase**: `git rebase [file hash]` --> Used to keep branches (excluding main) up to date.
- **stash**: `git stash` --> Holds your unsaved changes temporary. Kinda works like copy and paste.
    -    `git stash apply` --> Applies your held changes.
- **checkout** --> Used to go back in the past.


## BRANCHES:

### Create:
- Write `git branch [name]` in cmd/terminal

### Delete:
- Write `git branch -d [name]` in cmd/terminal

### Switch between branches:
- Write `git switch [branch name]` in cmd/terminal

### Merge a branch to the *main* branch:
- Change back to main branch, in cmd/terminal
- Write `git merge -m <message of choice, optional> [branch name]` in cmd/terminal

    **Note: This method doesnt update Github!*

*or*

- Go to Github website and select **Compare and Pull Request** or **Pull Request**
- Select **New Pull Request** *(if selected Compare and Pull Request)*
- '**base**' means *where you want to merge it to* and '**compare**' means *what you're merging into the 'base'*. So choose accordingly --> base: ['**branch name**'] and compare: **main**
- Write a title *(if empty or you can write your own title)* and write a description for clarity of merge and purpose
- You *(if branches can merge auotmatically)* or Owner *(Ali)* can confirm the pull request in order to merge the 2 branches
- Switch to the main branch and do `git pull` in cmd/terminal


### Merge the main branch to a *different* branch:
- Go to Github website and select **Pull Requests**
- Select **New Pull Request**
- '**base**' means *where you want to merge it to* and '**compare**' means *what you're merging into the 'base'*. So choose accordingly --> base: ['**branch name**'] and compare: **main**
- Write a title *(if empty or you can write your own title)* and write a description for clarity of merge and purpose
- You *(if branches can merge auotmatically)* or Owner *(Ali)* can confirm the pull request in order to merge the 2 branches
- Switch to the branch *(not main)* and do `git pull` in cmd/terminal

### Check which branch you're in and see all your branches:
- Write `git branch` in cmd/terminal

## PULLS:

To receive the saved changes from Github to your device:
- Write `git pull` in cmd/terminal

## CLONE:

An easy and clean way to clone repository from github to your pc is:
- Go to Github website
- Select the correct repository
- Click on green button that says `code` and select `Open  with Github Desktop`
- When Github desktop is installed, select the repository you desire to clone
- Select in which folder you want to install the cloned repository
- Hit '**Clone**'

## WEBSITE:

To start the website using cmd commands (env commands) do:
- Write `flask run`

    For Ali:
        -Write `python -m flask run` in cmd/terminal

To start the website using python script, make sure to have `__name__ = '__main__'` set in your code *(bottom)*:
- Write `python [file name]`. It should run smoothly



## INFO:

- set **FLASK_APP=[file name]**: This means that you're creating an environment variable for your website.

- set **FLASK_DEBUG=[file name]**: This will make it so you don't have to stop and restart your website everytime you make a change. With this you can reload the page in your browser and the changes will be applied.
