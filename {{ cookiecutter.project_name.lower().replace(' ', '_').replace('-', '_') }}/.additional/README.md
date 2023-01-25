# Additional changes after template generation

Here you can find additional specific template data to add to your project if you choose to.

## .github

Github related files for:
- Issue template
- Pull Request template
- Workflows

To add:
Copy the `.github` folder to the root of your project

### Templates

To Modify:
Use and edit as you wish

### workflows

To Modify:
- `builds.yml`
  - You need to add in other python version you might want to support (Beside the main version you are using)
- `codeql-analysis.yml`
  - Ensure the correct branch is set
- `release-drafter.yml`
  - Ensure the correct branch is set


## Makefile

### test-gen-badge
Used for:
You can add in the ability to generate a coverage badge based on your coverage result in your test.

To add:
Take the code [here](./Makefile#L1) and replace it [here](../Makefile#L46)

## .editor

A folder to folder editor specific configs for the project.

To add:
- Copy the `.editor` folder into the root of the project
- Add in your editor configs, update the `.editor/README.md`
