import os
import subprocess

input_dir = "data/platform-docs-snapshots"
output_dir = "data/platform-docs-versions"

for filename in os.listdir(input\_dir):
    if filename.endswith(".pdf"):
        input_pdf_path = os.path.join(input_dir, filename)

        output_filename = os.path.splitext(filename)[0] + ".md"
        output_file_path = os.path.join(output_dir, output_filename)

        subprocess.run(["nougat", input_pdf_path, "-o", output_dir, "--markdown"])

