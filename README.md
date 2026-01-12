# AI Agent - Calculator Maintenance System

An intelligent agentic system powered by **Gemini 2.5 Flash** designed to autonomously maintain, debug, and improve a Python-based calculator application.

## 🚀 Features

-   **Gemini 2.5 Flash Integration**: Leverages the latest GenAI capabilities for code analysis and generation.
-   **Autonomous Loop**: Features a 20-iteration execution loop allowing the agent to perform multi-step tasks (read -> analyze -> fix -> verify).
-   **Tool-Augmented Generation**:
    -   `get_files_info`: Recursive file system exploration.
    -   `get_file_content`: Deep code inspection.
    -   `write_file`: Automated code modification.
    -   `run_python_file`: Verification of fixes via script execution.
-   **Real-time Monitoring**: Verbose mode for tracking token usage and tool call details.

## 📁 Project Structure

```text
aiagent/
├── calculator/         # The target application maintained by the agent
├── functions/          # Tool implementations (file I/O, code execution)
├── main.py             # Agent entry point and execution loop
├── call_function.py    # Tool definitions and dispatcher
├── prompts.py          # System instructions for the agent
└── tests/              # Agent system tests
```

## 🛠️ Setup

### Prerequisites

-   Python 3.13+
-   A Google Gemini API Key

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd aiagent
    ```

2.  **Install dependencies**:
    Using `uv` (recommended):
    ```bash
    uv sync
    ```
    Or using `pip`:
    ```bash
    pip install google-genai python-dotenv
    ```

3.  **Configure Environment**:
    Create a `.env` file in the root directory:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

## 📖 Usage

Run the agent by providing a user prompt. The agent will interact with the `calculator/` directory as its working environment.

```bash
# Basic usage
python main.py "Check the calculator tests and fix any failing ones"

# Verbose usage (shows token counts and tool details)
python main.py "Add a new multiplication feature to the calculator" --verbose
```

## 🤖 How it Works

The agent follows a strict workflow defined in its system prompt:
1.  **Explore**: Scans the `calculator/` directory.
2.  **Analyze**: Reads relevant code and test files.
3.  **Implement**: Writes corrections or new features.
4.  **Verify**: Runs tests to ensure the changes are correct.

The agent continues this cycle until the task is complete or the maximum iteration limit (20) is reached.
