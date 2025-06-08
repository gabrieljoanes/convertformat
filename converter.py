import json

def convert_examples(data):
    converted = []
    for item in data:
        input_text = item["paragraph_a"].strip() + "\n" + item["paragraph_b"].strip()
        output_text = item["transition"].strip()
        converted.append({
            "input": input_text,
            "output": output_text
        })
    return converted

def convert_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    converted = convert_examples(data)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(converted, f, ensure_ascii=False, indent=2)
