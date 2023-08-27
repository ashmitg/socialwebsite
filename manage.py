#!/usr/bin/env 

import os
import sys

import dotenv


def main():

    dotenv.load_dotenv()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social.settings.dev")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "failed installation",
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
