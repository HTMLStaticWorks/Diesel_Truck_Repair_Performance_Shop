import os

files = [f for f in os.listdir('pages') if f.endswith('.html')]

for file in files:
    path = os.path.join('pages', file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # ensure we haven't already wrapped it
    if 'div style="overflow-x: hidden' not in content:
        nav_end = content.find('</nav>')
        if nav_end != -1:
            insert_pos = nav_end + 6
            content = content[:insert_pos] + '\n<div style="overflow-x: hidden; width: 100%;">\n' + content[insert_pos:]
            
            body_end = content.find('</body>')
            if body_end != -1:
                content = content[:body_end] + '</div>\n' + content[body_end:]
                
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Fixed " + file)

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('overflow-x: hidden;', '')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("CSS fixed")
