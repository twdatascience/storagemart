import re
import pandas as pd
import pdb  

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_storage_info(text):
    """
    Finds and extracts the JSON object containing storage info from the given text.
    Returns the extracted JSON object as a Python dictionary, or None if not found.
    """
    return_dict = {}
    idx = 0 
    pattern = r'(\{("id"[\s\S]*?)\})'
    matches = re.finditer(pattern, text)
    for match in matches:
        match_str = match.group(0)
        if "discountedPrice" in match_str:
            return_dict[idx] = match_str
            idx += 1

    return return_dict

def parse_json_like_string(s):
    """
    Parses a JSON-like string into a Python dictionary using regex.
    Handles strings, numbers, booleans, nulls, and simple arrays of dicts.
    """
    result = {}
    # Remove outer braces if present
    s = s.strip()
    if s.startswith('{') and s.endswith('}'):
        s = s[1:-1]
    # Regex to match key-value pairs
    # Handles: "key":"value", "key":number, "key":true/false/null, "key":[{...}]
    pattern = r'"([^"]+)":(\[.*?\]|\{.*?\}|"(?:[^"\\]|\\.)*"|true|false|null|[\d\.\-]+)'
    matches = re.findall(pattern, s)
    for key, value in matches:
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            result[key] = value[1:-1]
        elif value == 'true':
            result[key] = True
        elif value == 'false':
            result[key] = False
        elif value == 'null':
            result[key] = None
        elif value.startswith('[') and value.endswith(']'):
            # For arrays, just keep as string or parse further if needed
            result[key] = value
        elif value.startswith('{') and value.endswith('}'):
            # For nested dicts, just keep as string or parse further if needed
            result[key] = value
        else:
            # Try to convert to int or float
            try:
                if '.' in value:
                    result[key] = float(value)
                else:
                    result[key] = int(value)
            except ValueError:
                result[key] = value
    return result

def json_str_to_df_row(json_str):
    """
    Converts a JSON-like string to a pandas DataFrame row without using json.loads.
    """
    try:
        data = parse_json_like_string(json_str)
    except Exception as e:
        print(f"ParseError: {e}")
        pdb.set_trace()
        raise
    df = pd.DataFrame([data])
    return df

if __name__ == "__main__":
    input_file = 'data/2025-06-27_storage_mart.html'  # Adjust filename as needed
    output_file = 'output.xlsx'
    text = read_file(input_file)
    info = extract_storage_info(text)
    if info:
        # Apply json_str_to_df_row to each value and concatenate results
        df_list = [json_str_to_df_row(json_str) for json_str in info.values()]
        df = pd.concat(df_list, ignore_index=True)
        df.to_excel(output_file, index=False)
        print(f"Extracted storage info saved to {output_file}")
    else:
        print("No storage info found.")