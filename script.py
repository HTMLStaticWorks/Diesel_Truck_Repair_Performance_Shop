import sys
with open('pages/index.html', 'r') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<!-- Feature 4 -->' in line:
        # find the end of section 2
        for j in range(i, len(lines)):
            if '</section>' in lines[j]:
                start_idx = j
                break
    if 'UNCOMPROMISING <span class="text-accent">PERFORMANCE</span>' in line:
        # this is inside section 4 col-lg-5
        # we want to replace up to the div before it
        for j in range(i, -1, -1):
            if '<div class="col-lg-5 offset-lg-1 reveal-right">' in lines[j]:
                end_idx = j
                break

if start_idx != -1 and end_idx != -1:
    with open('restore.txt', 'r') as f2:
        restore_content = f2.readlines()
    
    new_lines = lines[:start_idx+1] + restore_content + lines[end_idx:]
    with open('pages/index.html', 'w') as f3:
        f3.writelines(new_lines)
    print("Successfully restored!")
else:
    print("Could not find boundaries", start_idx, end_idx)
