#!/usr/bin/env python3
import os
import sys

sys.path.append("/private/var/mobile/Containers/Shared/AppGroup/78C973F3-CD3B-41D8-9BE8-E489AE2EB4B6/Pythonista3/Documents/git/learning_log_Django_Python_crash_course/")

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
