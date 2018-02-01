from datetime import datetime


MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'mdx_math',
]

# The path where the images will be stored in your MEDIA_ROOT directory.
# Image uploaded on the 15th of April 2017 will be stored under media/markdownx/2017/4/15/unique_name.png.
MARKDOWNX_MEDIA_PATH = datetime.now().strftime('markdownx/%Y/%m/%d')

# Maximum image size allowed in bytes: Default is 50MB, which is equal to 52,428,800 bytes.
MARKDOWNX_UPLOAD_MAX_SIZE = 50 * 1024 * 1024
