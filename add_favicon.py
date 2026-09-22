import os

files = [f for f in os.listdir('pages') if f.endswith('.html')]

favicon_link = '\n    <!-- Favicon -->\n    <link rel="icon" type="image/svg+xml" href="../assets/images/favicon.svg">\n'

for file in files:
    path = os.path.join('pages', file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'favicon.svg' not in content:
        head_end = content.find('</head>')
        if head_end != -1:
            content = content[:head_end] + favicon_link + content[head_end:]
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Added to " + file)
