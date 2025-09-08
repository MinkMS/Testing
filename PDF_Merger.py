import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PyPDF2 import PdfMerger

def merge_pdfs():

    root = tk.Tk()
    root.withdraw()


    file_paths = filedialog.askopenfilenames(
        title="Chọn các file PDF để merge",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not file_paths:
        messagebox.showinfo("Thông báo", "Bạn chưa chọn file nào!")
        return


    output_file = simpledialog.askstring("Tên file xuất ra", "Nhập tên file PDF xuất ra (không cần .pdf):")
    if not output_file:
        messagebox.showinfo("Thông báo", "Bạn chưa nhập tên file xuất ra!")
        return

    output_file += ".pdf"


    merger = PdfMerger()
    for pdf in file_paths:
        merger.append(pdf)

    try:
        merger.write(output_file)
        merger.close()
        messagebox.showinfo("Thành công", f"Merge hoàn tất! File lưu tại: {output_file}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu file: {e}")

if __name__ == "__main__":
    merge_pdfs()
