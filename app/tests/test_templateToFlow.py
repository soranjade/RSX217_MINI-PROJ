from pathlib import Path

txt = Path('flow.json').read_text()
print(txt)