import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PyPDF2 import PdfMerger

"""
Simple GUI PDF merger.
- Opens file dialog to select multiple PDFs
- Asks for an output filename
- Merges selected PDFs into the output file
Notes / suggestions:
- Requires PyPDF2 installed: pip install PyPDF2
- Running this script will show GUI dialogs (no main window displayed)
- Consider adding validation for overwriting existing files or choosing output path
- For large PDFs or many files, consider using streaming/temporary files to reduce memory usage
"""

def merge_pdfs():
    """Open dialogs to pick PDFs and merge them into a single output PDF.
    Uses tkinter dialogs:
    - filedialog.askopenfilenames for input selection
    - simpledialog.askstring for output filename
    - messagebox for user feedback
    """
    # Create a hidden root window so dialogs can appear without an extra main window
    root = tk.Tk()
    root.withdraw()

    # Ask the user to pick PDF files.
    file_paths = filedialog.askopenfilenames(
        title="Chọn các file PDF để merge",
        filetypes=[("PDF files", "*.pdf")]
    )

    # If the user cancelled the selection, notify and exit.
    if not file_paths:
        messagebox.showinfo("Thông báo", "Bạn chưa chọn file nào!")
        return

    # Ask for the output filename (without .pdf). simpledialog returns None if cancelled.
    output_file = simpledialog.askstring("Tên file xuất ra", "Nhập tên file PDF xuất ra (không cần đuôi .pdf):")
    if not output_file:
        messagebox.showinfo("Thông báo", "Bạn chưa nhập tên file xuất ra!")
        return

    # Ensure the filename has the .pdf extension
    output_file += ".pdf"

    # Merge the selected PDFs
    merger = PdfMerger()
    for pdf in file_paths:
        merger.append(pdf)

    # Try writing the merged PDF to disk and report success or failure.
    try:
        merger.write(output_file)
        merger.close()
        messagebox.showinfo("Thành công", f"Merge hoàn tất! File lưu tại: {output_file}")
    except Exception as e:
        # Show a user-friendly error.
        messagebox.showerror("Lỗi", f"Không thể lưu file: {e}")

if __name__ == "__main__":
    merge_pdfs()
