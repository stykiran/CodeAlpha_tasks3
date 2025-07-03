import re

# Input and output file paths
input_file = "sample.txt"
output_file = "emails.txt"

# Regular expression pattern for matching emails
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# Read text from input file
try:
    with open(input_file, 'r') as file:
        content = file.read()

    # Find all emails
    emails = re.findall(email_pattern, content)

    # Write emails to output file
    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')

    print(f"✅ {len(emails)} email(s) extracted and saved to {output_file}")

except FileNotFoundError:
    print(f"❌ File {input_file} not found.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")
