"""This module is called after project is created."""

import textwrap
from pathlib import Path
from shutil import copyfile, rmtree

PROJECT_ROOT = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_MODULE = "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}"
CREATE_EXAMPLE_TEMPLATE = "{{ cookiecutter.create_example_template }}"
ADDITIONAL_CONTENT = "{{ cookiecutter.additional_content }}"

ADDITIONAL_CONTENT_DIR = PROJECT_ROOT / "_additional"
LICENSES_DIR = PROJECT_ROOT / "_licences"

# Values to generate correct license
LICENSE = "{{ cookiecutter.license }}"
ORGANIZATION = "{{ cookiecutter.organization }}"

# License selected to file name mapping
licences_dict = {
    "MIT": "mit",
    "BSD-3": "bsd3",
    "GNU GPL v3.0": "gpl3",
    "Apache Software License 2.0": "apache",
}


def generate_license(project_root: Path, licenses_dir: Path, licence: str) -> None:
    """Generates and cleans up license  file for the project"""
    copyfile(
        (licenses_dir / f"{licence}.txt").as_posix(),
        (project_root / "LICENSE").as_posix(),
    )
    rmtree(licenses_dir.as_posix())


def remove_cli(project_root: Path, module_name: str) -> None:
    """Remove unused files.

    Args:
        project_root: path to the project project_root
        module_name: project module name
    """
    file_to_delete: Path = project_root / module_name / "__main__.py"
    file_to_delete.unlink()


def remove_additional_content(additional_content_dir: Path) -> None:
    rmtree(additional_content_dir.as_posix())


def print_usage_additional_instructions():
    """Shows user what to do with the additional data generated"""
    message = """
    === Additional Data ===

    There is also additional data generated along with your project.
    You can find how and what you can do with the files in ./.additional directory.

    DO REMEMBER to delete the `.additional` directory after you are done adding any data you want.
    IT IS RECOMMENDED TO NOT commit the folder into git"""
    print(textwrap.dedent(message))


def print_futher_instructions(project_name: str) -> None:
    """Show user what to do next after project creation."""
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

    === Recommended Changes ===

    - Check through docs, README.md, SECURITY.md, CODE_OF_CONDUCT.md, CONTRIBUTING.md"""
    print(textwrap.dedent(message))


def main() -> None:
    # Post project generation cleanup
    generate_license(
        project_root=PROJECT_ROOT, licenses_dir=LICENSES_DIR, licence=licences_dict[LICENSE]
    )
    if CREATE_EXAMPLE_TEMPLATE != "cli":
        remove_cli(
            project_root=PROJECT_ROOT,
            module_name=PROJECT_MODULE,
        )
    if ADDITIONAL_CONTENT == "no":
        remove_additional_content(additional_content_dir=ADDITIONAL_CONTENT_DIR)

    # Showing instructions
    print_futher_instructions(project_name=PROJECT_NAME)
    if ADDITIONAL_CONTENT == "yes":
        print_usage_additional_instructions()


if __name__ == "__main__":
    main()
