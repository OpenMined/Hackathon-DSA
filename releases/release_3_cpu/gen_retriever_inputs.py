from pathlib import Path
import json

VERSIONS_DIR = "data/platform-docs-versions-english/"

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter

import os
import re

def list_folders(directory):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory.")
        return

    # List all items in the directory
    items = os.listdir(directory)

    # Filter out only the directories
    return [item for item in items if os.path.isdir(os.path.join(directory, item))]


def replace_alternate_headings(text):
    lines = text.split('\n')
    new_lines = []
    i = 0
    while i < len(lines):
        if i + 1 < len(lines) and lines[i].strip():
            # '=' underline headings
            if re.match(r'^=+$', lines[i + 1]):
                new_lines.append(f'# {lines[i]}')
                i += 2
                continue
            # '-' underline headings
            elif re.match(r'^-+$', lines[i + 1]):
                new_lines.append(f'## {lines[i]}')
                i += 2
                continue
        new_lines.append(lines[i])
        i += 1
    return '\n'.join(new_lines)


def find_substring_line(content, substring):
    all_lines = content.split('\n')

    substring_lines = substring.split('\n')
    for line_num, line in enumerate(all_lines):
        if substring_lines[0].strip(' ') == line.strip(' '):
            line_end = line_num + len(substring_lines)
            return line_num, line_end
    return None, None



def process_document(document, merge_h3=False):
    if merge_h3:
        headers_to_split = [("#", "H1"),("##", "H2")]
    
    headers_to_split = [("#", "H1"),("##", "H2"), ('###', "H3")]
    new_markdown = replace_alternate_headings(document.page_content)

    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split, strip_headers=False
    )
    md_header_splits = markdown_splitter.split_text(new_markdown)
    filtered_header_splits = []
    threshold = 6000 # length of allowed threshold

    metadata = item = None

    for d in md_header_splits:
        # skip if empty
        if len(d.page_content) <= 50:
            continue

        # add to previous if short and have exactly the same metadata
        if metadata == d.metadata.items() and item is not None and len(item) + d.page_content < threshold:
            item = item + '\n' + d.page_content
            filtered_header_splits[-1][0] = item
            continue
        
        # create a new split
        source = "Source document: " + document.metadata['source']
        metadata = d.metadata.items()
        hierarchy = "Paragraph location: " + '\n'
        for k, v in metadata:
            if k.startswith('H'):
                hierarchy = hierarchy + f"\t{v}\n"

        content = "Content: \n" + d.page_content  + '\n'
        
        item = f"{source}\n{hierarchy}\n{content}" 



        def extract_urls(text):
            if "Resource URL" in text:
                print('found')
                # Regular expression pattern to match URLs
                pattern = r'https?://\S+'

                # Find all matches using re.findall
                urls = re.findall(pattern, text)

                return urls[0]
            
            # Regular expression pattern to match URLs
            pattern = r'https?://\S+'

            # Find all matches using re.findall
            urls = re.findall(pattern, text)
            
            if len(urls):
                return urls[0]
            
            return document.metadata['source'].split('/')[-2] + '/' + document.metadata['source'].split('/')[-1]
        
        url = extract_urls(d.page_content)

        if new_markdown is not None and d.page_content is not None:
            line_start, line_end = find_substring_line(new_markdown, d.page_content)
            metadata=(line_start, line_end, url)
    
        filtered_header_splits.append((item, metadata))


    return filtered_header_splits

def save_splits(folder_name, file_name, splits):

    data = {}
    for idx, split in enumerate(splits):
        data[idx] = {
            'content': split[0],
            'line_start': split[1][0],
            'line_end': split[1][1],
            'url': split[1][2],
        }

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(f"{folder_name}/{file_name}", "w") as f:
        json.dump(data, f, indent=4)
        print(f"Dumping in {folder_name}...")


folders = list_folders(VERSIONS_DIR)

for folder in folders:
    full_path = VERSIONS_DIR + folder
    print(f"Looking in folder {full_path}")
    docs = DirectoryLoader(Path(VERSIONS_DIR + folder), glob="[!.]*.md", loader_cls=TextLoader).load()

    print(f"Found {len(docs)}")
    for doc in docs:
        splits = process_document(doc)
        save_splits(full_path.replace('data', 'data/_jsons'),  doc.metadata["source"].split('/')[-1].replace('.md', '.json'), splits) # test would be original folder name

