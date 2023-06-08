
def git_clone_repository(ti):
    import os
    os.environ["GIT_PYTHON_REFRESH"] = "quiet"
    import git
    import subprocess
    subprocess.call(['chmod', '-R', 'a+rwx', f'{os.getcwd()}/../gitfiles'])
    # new_repo = git.Repo.init(f'{os.getcwd()}/gitfiles')
    #if os.path.isdir(localpath):
    git_clone_url = ti.xcom_pull(key='return_value', task_ids='fetch_git_url')
    print(git_clone_url)
    #     #if os.path.isdir(localpath)
    git.Repo.clone_from(git_clone_url, f'{os.getcwd()}/gitfiles')