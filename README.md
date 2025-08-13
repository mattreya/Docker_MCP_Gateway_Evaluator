# Gemini CLI Project Template

This project serves as a template for developing Python applications that integrate with the Gemini Command Line Interface (CLI). It demonstrates how to incorporate external Python packages like `bandit` for security analysis and `duckduckgo_mcp_interface` for web searches, and expose their functionalities as custom Gemini CLI slash commands.

## What's New in This Repo

We've recently enhanced this repository by integrating Trivy, a comprehensive open-source vulnerability scanner. The new `/trivy` slash command allows users to perform filesystem scans directly from the Gemini CLI. This integration streamlines the process of identifying security vulnerabilities in project dependencies and configurations, making security analysis an integral part of the development workflow within the CLI environment.

## Features

- **Gemini CLI Integration:** Provides a structured way to define and manage custom slash commands for the Gemini CLI.
- **Bandit Integration:** Includes a slash command (`/bandit`) to run the Bandit static analysis tool on your project, helping identify common security vulnerabilities in Python code.
- **DuckDuckGo Search Integration:** Offers a slash command (`/ddg`) to perform web searches using the DuckDuckGo API, leveraging the `duckduckgo_mcp_interface`.
- **NIST Guidelines Reference:** Contains a reference to NIST guidelines (`/nist`) for secure bot development, emphasizing best practices for handling sensitive information.
- **Configurable Preferences:** Introduces a preference system (`/preferences`) that allows the Gemini CLI to understand and adapt to user-defined preferences for various tasks, such as preferred tools for web searches, project analysis, and security scanning.

## Project Focus: Docker MCP and Toolkit Integration

This project's primary focus is the integration with Docker's Multi-Cloud Platform (MCP) and Toolkit, exposed through new Gemini CLI slash commands. These commands streamline the process of discovering and utilizing Docker tools directly from your command line.

### New Docker-Related Slash Commands:

-   **`/mcp_catalog_lookup`**:
    *   **Purpose:** This command allows you to search and retrieve information from the Docker MCP Catalog. It helps in discovering available Docker images, services, and solutions.
    *   **How to use:**
        ```
        /mcp_catalog_lookup <search_query>
        ```
        Replace `<search_query>` with keywords to find relevant items in the catalog.

-   **`/mcp_toolkit_selector`**:
    *   **Purpose:** After reviewing the MCP Catalog, this command assists in determining the best Docker tool from the MCP Toolkit to use for a specific task or requirement. It aims to guide users to the most suitable solution.
    *   **How to use:**
        ```
        /mcp_toolkit_selector <catalog_item_id_or_description>
        ```
        Provide an identifier or description of the catalog item you're interested in, and the command will suggest appropriate tools.

-   **`/askgordon`**:
    *   **Purpose:** While not directly tied to Docker MCP, this command is part of the new set of functionalities. Its specific purpose would be defined by its implementation, but it's designed to provide intelligent assistance or answer questions within the Gemini CLI context.
    *   **How to use:**
        ```
        /askgordon <your_question>
        ```
        Ask Gordon anything, and it will attempt to provide a relevant answer or guidance.

This project builds upon the foundation of the `matt_raio_bot_constraints` repository, which provides the underlying framework for Gemini CLI integration and custom slash commands.

## Setup and Installation

To get this project up and running, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create and activate a virtual environment:**
    It's highly recommended to use a virtual environment to manage project dependencies.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    Install the required Python packages using `pip`.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the project is set up, you can interact with it through the Gemini CLI using the defined slash commands.

-   **`/bandit`**: Runs the Bandit static analysis tool on the project.
-   **`/ddg`**: Performs a DuckDuckGo web search. You can specify a query as an argument.
-   **`/nist`**: Displays the NIST guidelines for bot development.
-   **`/preferences`**: Shows the current preferences configured for the Gemini CLI's behavior.
-   **`/trivy`**: Runs a Trivy filesystem scan on the current directory. You can specify a target and scan type (e.g., `/trivy . fs`).

## Project Structure

-   `.gemini/commands/`: Contains the `.toml` files defining the custom Gemini CLI slash commands.
-   `slash_commands.py`: Implements the Python functions that are executed by the slash commands.
-   `requirements.txt`: Lists the project's Python dependencies.
-   `NIST_guildlines.md`: Document outlining NIST guidelines for bot development.
-   `.gitignore`: Specifies files and directories to be ignored by Git.

