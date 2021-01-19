import os
from django.core.management.base import BaseCommand, CommandError
from config.settings import APPS_DIR, PROJECT_APPS


class Command(BaseCommand):
    help = 'Start new app in config directory'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)

    def handle(self, *args, **options):
        access_rights = 0o755
        app_name = options['name']
        app = os.path.join(APPS_DIR, app_name)
        if not os.path.exists(app):
            os.mkdir(app, access_rights)
            os.walk(app)

            files = ['__init__.py', 'admin.py', 'models.py',
                     'views.py', 'apps.py', 'tests.py', 'urls.py']
            for f in files:
                with open(os.path.join(app, f), 'w') as fp:
                    name = fp.name.split('/')[-1]
                    if name == 'urls.py':
                        fp.write("from django.urls import path\n\n")
                        fp.write("urlpatterns = []")
                        fp.close()

                    if name == 'views.py':
                        fp.write("from django.shortcuts import views\n")
                        fp.close()

                    if name == 'admin.py':
                        fp.write("from django.contrib import admin\n")
                        fp.close()

                    if name == 'models.py':
                        fp.write("from django.db import models\n")
                        fp.close()

                    if name == 'tests.py':
                        fp.write("from django.test import TestCase\n")
                        fp.close()

                    if name == 'apps.py':
                        fp.write("from django.apps import AppConfig\n\n\n")
                        fp.write("class %sConfig(AppConfig):\n" %
                                 app_name.title())
                        fp.write("    name = 'apps.%s'" % app_name)
                        fp.close()

            self.stdout.write(self.style.SUCCESS(
                'Successfully created "%s"' % app_name))
        else:

            self.stdout.write(self.style.SUCCESS(
                'App already exists "%s"' % app_name))
