- git fetch <远程主机名> 将某个远程主机的更新，全部取回本地
- git fetch <远程主机名> <分支名> 取回特定分支的更新
- git log -p master..origin/master 比较本地与远程分支的区别
- git checkout HEAD [file] 放弃本地没有提交的修改
- git log -p file 查看某个文件提交记录
- git log --since=2017-10-24 --until=2017-10-25 -p 查看某个时间段的记录
- git log --author='username' 查看某个用户的提交记录
- git diff 查看修改
- git remote rm origin删除远程
- git remote add origin [url] 添加新的远程
- git remote update origin --prune 刷新远程分支
- git symbolic-ref --short -q HEAD 获取当前分支名称
- git tag 列出所有tag
- git tag -a v1.0.0 -m '多游戏前稳定版本' 创建标签
- git show v1.0.0展示tag详情
- ssh-keygen -f "/home/hubo/.ssh/known_hosts" -R 172.16.20.174

- 如果当前文件是已经commit, push到远程仓库后了，.gitignore里面再配置是不起作用的，     
    此时需要清除对此文件的追踪git rm --cached xxx    或者git rm -r --cached
    文件夹名称取消追踪
    在.gitignored中添加需要过滤的文件commit, push提交.gitignore