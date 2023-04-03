# wan-show-parsing

My first Python project, a script to generate timestamps and chapter/clip names automatically from a YouTube URL of the WAN Show.

Sure, here's a template for setting up a project with Python and Poetry:

## Prerequisites

- Python 3.8 or higher
- Poetry

## Environment Variables

Make sure you have the following environment variables set:

- `OPENAI_KEY` - OpenAI API Key
- `OPENAI_ORG` - OpenAI Organization API Key

## Setup

1. Clone the repository to your local machine.

2. Open a terminal or command prompt and navigate to the project's root directory.

3. Install the project dependencies using Poetry by running the following command:

   ```shell
   poetry install
   ```

   This will create a virtual environment and install all the dependencies specified in the `pyproject.toml` file.

4. Activate the virtual environment by running the following command:

   ```shell
   poetry shell
   ```

   This will activate the virtual environment and allow you to run commands in the context of the project.

5. You're all set! You can now run the project by running the following command:

   ```shell
   python app.py
   ```

   Replace `app.py` with the name of the file that contains your project's entry point.

## Updating Dependencies

To update the project dependencies, simply update the version number of the dependency in the `pyproject.toml` file and run the following command:

```shell
poetry update
```

This will update the dependencies in the virtual environment.
