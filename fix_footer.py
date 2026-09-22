import os

files = [f for f in os.listdir('pages') if f.endswith('.html')]

for file in files:
    path = os.path.join('pages', file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('<h5>Quick Links</h5>', '<h6 class="mb-3 text-uppercase fw-bold" style="letter-spacing: 1px; color: var(--accent);">Quick Links</h6>')
    content = content.replace('<h5>Our Services</h5>', '<h6 class="mb-3 text-uppercase fw-bold" style="letter-spacing: 1px; color: var(--accent);">Our Services</h6>')
    content = content.replace('<h5>Contact Info</h5>', '<h6 class="mb-3 text-uppercase fw-bold" style="letter-spacing: 1px; color: var(--accent);">Contact Info</h6>')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
print("Replaced footer headings")
