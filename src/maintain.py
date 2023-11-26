import json

scan_folder = 'algorithm/'
#ipynb를 json으로 보는법: 문서 빈 공간에 우클릭 - Edit Cell Tags (JSON)
def scan_broken_links(): 
  """Scan broken links in ipynb"""

  with open(scan_folder, 'r', encoding='utf-8') as file:
    data = json.load(file)
  
  for cell in data.get('cells', []):
    if cell.get('cell_type') != 'markdown': continue
    for line in cell['source'] :
      if line.startswith('!['):
        pass #TODO: 이미지 링크 검사