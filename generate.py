#!/usr/bin/env python3

import os
import markdown
from jinja2 import Environment, FileSystemLoader, Markup, select_autoescape

env = Environment(
        loader = FileSystemLoader('templates'),
        autoescape = select_autoescape(['html', 'xml'])
        )

def ProcessPage(filename):
    md = open(filename, "r").read()
    md_html = markdown.markdown(md, extensions = ['extra', 'tables', 'smarty'],
                                output_format = 'html5')
    template = env.get_template('default.html')
    out = open(os.path.splitext(filename)[0] + ".html", "w")
    out.write(template.render(page = "UWaterloo CS Co-op Program",
                              bodytxt = Markup(md_html)))
    out.close()

files = os.listdir()
for f in files:
    if f.endswith(".md"):
        ProcessPage(f)

