"""
One Row Joiner - Consolidates multi-line text into a single row with a custom delimiter.
"""
import tkinter as tk
from tkinter import messagebox

def join_rows(data: str, delimiter: str) -> str:
    """Joins multi-line text into a single row using a delimiter.

    Args:
        data: The multi-line string to join.
        delimiter: The string to use as a separator.

    Returns:
        A single string with rows joined by the delimiter.
    """
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    return delimiter.join(lines)

class OneRowJoinerApp:
    """The main application class for the One Row Joiner GUI."""

    def __init__(self, root: tk.Tk) -> None:
        """Initializes the GUI components.

        Args:
            root: The root tkinter window.
        """
        self.root = root
        self.root.title("One Row Joiner")
        
        # Disable maximize button
        self.root.resizable(False, False)

        # Main frame
        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Input Section
        self.input_label = tk.Label(self.frame, text="Input (Rows):", font=("Segoe UI", 10, "bold"))
        self.input_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.input_text = tk.Text(self.frame, height=10, width=70, font=("Segoe UI", 10))
        self.input_text.grid(row=1, column=0, columnspan=2, pady=(0, 15))

        # Delimiter Section
        self.delimiter_label = tk.Label(self.frame, text="Delimiter:", font=("Segoe UI", 10, "bold"))
        self.delimiter_label.grid(row=2, column=0, sticky="w", pady=(0, 5))

        self.delimiter_entry = tk.Entry(self.frame, width=25, font=("Segoe UI", 10))
        self.delimiter_entry.insert(0, ",")  # Default delimiter
        self.delimiter_entry.grid(row=3, column=0, sticky="w", pady=(0, 15))

        # Buttons Section
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.grid(row=3, column=1, sticky="e", pady=(0, 15))

        self.clear_button = tk.Button(
            self.button_frame,
            text="Clear",
            command=self.clear_fields,
            font=("Segoe UI", 10, "bold"),
            bg="#f3f2f1",
            fg="black",
            width=12,
            pady=5
        )
        self.clear_button.pack(side=tk.LEFT, padx=(0, 10))

        self.join_button = tk.Button(
            self.button_frame, 
            text="Join Rows", 
            command=self.handle_join,
            font=("Segoe UI", 10, "bold"),
            bg="#0078d4",
            fg="white",
            width=12,
            pady=5
        )
        self.join_button.pack(side=tk.LEFT)

        # Output Section
        self.output_label = tk.Label(self.frame, text="Output (Single Row):", font=("Segoe UI", 10, "bold"))
        self.output_label.grid(row=4, column=0, sticky="w", pady=(0, 5))

        self.output_entry = tk.Entry(self.frame, width=70, font=("Segoe UI", 10))
        self.output_entry.grid(row=5, column=0, columnspan=2)

    def clear_fields(self) -> None:
        """Clears the input and output fields."""
        self.input_text.delete("1.0", tk.END)
        self.output_entry.delete(0, tk.END)

    def handle_join(self) -> None:
        """Handles the join button click event."""
        data = self.input_text.get("1.0", tk.END)
        delimiter = self.delimiter_entry.get()

        if not data.strip():
            messagebox.showwarning("Warning", "Input text cannot be empty.")
            return

        try:
            result = join_rows(data, delimiter)
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, result)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main() -> None:
    """Initializes and runs the One Row Joiner application."""
    root = tk.Tk()
    app = OneRowJoinerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
