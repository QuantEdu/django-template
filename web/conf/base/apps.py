INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # External libraries
    # Markdown
    'markdownx',

    # Model layer
    'polymorphic',

    'apps.example',
    'apps.custom_admin',
    'apps.graph.blocks',
]
