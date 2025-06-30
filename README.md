# HTML to Spreadsheet Converter

This project is designed to convert HTML files into spreadsheet formats such as CSV or Excel. It utilizes Python libraries for HTML parsing and spreadsheet creation.

## Project Structure

```
html-to-spreadsheet
├── src
│   ├── main.py
│   └── utils.py
├── requirements.txt
├── README.md
└── tests
    └── test_main.py
```

## Installation

To set up the environment, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Usage

To convert an HTML file to a spreadsheet, run the following command:

```
python src/main.py <path_to_html_file> <output_file>
```

Replace `<path_to_html_file>` with the path to your HTML file and `<output_file>` with the desired output filename (including the file extension, e.g., `.csv` or `.xlsx`).

## Example

```bash
python src/main.py example.html output.csv
```

This command will read `example.html` and generate `output.csv`.

## Testing

To run the tests, navigate to the `tests` directory and execute:

```
pytest test_main.py
```

Ensure that all tests pass to confirm that the functionality works as expected.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.