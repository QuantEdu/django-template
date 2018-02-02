# Github

1. [Project guidelines](https://github.com/wearehive/project-guidelines)
- Perform work in a feature branch. (Работайте в отдельном бранче)
- Branch out from develop (Ответвляйтесь от ветки develop)

2. [Tuturial from BitBucket](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)

## Команды гита

`git status` - показывает статус репозитория, измененные файлы

`git add .` - добавить файлы из данной директории в индекс git

`git commit -m "First Commit"` - делаем коммит

`git push origin master` - послать изменения из ветки (master) на удаленный сервер (origin)

`git branch future-plans` - создать бранч future-plans

`git checkout future-plans` - переместиться в бранч future-plans

Процесс merge

`git checkout master` - вернуться на ветку master

`git merge future-plans` - слить изменения из ветки future-plans в текущую ветку

`git branch -d future-plans` - удалить локальную ветку future-plans

`git push origin master` - push на сервер

`git fetch [имя удал. сервера]` - для получения данных из удалённых проектов
