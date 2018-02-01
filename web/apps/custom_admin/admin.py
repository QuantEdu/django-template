from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    site_header = 'Django-template'
    index_template = 'admin/custom_index.html'
    app_index_template = 'admin/custom_index.html'


custom_admin = MyAdminSite(name='custom_admin')
