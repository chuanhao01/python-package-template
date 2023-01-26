"""This module is called before project is created."""

import re
import sys

PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_VERSION = "{{ cookiecutter.version }}"
LINE_LENGTH_PARAMETER = "{{ cookiecutter.line_length }}"
AUTHOR_NAME = "{{ cookiecutter.author_name }}"
EMAIL = "{{ cookiecutter.email }}"


def validate_project_name(project_name: str) -> None:
    """Ensure that `project_name` parameter is valid.

    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or underscores.

    Args:
        project_name: current project name

    Raises:
        ValueError: If project_name is not a valid Python module name
    """
    MODULE_REGEX = re.compile(r"^[a-z][a-z0-9\-\_]+[a-z0-9]$")  # pylint: disable=invalid-name
    if len(project_name) == 0:
        message = "Please provide a project_name"
        raise ValueError(message)
    if MODULE_REGEX.fullmatch(project_name) is None:
        message = f"The project name `{project_name}` is not a valid Python module name."
        raise ValueError(message)


def validate_semver(version: str) -> None:
    """Ensure version in semver notation.

    Args:
        version: string version. For example 0.1.2 or 1.2.4

    Raises:
        ValueError: If version is not in semver notation
    """
    SEMVER_REGEX = re.compile(  # pylint: disable=invalid-name
        r"""
            ^
            (?P<major>0|[1-9]\d*)
            \.
            (?P<minor>0|[1-9]\d*)
            \.
            (?P<patch>0|[1-9]\d*)
            (?:-(?P<prerelease>
                (?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)
                (?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*
            ))?
            (?:\+(?P<build>
                [0-9a-zA-Z-]+
                (?:\.[0-9a-zA-Z-]+)*
            ))?
            $
        """,
        re.VERBOSE,
    )
    if SEMVER_REGEX.fullmatch(version) is None:
        message = f"The `{version}` is not in semver notation (https://semver.org/)"
        raise ValueError(message)


def validate_line_length(line_length: int) -> None:
    """Validate line_length parameter. Length should be between 50 and 300.

    Args:
        line_length: integer paramenter for isort and black formatters

    Raises:
        ValueError: If line_length isn't between 50 and 300
    """
    MIN_LINE_LENGTH = 50  # pylint: disable=invalid-name
    MAX_LINE_LENGTH = 300  # pylint: disable=invalid-name
    if not MIN_LINE_LENGTH <= line_length <= MAX_LINE_LENGTH:
        message = f"line_length must be between {MIN_LINE_LENGTH} and {MAX_LINE_LENGTH}. Got `{line_length}`."
        raise ValueError(message)


def validate_author_name(author_name: str) -> None:
    if len(author_name) == 0:
        message = "Please provide an author_name"
        raise ValueError(message)


def validate_email(email: str) -> None:
    if len(email) == 0:
        message = "Please provide an email"
        raise ValueError(message)


def main() -> None:
    try:
        validate_project_name(project_name=PROJECT_NAME)
        validate_semver(version=PROJECT_VERSION)
        validate_line_length(line_length=int(LINE_LENGTH_PARAMETER))
        validate_author_name(author_name=AUTHOR_NAME)
        validate_email(email=EMAIL)
    except ValueError as ex:
        print(ex)
        sys.exit(1)


if __name__ == "__main__":
    main()
