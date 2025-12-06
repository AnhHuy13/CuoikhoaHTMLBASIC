import os
import re

base_dir = "/Users/mangoking/desktop/html/cuoikhoa" 
html_dir = os.path.join(base_dir, "html")
css_dir = os.path.join(base_dir, "css")

files_updated = 0
files_skipped = 0

def alert(msg):
    print(f"\033[1;31m!!! {msg} !!!\033[0m")

def extract_current_title(content):
    """Trích xuất nội dung giữa thẻ <title>...</title> từ nội dung HTML."""
    match = re.search(r'<title>(.*?)</title>', content, re.DOTALL | re.IGNORECASE)
    if match:
        if 'ACTION REQUIRED' in match.group(1):
            return "Khám phá"
        return match.group(1).strip()
    return "Khám phá"

def generate_new_html_content(css_relative_path, current_title):
    """Tạo cấu trúc HTML mới theo mẫu, với body hoàn toàn trống."""
    
    final_title = current_title if current_title else "Khám phá"
    
    empty_body = """
  <body>
  
  </body>
"""
    
    return f"""<!DOCTYPE html>
<html lang="vi">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{final_title}</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Maven+Pro:wght@400;500;600;700&display=swap"
      rel="stylesheet"
    />
    <link
      rel="icon"
      type="image/png"
      href="https://cdn.haitrieu.com/wp-content/uploads/2022/01/Icon-Bamboo-Airways.png"
    />
    <link rel="stylesheet" href="{css_relative_path}" />
    <link rel="stylesheet" href="../../css/navbar.css" />
    <link rel="stylesheet" href="../css/footer.css" />
  </head>
  <style>
    body {{
      font-family: "Maven Pro", sans-serif;
      margin: 0;
      padding: 0;
    }}
  </style>{empty_body}
</html>
"""


for root, dirs, files in os.walk(html_dir):
    for file in files:
        if file.endswith(".html"):
            html_path = os.path.join(root, file)
            
            relative_path = os.path.relpath(root, html_dir)
            css_subdir = os.path.join(css_dir, relative_path)
            os.makedirs(css_subdir, exist_ok=True)
            
            css_file_name = file.replace(".html", ".css")
            css_path = os.path.join(css_subdir, css_file_name)
            
            if not os.path.exists(css_path):
                with open(css_path, "w") as f:
                    f.write(f"")
                alert(f"Tạo CSS: {css_path}")
            
            try:
                with open(html_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
            except UnicodeDecodeError:
                alert(f"Không thể đọc file {html_path} với encoding utf-8. Bỏ qua.")
                files_skipped += 1
                continue
            
            current_title = extract_current_title(content)
            
            if relative_path == ".":
                css_relative_link = f"../css/{css_file_name}"
            else:
                css_relative_link = f"{'../' * relative_path.count(os.sep)}../css/{relative_path.replace(os.sep,'/')}/{css_file_name}"

            body_empty_check = re.search(r'<body\b[^>]*>\s*</body>', content, re.DOTALL | re.IGNORECASE)

            if len(content) == 0 or body_empty_check:
                
                new_content = generate_new_html_content(css_relative_link, current_title)
                
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                    
                alert(f"CẬP NHẬT HOÀN TOÀN ({file}): Giữ lại Title: '{current_title}' (Body Rỗng)")
                files_updated += 1
            else:
                files_skipped += 1
                print(f"--- BỎ QUA ({file}): Đã có nội dung trong <body>. Title: '{current_title}'")

print("\n" + "="*70)
print(" KẾT QUẢ XỬ LÝ TOÀN BỘ FILE HTML".center(70))
print("="*70)

print(f"{'Tổng số file quét:':35} {files_updated + files_skipped}")
print(f"{'Số file đã cập nhật/tạo mới:':35} {files_updated} ({(files_updated / (files_updated+files_skipped)) * 100}%)")
print(f"{'Số file bị bỏ qua:':35} {files_skipped}  ({(files_skipped / (files_updated+files_skipped)) * 100}%)")

print("-"*70)

if files_updated > 0:
    print(" Danh mục file được cập nhật:".ljust(70))
    print("  - Các file có <body> rỗng hoặc file trống".ljust(70))

if files_skipped > 0:
    print("\n Danh mục file bị bỏ qua:".ljust(70))
    print("  - Các file đã có nội dung <body> nên không ghi đè".ljust(70))

print("="*70)
print(" Hoàn tất xử lý.")
print("="*70)
