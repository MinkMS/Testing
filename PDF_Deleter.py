import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import os
import tempfile

# Simple GUI PDF deleter.
# - Opens file dialog to select multiple PDFs
# - Asks whether to overwrite or create new files
# - Deletes the first and last page of each selected PDF

def _unique_path(path):
    """Return a non-colliding path by adding a numeric suffix if needed."""
    base, ext = os.path.splitext(path)
    candidate = path
    i = 1
    while os.path.exists(candidate):
        candidate = f"{base}_{i}{ext}"
        i += 1
    return candidate

def delete_first_last_pages():
    """Pick PDFs and remove first+last page from each, then show a single summary message."""
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="Chọn các file PDF để xóa trang đầu và trang cuối",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not file_paths:
        messagebox.showinfo("Thông báo", "Bạn chưa chọn file nào!")
        return

    choice = simpledialog.askstring("Lựa chọn", "Nhập 'o' để ghi đè lên file gốc hoặc 'n' để tạo file mới:")
    if choice not in ('o', 'n'):
        messagebox.showinfo("Thông báo", "Lựa chọn không hợp lệ hoặc bạn đã hủy!")
        return

    processed = 0
    skipped = []
    errors = []

    for pdf_path in file_paths:
        try:
            reader = PdfReader(pdf_path)
            writer = PdfWriter()

            num_pages = len(reader.pages)
            if num_pages <= 2:
                skipped.append(os.path.basename(pdf_path))
                continue

            for i in range(1, num_pages - 1):
                writer.add_page(reader.pages[i])

            if choice == 'o':
                # Write to a temp file first, then replace original to avoid corruption on failure.
                dir_name, name = os.path.split(pdf_path)
                base, ext = os.path.splitext(name)
                fd, tmp_path = tempfile.mkstemp(prefix=base + "_tmp_", suffix=ext, dir=dir_name)
                os.close(fd)
                try:
                    with open(tmp_path, "wb") as out_file:
                        writer.write(out_file)
                    os.replace(tmp_path, pdf_path)
                finally:
                    if os.path.exists(tmp_path):
                        try:
                            os.remove(tmp_path)
                        except Exception:
                            pass
            else:
                base, ext = os.path.splitext(pdf_path)
                out_candidate = f"{base}_modified{ext}"
                out_path = _unique_path(out_candidate)
                with open(out_path, "wb") as out_file:
                    writer.write(out_file)

            processed += 1

        except Exception as e:
            errors.append(f"{os.path.basename(pdf_path)}: {e}")
            continue

    # Build and show a single summary message in logical order.
    summary_lines = []
    if processed:
        summary_lines.append(f"Đã xử lý: {processed} file.")
    if skipped:
        summary_lines.append(f"Bỏ qua {len(skipped)} file (<= 2 trang): " + ", ".join(skipped))
    if errors:
        summary_lines.append(f"Lỗi xảy ra với {len(errors)} file:")
        # show only filenames and short messages to keep the dialog readable
        summary_lines.extend(errors[:10])  # limit list length in dialog
        if len(errors) > 10:
            summary_lines.append(f"...và {len(errors)-10} file khác.")

    if not processed and not errors:
        # Nothing was done (all skipped)
        messagebox.showinfo("Kết quả", "Không có file nào được thay đổi.")
    else:
        # If there were errors, show an error dialog; otherwise show success.
        if errors:
            messagebox.showerror("Kết quả - Có lỗi", "\n".join(summary_lines))
        else:
            messagebox.showinfo("Thành công", "\n".join(summary_lines))

if __name__ == "__main__":
    delete_first_last_pages()