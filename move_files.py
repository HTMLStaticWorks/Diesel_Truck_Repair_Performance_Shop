import os
import glob

html_files = glob.glob('pages/*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('../assets', 'assets')
    
    filename = os.path.basename(file)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    os.remove(file)
print('Moved and updated html files')
