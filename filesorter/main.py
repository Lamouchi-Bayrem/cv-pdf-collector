import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def browse_directory(entry_dir: tk.Entry):
    """Open folder dialog and set the path in the entry."""
    folder = filedialog.askdirectory()
    if folder:
        entry_dir.delete(0, tk.END)
        entry_dir.insert(0, folder)


def search_and_copy(entry_dir: tk.Entry, entry_ext: tk.Entry, entry_name: tk.Entry):
    """Search and copy files based on extension and/or name filter."""
    src_dir = entry_dir.get().strip()
    extension = entry_ext.get().strip().lower()
    name_filter = entry_name.get().strip().lower()

    if not src_dir or not os.path.exists(src_dir):
        messagebox.showerror("Error", "Please select a valid directory.")
        return

    # Normalize extension
    if extension and not extension.startswith('.'):
        extension = '.' + extension

    # Build destination folder name
    folder_name = "Sorted"
    if name_filter:
        folder_name += f"_{name_filter.replace(' ', '_')}"
    if extension:
        folder_name += f"_{extension.replace('.', '')}"

    dest_dir = os.path.join(src_dir, folder_name)
    os.makedirs(dest_dir, exist_ok=True)

    count = 0
    for root, _, files in os.walk(src_dir):
        for file in files:
            lower_file = file.lower()
            if (not extension or lower_file.endswith(extension)) and \
               (not name_filter or name_filter in lower_file):
                src_file = os.path.join(root, file)
                shutil.copy2(src_file, dest_dir)
                count += 1

    messagebox.showinfo(
        "Success",
        f"✅ {count} file{'s' if count != 1 else ''} copied to:\n{dest_dir}"
    )


def run():
    """Launch the File Sorter GUI."""
    root = tk.Tk()
    root.title("📁 File Sorter by Extension or Name")
    root.geometry("520x340")
    root.resizable(False, False)

    # Directory selection
    tk.Label(root, text="Source Directory:", font=("Arial", 11, "bold")).pack(pady=(15, 5))
    entry_dir = tk.Entry(root, width=60)
    entry_dir.pack(pady=2, padx=20)
    tk.Button(root, text="Browse", command=lambda: browse_directory(entry_dir)).pack(pady=5)

    # Extension filter
    tk.Label(root, text="File Extension (e.g. pdf, jpg, png, docx):", font=("Arial", 10)).pack(pady=(15, 5))
    entry_ext = tk.Entry(root, width=25)
    entry_ext.pack(pady=2)

    # Name filter
    tk.Label(root, text="File Name Contains (optional):", font=("Arial", 10)).pack(pady=(12, 5))
    entry_name = tk.Entry(root, width=25)
    entry_name.pack(pady=2)

    # Start button
    tk.Button(
        root,
        text="Start Sorting",
        command=lambda: search_and_copy(entry_dir, entry_ext, entry_name),
        bg="#0078D7",
        fg="white",
        font=("Arial", 11, "bold"),
        width=25,
        height=2
    ).pack(pady=25)

    # Tip
    tk.Label(
        root,
        text="💡 Tip: Use both filters together, e.g. extension = 'pdf' + name = 'resume'",
        fg="gray",
        font=("Arial", 9)
    ).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    run()
