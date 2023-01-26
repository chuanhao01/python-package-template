"""This module is called after project is created."""

import textwrap
from pathlib import Path
from shutil import copyfile, rmtree

PROJECT_ROOT = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_MODULE = "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}"
CREATE_EXAMPLE_TEMPLATE = "{{ cookiecutter.create_example_template }}"
ADDITIONAL_CONTENT = "{{ cookiecutter.additional_content }}"

# Values to generate correct license
LICENSE = "{{ cookiecutter.license }}"
ORGANIZATION = "{{ cookiecutter.organization }}"

licences_dict = {
    "MIT": "mit",
    "BSD-3": "bsd3",
    "GNU GPL v3.0": "gpl3",
    "Apache Software License 2.0": "apache",
}


def generate_license(project_root: Path, licence: str) -> None:
    """Generate license file for the project.

    Args:
        project_root: path to the project project_root
        licence: chosen licence
    """
    copyfile(
        (project_root / "_licences" / f"{licence}.txt").as_posix(),
        (project_root / "LICENSE").as_posix(),
    )
    rmtree((project_root / "_licences").as_posix())


def remove_cli(project_root: Path, module_name: str) -> None:
    """Remove unused files.

    Args:
        project_root: path to the project project_root
        module_name: project module name
    """
    file_to_delete: Path = project_root / module_name / "__main__.py"
    file_to_delete.unlink()


def remove_additional_content(project_root: Path) -> None:
    rmtree((project_root / ".additional").as_posix())


def print_futher_instuctions(project_name: str) -> None:
    """Show user what to do next after project creation.

    Args:
        project_name: current project name
    """
    message = f"""
    Your project {project_name} is created.

    1) Now you can start working on it:

        $ cd {project_name} && git init

    2) If you don't have Poetry installed run:

        $ make poetry-download

    3) Initialize poetry and install pre-commit hooks:

        $ make install
        $ make pre-commit-install

    4) Run codestyle:

        $ make codestyle

    """
    print(textwrap.dedent(message))


def main() -> None:
    generate_license(project_root=PROJECT_ROOT, licence=licences_dict[LICENSE])
    if CREATE_EXAMPLE_TEMPLATE != "cli":
        remove_cli(
            project_root=PROJECT_ROOT,
            module_name=PROJECT_MODULE,
        )
    if ADDITIONAL_CONTENT == "no":
        remove_additional_content(project_root=PROJECT_ROOT)
    print_futher_instuctions(project_name=PROJECT_NAME)


if __name__ == "__main__":
    main()
