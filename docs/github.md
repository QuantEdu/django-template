# Github

## Наш текущий workflow

- ответвляемся от ветки develop, создаем ветку под каждую весомую фичу (feature-1)
- вносим изменения в своей ветке (feature-1), пушим изменения в origin/feature-1
- когда работа закончена, вносим pull-request для внесения изменения в develop
- изменения обсуждаются, вносятся промежуточные правки
- изменения merge в ветку develop
- затем периодически спускаем правки в master. master является защищенной от push веткой

## Полезные статьи

1. [Project guidelines](https://github.com/wearehive/project-guidelines)
- Perform work in a feature branch. (Работайте в отдельном бранче)
- Branch out from develop (Ответвляйтесь от ветки develop)
- Never push into develop or master branch. Make a Pull Request. (Не пушьте в aster и develop, а делайте pul-requests)
- Update your local develop branch and do an interactive rebase before pushing your feature and making a Pull Request. (перед созданием pull-request в develop обнови свою локальную версию develop ветки)
    - `git checkout feature && git merge master` - создаем новый “merge commit” в ветке feature которая объединяет историю изменений. Merging это отлично, ведь это не деструктивная операция, она никак не влияет на соседние ветки. Могут быть проблемы, если ветка master очень активна - придется часто делать merge
    - `git checkout feature && git rebase master` - перемещаем весь feature branch в конец master branch, вставляя все новые коммиты прямиком в master. В отличие merge commit, rebasing вмешивается в историю проекта, создавая копии коммитов в ветке original branch. Главное преимущество перед merge - более чистая история изменений. История изменений становится линейной.
- Золотое правило rebase. Никогда не делайте rebase, находясь в публичной ветке. Это может повлиять на структуру master ветки, что разобъет workflow с другими разработчиками.
    

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

`git checkout <branchname> && git rebase -i --autosquash develop` - Update your <branchname> branch with latest changes from develop by interactive rebase.

`git add <file1> <file2> ... && git rebase --continue` - если появились конфликты в процессе rebase - решаем их, добавляем файлы индекс и продолжаем rebase

`git push -f` - Push your branch. Rebase поменяет историю коммитов, поэтому обычный push не сработает. If someone else is working on your branch, use the less destructive --force-with-lease.


