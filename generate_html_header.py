import os

print("Running generate_html_header.py script")
input_file = os.path.join("src", "homepage.html")
output_file = os.path.join("src", "htmlHomePage.h")

with open(input_file, "r") as infile:
  html_content = infile.read()

header_content = f'''#pragma once

const char HTML_HOMEPAGE_CONTENT[] PROGMEM = R"HTMLHOMEPAGE(
{html_content}
)HTMLHOMEPAGE";
'''

with open(output_file, "w") as outfile:
  outfile.write(header_content)