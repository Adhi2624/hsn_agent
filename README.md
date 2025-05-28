# hsn_agent

## Description

hsn\_agent is a project designed for processing, analyzing, and leveraging Harmonized System Nomenclature (HSN) data. It provides tools for data preprocessing, interaction with a Chroma database for efficient data storage and retrieval, and an intelligent agent for in-depth data analysis. This project aims to streamline the handling of HSN data, making it easier to extract valuable insights and patterns.

## Files

-   `agent.py`: Contains the core logic for the data analysis agent, including algorithms and methods for extracting insights from HSN data.
-   `preprocess.py`: Includes scripts for cleaning, transforming, and preparing HSN data for analysis and storage in the Chroma database.
-   `chromaclient.py`: Provides a client interface for interacting with the Chroma database, enabling data storage, retrieval, and querying.
-   `requirements.txt`: Lists all the necessary dependencies and libraries required to run the project, ensuring easy setup and reproducibility.
-   `data/`: Contains the raw HSN data files, such as `HSN_SAC.xlsx - HSN_MSTR.csv`, which serve as the input for the project's data processing and analysis pipelines.

## Installation

To get started with hsn\_agent, follow these steps:

1.  Clone the repository to your local machine.
2.  Navigate to the project directory:

    ```bash
    cd hsn_agent
    ```

3.  Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Data Preprocessing:**
    Use the scripts in `preprocess.py` to clean and transform the HSN data.
    ```bash
    python preprocess.py
    ```

2.  **Chroma Database Interaction:**
    Utilize the `chromaclient.py` to interact with the Chroma database.
    ```python
    from chromaclient import ChromaClient
    client = ChromaClient()
    # Perform database operations
    ```

3.  **Run the Agent:**
    Execute the main agent script to perform data analysis.
    ```bash
    python HSN_agent/agent.py
    ```

## Data

The `data/` directory contains the HSN data files, including `HSN_SAC.xlsx - HSN_MSTR.csv`. These files are used as input for the data processing and analysis pipelines. Ensure that the data is properly formatted and accessible to the scripts.

## Chroma Database

The project uses a Chroma database to store and retrieve processed HSN data. The database files are located in the `chroma/` directory. The `chromaclient.py` provides the necessary tools to interact with the database, allowing you to store, query, and retrieve data efficiently.

## Contributing

We welcome contributions to hsn\_agent! If you'd like to contribute, please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and ensure they are well-tested.
4.  Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
