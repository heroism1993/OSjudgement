import github_global
import os


def git_download( uri, branch,stu_no ):
    target_dir=os.path.join(github_global.HOME_DIR,stu_no)
    project=uri.split('/')
    print uri
    print project
    target_dir=os.path.join(target_dir,project[len(project)-1])
    if(os.path.exists(target_dir)):
        __import__('shutil').rmtree(target_dir)
    os.execl('/usr/bin/git','git','clone',uri,target_dir)


print github_global.HOME_DIR


print github_global.HOME_DIR+'1'


git_download('http://github.com/heroism1993/ostest','master','gaochao')


