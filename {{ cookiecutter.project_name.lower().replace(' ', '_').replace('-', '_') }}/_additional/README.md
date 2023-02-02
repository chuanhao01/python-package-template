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

### Workflows

To Modify:

- `builds.yml`
  - You need to add in other python version you might want to support (Beside the main version you are using)
- `codeql-analysis.yml`
  - Ensure the correct branch is set
- `release-drafter.yml`
  - Ensure the correct branch is set

### Additional Information

#### Set up bots

- Set up [Dependabot](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates) to ensure you have the latest dependencies.
- Set up [Stale bot](https://github.com/apps/stale) for automatic issue closing.

#### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.
- Make a commit to `GitHub`.
- Create a `GitHub release`.
- And... publish 🙂 `poetry publish --build`

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
