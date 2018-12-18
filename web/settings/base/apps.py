INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # External librariess
    #  Markdown
    'markdownx',
    #  Bootstrap
    'bootstrap4',

    # Our apps
    'apps.bot',

    'apps.crm.courses',
    'apps.crm.groups',
    'apps.crm.services',
    'apps.crm.social',
    'apps.users',

    'apps.custom_admin',

    'apps.lms',
    'apps.lms.lessons',
    'apps.lms.results',
    'apps.lms.tasks',

    'apps.lp',

    'apps.quiz',

    'apps.studio.blocks',
    'apps.studio.tags',
    'apps.studio.themes',
]
