import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        # Varify directory is in working directory
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir])
            == working_dir_abs  # Will be True or False
        )
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        files = []
        for file in os.listdir(target_dir):
            file_path = os.path.join(target_dir, file)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            file_info = f"  - {file}: file_size={file_size} bytes, is_dir={is_dir}"
            files.append(file_info)

        result = f"Result for '{directory}' directory:\n" + "\n".join(files)
        return result
    except Exception as e:
        return f"Error: {str(e)}"
