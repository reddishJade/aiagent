import os

from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write into the file",
            ),
        },
        required=["file_path", "content"],
    ),
)


def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Varify directory is in working directory
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_file])
            == working_dir_abs  # Will be True or False
        )
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Check if target is a directory
        if os.path.isdir(target_file):
            return f'Error: Target path is a directory, not a file: "{file_path}"'

        # Ensure the directory exists
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        # Write content to the file
        with open(target_file, "w") as file:
            file.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: writing to file: {e}"
