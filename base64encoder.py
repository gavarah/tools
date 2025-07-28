import base64
import argparse

# Set up command-line arguments
parser = argparse.ArgumentParser(description="Base64 encode a PEM certificate file.")
parser.add_argument("input_file", help="Path to the input PEM file")
parser.add_argument("output_file", help="Path to the output base64-encoded file")

args = parser.parse_args()

# Read the PEM certificate(s)
with open(args.input_file, "r") as infile:
    pem_content = infile.read()

# Base64 encode
encoded_content = base64.b64encode(pem_content.encode("utf-8")).decode("utf-8")

# Write the encoded content to output file
with open(args.output_file, "w") as outfile:
    outfile.write(encoded_content)

print(f"Base64-encoded certificate saved to '{args.output_file}'")
