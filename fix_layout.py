import os

files = [f for f in os.listdir('pages') if f.endswith('.html')]

for file in files:
    path = os.path.join('pages', file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('class="col-md-4"', 'class="col-md-6 col-lg-4"')
    content = content.replace('class="col-md-4 ', 'class="col-md-6 col-lg-4 ')
    
    # Add justify-content-center to row g-4 (unless it already has it)
    content = content.replace('class="row g-4"', 'class="row g-4 justify-content-center"')
    content = content.replace('class="row g-4 justify-content-center justify-content-center"', 'class="row g-4 justify-content-center"')
    
    content = content.replace('row-cols-2', 'row-cols-1')
    
    content = content.replace('class="col-6"', 'class="col-12 col-sm-6"')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()
if 'html, body {' not in css:
    css = css.replace('body {', 'html, body {\n    overflow-x: hidden;')
with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done")
