# convert_encoding.py

input_file = 'quotes.json'
output_file = 'quotes_fixed.json'

encodings_to_try = ['utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'latin-1', 'cp1252']

for enc in encodings_to_try:
    try:
        with open(input_file, 'r', encoding=enc) as f:
            content = f.read()
            print(f"✅ Successfully read using encoding: {enc}")
            break
    except UnicodeDecodeError:
        print(f"❌ Failed with encoding: {enc}")
else:
    raise Exception("❌ Could not read the file with any known encoding.")

# Save it back in UTF-8
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Encoding converted and saved to {output_file}")
