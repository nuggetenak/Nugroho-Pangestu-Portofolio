import re, subprocess, sys, html

src = open('resume.html').read()
body = src.split('<body>',1)[1]
body = re.sub(r'<[^>]+>', ' ', body)
body = html.unescape(body)

# every hyphenated compound in the source
compounds = sorted(set(re.findall(r'\w+(?:-\w+)+', body)))

txt = subprocess.run(['pdftotext','Nugroho-Pangestu-Resume.pdf','-'],
                     capture_output=True, text=True).stdout
flat = re.sub(r'\s+', ' ', txt)

broken = []
for c in compounds:
    if c in flat:
        continue
    squashed = c.replace('-', '')
    if squashed in re.sub(r'\s+','',txt):
        broken.append((c, squashed))

print(f"hyphenated compounds in source : {len(compounds)}")
print(f"BROKEN by line-end de-hyphenation: {len(broken)}")
for c, s in broken:
    print(f"   {c!r}  ->  parsed as  {s!r}")
sys.exit(1 if broken else 0)
