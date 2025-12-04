import os
import sys
import inquirer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

TARGET_DIR = "html/Diemden"


HEADER_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{page_title}</title>
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
    <link rel="stylesheet" href="../../css/Diemden/Hanoi.css" />
    <link rel="stylesheet" href="../../css/navbar.css" />
    <link rel="stylesheet" href="../../css/footer.css" />
  </head>
  <body>
    <nav class="navbar bg-light">
      <div class="navbar-container">
        <div class="navbar-left">
          <a class="navbar-brand" href="../trangchu.html">
            <img
              src="https://www.bambooairways.com/o/wpbav-home-theme/css/assets/logo.png"
              alt="Logo"
              height="40"
            />
          </a>
        </div>
        <div class="navbar-center">
          <ul class="navbar-nav main-menu">
            <li class="nav-item">
              <a class="nav-link" href="Khampha/khampha.html">Khám phá</a>
            </li>
            <li class="nav-item"><a class="nav-link" href="#">Đặt vé</a></li>
            <li class="nav-item">
              <a class="nav-link" href="#">Thông tin hành trình</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="../BambooClub/GioithieuQuyenloi.html"
                >Bamboo Club</a
              >
            </li>
          </ul>
        </div>
        <div class="navbar-right">
          <ul class="navbar-nav right-menu">
            <li class="signin-li">
              <a class="signin-option-navbar" href="#">Đăng nhập</a>
            </li>
            <li><a class="signup-option-navbar" href="#">Đăng ký</a></li>
            <li>
              <img
                src="https://www.bambooairways.com/o/com.bav.header.languages/assets/Unlogin_Avatar.png"
                alt="Avatar"
                height="20"
                width="20"
              />
            </li>
          </ul>
        </div>
      </div>
    </nav>
"""

CAROUSEL_TEMPLATE = """
    <div
      id="carouselExampleInterval"
      class="carousel slide"
      data-bs-ride="carousel"
    >
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="2000">
          <img
            src="{carousel_url}"
            class="d-block w-100"
            alt="Banner-{page_title}"
          />
        </div>
      </div>
    </div>
"""

MAIN_CONTENT_HEADER = """
    <div class="main-content">
      <h2>{main_title}</h2>
      <p>{main_content_p1}</p>
      <p>{main_content_p2}</p>
      <h3>KHÁM PHÁ</h3>

      <div class="navigation-tabs">
        <a href="#canhdep-panel" class="tab-button active">CẢNH ĐẸP</a>
        <a href="#amthuc-panel" class="tab-button">ẨM THỰC</a>
        <div class="tab-divider"></div>
      </div>

      <div class="tab-content-wrapper">
"""

CONTENT_PANEL_TEMPLATE = """
        <div id="{panel_id}" class="tab-panel">
          <h4>{panel_title}</h4>
          <div class="kham-pha-container">
            {panel_content}
          </div>
        </div>
"""

CONTAINER_TEMPLATE = """
            <div class="container-1">
              <img
                src="{image_url}"
                alt="{alt_text}"
              />
              <p>{text_content}</p>
            </div>
"""

FOOTER_TEMPLATE = """
      </div>
    </div>
    <footer>
        <div class="slogan-and-logo-footer">
            <img
            src="https://www.bambooairways.com/o/wpbav-home-theme/css/assets/logo.png"
            alt="Icon-Bamboo-Airways"
            height="50"
            />
            <div class="divider-footer-logo"></div>
            <h5>HƠN CẢ MỘT CHUYẾN BAY</h5>
        </div>
        <div class="divider-footer"></div>
        <div class="install-qr-footer">
            <div class="install-app-qr">
            <img
                src="https://www.bambooairways.com/documents/20122/770343/app.png/4074ab42-5f15-760b-9bb7-5d522d7ff200?t=1697600790190"
                alt="qr_code_install_app"
                width="70"
                height="70"
            />
            <div class="install-app-qr-content">
                <h6>Cài đặt ứng dụng</h6>
                <p>Quét mã ngay để cài đặt từ các</p>
                <p>cửa hàng ứng dụng!</p>
            </div>
            </div>
            <div class="install-sticker-qr">
            <img
                src="https://www.bambooairways.com/documents/20122/770343/viber-bamboo.png/a21d4733-0669-665b-4b16-a12e153b7098?t=1697600790190"
                alt="qr_code_install_sticker"
                width="70"
                height="70"
            />
            <div class="install-sticker-qr-content">
                <h6>Cài đặt nhãn dán</h6>
                <p>Quét mã ngay để sở hữu bộ nhãn dán Viber!</p>
            </div>
            </div>
        </div>
        <div class="divider-footer"></div>
        <div class="chooser-footer">
            <div class="bambooairways-footer">
            <h5>Bamboo Airways</h5>
            <div class="bambooairways-footer-choice">
                <a href="../BambooAirways/gioithieu.html"
                >Giới thiệu về Bamboo Airways</a
                >
                <a href="../BambooAirways/thongdiep.html"
                >Thông điệp của Bamboo Airways</a
                >
                <a href="../BambooAirways/nhandienthuonghieu.html"
                >Nhận diện thương hiệu</a
                >
            </div>
            </div>
            <div class="dieukhoanphaply-footer">
            <h5>Điều khoản & Pháp lý</h5>
            <div class="bambooairways-footer-choice">
                <a href="../Dieukhoan/dieukhoan.html">Điều khoản sử dụng website</a>
            </div>
            </div>
            <div class="camnangdulich-footer">
            <h5>Cẩm nang Du lịch</h5>
            <div class="bambooairways-footer-choice">
                <a href="../Camnangdulich/tipdulich.html"
                >Chia sẻ Mẹo (Tips Du Lịch)</a
                >
            </div>
            </div>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
"""


def edit_item_data(data, key, message, is_editor=False):
    """Mở trình soạn thảo/text input cho một key dữ liệu cụ thể."""
    
    input_type = inquirer.Editor if is_editor else inquirer.Text
    
    questions = [
        input_type(key, message=f"[CHỈNH SỬA] {message}", default=data.get(key, ''))
    ]
    
    answers = inquirer.prompt(questions)
    
    if answers and answers.get(key) is not None:
        data[key] = answers[key]
    return data

def edit_tab_item(item_data, tab_name, item_index):
    """Mở trình soạn thảo/text input cho một item trong Tab (URL và Text)."""
    
    questions = [
        inquirer.Text('img_url', message="URL Hình ảnh", default=item_data.get('img_url', '')),
        inquirer.Editor('text', message="Nội dung Văn bản", default=item_data.get('text', '')),
        inquirer.Confirm('delete', message="XÓA mục này?", default=False)
    ]
    
    answers = inquirer.prompt(questions)
    
    if answers['delete']:
        console.print(f"[bold red]❌ Đã xóa Mục {item_index + 1} khỏi Tab {tab_name}[/bold red]")
        return True
    
    img_url = answers.get('img_url', '').strip()
    text = answers.get('text', '').strip()
    
    if img_url and text:
        item_data['img_url'] = img_url
        item_data['text'] = text
        console.print(f"[bold green]✅ Đã cập nhật Mục {item_index + 1}[/bold green]")
        return item_data
    else:
        console.print("[bold red]❗ Không thể cập nhật: URL và Nội dung không được để trống.[/bold red]")
        return False

def get_general_data_inquirer(initial_data=None):
    """Thu thập dữ liệu chung của trang, sử dụng editor cho đoạn văn."""
    
    data = initial_data if initial_data is not None else {}
    
    questions = [
        inquirer.Text('page_title', message="1. Tên trang (<title>)", default=data.get('page_title', '')),
        inquirer.Text('carousel_url', message="2. URL hình ảnh Banner Carousel", default=data.get('carousel_url', '')),
        inquirer.Text('main_title', message="3. Tiêu đề chính (H2)", default=data.get('main_title', '')),
        inquirer.Editor('p1', message="4. Đoạn văn giới thiệu thứ nhất", default=data.get('p1', '')),
        inquirer.Editor('p2', message="5. Đoạn văn giới thiệu thứ hai (Lời kêu gọi)", default=data.get('p2', '')),
    ]
    answers = inquirer.prompt(questions)
    
    for key, value in answers.items():
        if value is None:
            answers[key] = ""
    return answers


def build_tab_content_inquirer(tab_name, tab_id, initial_content=[]):
    """Xây dựng nội dung cho một tab, chỉ thêm mới, không chỉnh sửa ở đây."""
    
    current_items = initial_content
    
    while True:
        add_more = inquirer.prompt([
            inquirer.Confirm('add_item', message=f"Bạn muốn thêm Mục {len(current_items) + 1} vào Tab '{tab_name}' không?", default=False)
        ])
        
        if not add_more['add_item']:
            break
            
        new_item_questions = [
            inquirer.Text('img_url', message="URL Hình ảnh"),
            inquirer.Editor('text', message="Nội dung Văn bản"),
        ]
        new_answers = inquirer.prompt(new_item_questions)
        
        img_url = new_answers.get('img_url', '').strip()
        text = new_answers.get('text', '').strip()

        if img_url and text:
            current_items.append({
                'img_url': img_url,
                'text': text,
                'alt_text': f"{tab_name} - Mục {len(current_items) + 1}"
            })
            console.print(f"[bold green]✅ Đã thêm Mục {len(current_items)}[/bold green]")
        else:
            console.print("[bold red]❗ Bỏ qua: Mục này thiếu URL hoặc Nội dung Văn bản. Vui lòng điền đầy đủ.[/bold red]")

    html_content = "".join([
        CONTAINER_TEMPLATE.format(
            image_url=item['img_url'],
            alt_text=f"{tab_name} - Mục {i + 1}",
            text_content=item['text']
        ) for i, item in enumerate(current_items)
    ])
            
    return CONTENT_PANEL_TEMPLATE.format(
        panel_id=tab_id,
        panel_title=tab_name,
        panel_content=html_content
    ), current_items



def review_and_edit_data(file_name, all_data):
    """Trang Review chính, cho phép dùng phím lên/xuống để chọn chỉnh sửa."""
    
    def update_tab_html(data, tab_key, tab_name, panel_id):
        """Hàm nội bộ để tái tạo HTML của Tab sau khi chỉnh sửa item."""
        html_content = "".join([
            CONTAINER_TEMPLATE.format(
                image_url=item['img_url'], 
                alt_text=f"{tab_name} - Mục {i + 1}", 
                text_content=item['text']
            ) for i, item in enumerate(data[tab_key])
        ])
        data[f'{tab_key}_html'] = CONTENT_PANEL_TEMPLATE.format(
            panel_id=panel_id, panel_title=tab_name, panel_content=html_content
        )

    while True:
        console.print(Panel(f"🔥 [bold yellow]BƯỚC 3: REVIEW VÀ CHỈNH SỬA - {file_name}[/bold yellow] 🔥", border_style="yellow", expand=False))
        
        options = []
        
        options.append(f"[GENERAL] Tên trang: {all_data['page_title']}")
        options.append(f"[GENERAL] URL Banner: {all_data['carousel_url']}")
        options.append(f"[GENERAL] Tiêu đề Chính: {all_data['main_title']}")
        
        console.print("\n[bold cyan]--- TÓM TẮT NỘI DUNG ---[/bold cyan]")
        console.print(f"Đoạn 1:\n[dim]{Text(all_data['p1'], overflow='ellipsis')}[/dim]")
        options.append(f"[GENERAL] Đoạn 1")

        console.print(f"\nĐoạn 2:\n[dim]{Text(all_data['p2'], overflow='ellipsis')}[/dim]")
        options.append(f"[GENERAL] Đoạn 2")

        options.append("--- CẢNH ĐẸP ---")
        for i, item in enumerate(all_data['canhdep_items']):
            options.append(f"[CĐ] Mục {i+1}: URL={item['img_url'][:30]}... | Text={item['text'].splitlines()[0][:30]}...")
        options.append("[CĐ] [+] Thêm Mục Mới")

        options.append("--- ẨM THỰC ---")
        for i, item in enumerate(all_data['amthuc_items']):
            options.append(f"[AT] Mục {i+1}: URL={item['img_url'][:30]}... | Text={item['text'].splitlines()[0][:30]}...")
        options.append("[AT] [+] Thêm Mục Mới")
        
        options.append("--- HÀNH ĐỘNG ---")
        options.append("[s] LƯU FILE VÀ THOÁT")
        options.append("[q] THOÁT KHÔNG LƯU")
        
        questions = [
            inquirer.List(
                'selection',
                message="Dùng phím lên/xuống/Enter để chọn mục cần chỉnh sửa",
                choices=options,
                carousel=True
            )
        ]
        
        answers = inquirer.prompt(questions)
        if not answers:
             console.print("[bold red]Đã hủy. Chương trình thoát mà không lưu file.[/bold red]")
             sys.exit(0)
             
        selected = answers['selection']

        if selected == "[s] LƯU FILE VÀ THOÁT":
            if save_confirmation_final(file_name, all_data):
                sys.exit(0)
            
        elif selected == "[q] THOÁT KHÔNG LƯU":
            console.print("[bold red]Đã hủy. Chương trình thoát mà không lưu file.[/bold red]")
            sys.exit(0)
            
        elif selected.startswith("[GENERAL]"):
            key_map = {
                "Tên trang": ('page_title', False), "URL Banner": ('carousel_url', False), 
                "Tiêu đề Chính": ('main_title', False), "Đoạn 1": ('p1', True), "Đoạn 2": ('p2', True)
            }
            
            property_name = selected.split(']')[1].strip().split(':')[0].strip()
            key, is_editor = key_map.get(property_name, (None, False))
            
            if key:
                all_data = edit_item_data(all_data, key, property_name, is_editor)
                
        elif selected.startswith("[CĐ]") or selected.startswith("[AT]"):
            
            is_canhdep = selected.startswith("[CĐ]")
            tab_key = 'canhdep_items' if is_canhdep else 'amthuc_items'
            tab_name = 'Cảnh đẹp' if is_canhdep else 'Ẩm thực'
            
            if "Thêm Mục Mới" in selected:
                new_item_questions = [
                    inquirer.Text('img_url', message="URL Hình ảnh"),
                    inquirer.Editor('text', message="Nội dung Văn bản"),
                ]
                new_answers = inquirer.prompt(new_item_questions)
                
                img_url = new_answers.get('img_url', '').strip()
                text = new_answers.get('text', '').strip()

                if img_url and text:
                    all_data[tab_key].append({
                        'img_url': img_url, 'text': text, 'alt_text': f"{tab_name} - Mục {len(all_data[tab_key]) + 1}"
                    })
                    console.print(f"[bold green]✅ Đã thêm Mục mới vào Tab {tab_name}[/bold green]")
                else:
                    console.print("[bold red]❗ Không thể thêm: Thiếu URL hoặc Nội dung Văn bản.[/bold red]")
            else:
                item_index = int(selected.split('Mục ')[1].split(':')[0].strip()) - 1
                
                result = edit_tab_item(all_data[tab_key][item_index], tab_name, item_index)
                
                if result is True:
                    all_data[tab_key].pop(item_index)
                    
        update_tab_html(all_data, 'canhdep_items', 'Cảnh đẹp', "canhdep-panel")
        update_tab_html(all_data, 'amthuc_items', 'Ẩm thực', "amthuc-panel")



def assemble_full_html(data):
    """Lắp ráp toàn bộ chuỗi HTML."""
    
    final_html = HEADER_TEMPLATE.format(page_title=data.get('page_title', ''))
    final_html += CAROUSEL_TEMPLATE.format(carousel_url=data.get('carousel_url', ''), page_title=data.get('page_title', ''))
    
    final_html += MAIN_CONTENT_HEADER.format(
        main_title=data.get('main_title', ''),
        main_content_p1=data.get('p1', ''),
        main_content_p2=data.get('p2', '')
    )
    
    final_html += data.get('canhdep_html', '')
    final_html += data.get('amthuc_html', '')
    
    final_html += FOOTER_TEMPLATE
    return final_html


def get_file_list(directory):
    if not os.path.isdir(directory):
        console.print(f"[bold red]Lỗi: Thư mục '{directory}' không tồn tại. Đã tạo thư mục.[/bold red]")
        os.makedirs(directory)
    files = [f for f in os.listdir(directory) if f.endswith('.html')]
    files.append("TẠO FILE MỚI")
    return files

def select_target_file(files):
    questions = [
        inquirer.List(
            'target',
            message="Chọn file HTML bạn muốn ghi đè hoặc chọn TẠO FILE MỚI",
            choices=files,
            carousel=True
        )
    ]
    answers = inquirer.prompt(questions)
    return answers['target'] if answers else None

def save_confirmation_final(file_to_save, data):
    """Thực hiện lưu file cuối cùng."""
    final_html = assemble_full_html(data)
    full_path = os.path.join(TARGET_DIR, file_to_save)
    
    try:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(final_html)
        console.print(Panel(f"[bold green]LƯU THÀNH CÔNG! File đã được ghi tại: {full_path}[/bold green]", border_style="green"))
        return True
    except Exception as e:
        console.print(f"[bold red]Lỗi khi ghi file: {e}[/bold red]")
        return False

def main_script():
    console.print(Panel("✨ [bold white on blue]TRÌNH TẠO TRANG ĐÍCH CHUYÊN NGHIỆP (BAMBOO AIRWAYS STYLE)[/bold white on blue] ✨"))

    available_files = get_file_list(TARGET_DIR)
    selected_option = select_target_file(available_files)

    if selected_option is None:
        console.print("[bold red]Đã hủy bỏ chương trình.[/bold red]")
        return

    if selected_option == "TẠO FILE MỚI":
        file_to_save = input("Nhập tên file mới (ví dụ: DaLat.html, không cần đường dẫn): ")
        if not file_to_save.endswith('.html'):
             file_to_save += '.html'
        
    else:
        file_to_save = selected_option
    
    all_data = {
        'page_title': '', 'carousel_url': '', 'main_title': '', 'p1': '', 'p2': '',
        'canhdep_items': [], 'amthuc_items': [], 
        'canhdep_html': '', 'amthuc_html': ''
    }
    
    console.print(Panel("[bold yellow]BƯỚC 1: THÔNG TIN CHUNG CỦA TRANG[/bold yellow]", border_style="cyan"))
    general_data = get_general_data_inquirer(all_data)
    all_data.update(general_data)

    console.print(Panel("[bold yellow]BƯỚC 2: NHẬP NỘI DUNG TABS (TẠM THỜI)[/bold yellow]", border_style="cyan"))
    
    canhdep_html, all_data['canhdep_items'] = build_tab_content_inquirer("Cảnh đẹp", "canhdep-panel", all_data['canhdep_items'])
    all_data['canhdep_html'] = canhdep_html
    
    amthuc_html, all_data['amthuc_items'] = build_tab_content_inquirer("Ẩm thực", "amthuc-panel", all_data['amthuc_items'])
    all_data['amthuc_html'] = amthuc_html
    
    review_and_edit_data(file_to_save, all_data)

if __name__ == "__main__":
    main_script()