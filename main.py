from lexer import Lexer
from parser import Parser
from codegen import CodeGenerator
import tkinter as tk
from tkinter import scrolledtext, ttk, font

def compile_and_display():
    source_code = source_text.get("1.0", tk.END)
    output_lexer.delete("1.0", tk.END)
    output_parser.delete("1.0", tk.END)
    output_codegen.delete("1.0", tk.END)
    output_interpreter.delete("1.0", tk.END)
    history_text.delete("1.0", tk.END)  # Clear history at the beginning

    try:
        # Lexer Phase
        lexer = Lexer(source_code)
        tokens = []
        token = lexer.get_next_token()
        while token:
            tokens.append(token)
            token = lexer.get_next_token()
        output_lexer.insert(tk.END, "Lexer Output (Tokens):\n", "header_lexer")
        if tokens:
            for token in tokens:
                output_lexer.insert(tk.END, f"  {token}\n", "token")
        else:
            output_lexer.insert(tk.END, "  No tokens generated.\n", "no_output")
        history_text.insert(tk.END, f"Input Source Code:\n{source_code}\n\n")
        history_text.insert(tk.END, f"Tokens:\n{tokens}\n\n")

        # Parser Phase
        parser = Parser(tokens)
        ast = parser.parse()
        output_parser.insert(tk.END, "Parser Output (AST):\n", "header_parser")
        output_parser.insert(tk.END, f"  {ast}\n", "ast")
        history_text.insert(tk.END, f"AST:\n{ast}\n\n")

        # Code Generator Phase
        codegen = CodeGenerator(ast)
        generated_code = codegen.generate()
        output_codegen.insert(tk.END, "Code Generator Output (Instructions):\n", "header_codegen")
        if generated_code:
            for instruction in generated_code:
                output_codegen.insert(tk.END, f"  {instruction}\n", "instruction")
        else:
            output_codegen.insert(tk.END, "  No instructions generated.\n", "no_output")
        history_text.insert(tk.END, f"Generated Code:\n{generated_code}\n\n")

        # Interpreter Phase
        variables = {}
        stack = []
        interpreter_output = ""
        for instruction in generated_code:
            if instruction[0] == "PUSH":
                stack.append(instruction[1])
            elif instruction[0] == "LOAD":
                stack.append(variables.get(instruction[1], 0))
            elif instruction[0] == "STORE":
                variables[instruction[1]] = stack.pop()
            elif instruction[0] == "ADD":
                stack.append(stack.pop() + stack.pop())
            elif instruction[0] == "SUB":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif instruction[0] == "MUL":
                stack.append(stack.pop() * stack.pop())
            elif instruction[0] == "DIV":
                second = stack.pop()
                first = stack.pop()
                stack.append(first / second)
            elif instruction[0] == "PRINT":
                if len(stack) > 0:  # added check.
                    interpreter_output += str(stack[-1]) + "\n"
                else:
                    interpreter_output += "Error: Stack empty during PRINT\n"
        output_interpreter.insert(tk.END, "Interpreter Output:\n", "header_interpreter")
        if interpreter_output:
            output_interpreter.insert(tk.END, interpreter_output, "interpreter")
        else:
            output_interpreter.insert(tk.END, "  No interpreter output.\n", "no_output")
        history_text.insert(tk.END, f"Interpreter Output:\n{interpreter_output}\n")

    except Exception as e:
        error_message = f"Error: {e}"
        output_lexer.delete("1.0", tk.END)
        output_parser.delete("1.0", tk.END)
        output_codegen.delete("1.0", tk.END)
        output_interpreter.delete("1.0", tk.END)
        output_lexer.insert(tk.END, error_message, "error")
        history_text.insert(tk.END, f"Error:\n{error_message}\n")

def clear_all():
    source_text.delete("1.0", tk.END)
    output_lexer.delete("1.0", tk.END)
    output_parser.delete("1.0", tk.END)
    output_codegen.delete("1.0", tk.END)
    output_interpreter.delete("1.0", tk.END)
    history_text.delete("1.0", tk.END)  # Clear history as well

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        window.configure(bg="#212121")  # Dark background
        title_label.configure(foreground="#ffffff", background="#212121")
        note_label.configure(foreground="#cccccc", background="#212121")
        source_label.configure(foreground="#ffffff", background="#212121")
        source_text.configure(bg="#333333", fg="#ffffff")
        output_lexer.configure(bg="#333333", fg="#ffffff")
        output_parser.configure(bg="#333333", fg="#ffffff")
        output_codegen.configure(bg="#333333", fg="#ffffff")
        output_interpreter.configure(bg="#333333", fg="#ffffff")
        history_text.configure(bg="#333333", fg="#ffffff")
        history_label.configure(foreground="#ffffff", background="#212121") 
        notebook.configure(
            background="#212121",
            foreground="#ffffff",
        )
        for child in notebook.winfo_children():
            child.configure(background="#212121", foreground="#ffffff")
        style.configure("TLabel", background="#212121", foreground="#ffffff")
        style.configure("TFrame", background="#212121")

        compile_button.configure(
            background="#66BB6A",  # Lighter shade for dark mode
            foreground="#ffffff",
        )
        clear_button.configure(
            background="#E57373",  # Lighter shade for dark mode
            foreground="#ffffff",
        )
        dark_mode_button.configure(
            background="#424242",  # Darker button for dark mode
            foreground="#ffffff"
        )

    else:
        window.configure(bg="#e0f8ff")  # Light background
        title_label.configure(foreground="#000000", background="#e0f8ff")
        note_label.configure(foreground="#000000", background="#e0f8ff")
        source_label.configure(foreground="#000000", background="#e0f8ff")
        source_text.configure(bg="#ffffff", fg="#333333")
        output_lexer.configure(bg="#f0f0f0", fg="#333333")
        output_parser.configure(bg="#f0f0f0", fg="#333333")
        output_codegen.configure(bg="#f0f0f0", fg="#333333")
        output_interpreter.configure(bg="#f0f0f0", fg="#333333")
        history_text.configure(bg="#f8f8f8", fg="#222222")
        notebook.configure(
            background="#e0f8ff",
            foreground="#000000",
        )
        for child in notebook.winfo_children():
            child.configure(background="#e0f8ff", foreground="#000000")
        style.configure("TLabel", background="#e0f8ff", foreground="#000000")
        style.configure("TFrame", background="#e0f8ff")

        compile_button.configure(
            background="#4CAF50",
            foreground="#ffffff",
        )
        clear_button.configure(
            background="#f44336",
            foreground="#ffffff",
        )
        dark_mode_button.configure(
            background="#f0f0f0",  # Lighter button for light mode
            foreground="#000000"
        )

# Global variable to track dark mode state
dark_mode = False

window = tk.Tk()
window.title("MiniLang Compiler")
window.configure(bg="#e0f8ff")

# Use a grid layout for more precise placement
window.grid_columnconfigure(0, weight=1)  # Make the first column resizable
window.grid_columnconfigure(1, weight=1)  # Make the second column resizable
window.grid_columnconfigure(2, weight=1) # Make third column resizable
window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=0)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=0)
window.grid_rowconfigure(4, weight=0) # Add a row for the title

header_font = font.Font(family="Helvetica", size=12, weight="bold")
error_font = font.Font(family="Helvetica", size=10)
token_font = font.Font(family="Courier", size=10)
ast_font = font.Font(family="Courier", size=10)
instruction_font = font.Font(family="Courier", size=10)
interpreter_font = font.Font(family="Courier", size=10)
no_output_font = font.Font(family="Courier", size=10)
style = ttk.Style()
style.configure("TButton", padding=5, font=("Helvetica", 10))
style.configure("TLabel", background="#e0f8ff", font=("Helvetica", 10))
style.configure("TFrame", background="#e0f8ff") #set default style for frame.

# Title Label
title_label = ttk.Label(window, text="CompileEase", font=("Helvetica", 48, "bold italic")) # Increased size, italic, emoji
title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 0), sticky="n") # Span 3 columns, move to top

# Note Label
note_label = ttk.Label(window, text="A compiler for a minimal language.", font=("Helvetica", 10, "italic")) # Added \n for newline
note_label.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 10), sticky="n")

# Source Code Label and Text Area
source_label = ttk.Label(window, text="Source Code:")
source_label.grid(row=1, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="sw") #make label stick to the box
source_text = scrolledtext.ScrolledText(window, width=80, height=10, font=("Courier", 10), bg="#ffffff", fg="#333333")
source_text.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

# Compile and Clear Buttons
button_frame = ttk.Frame(window, style='TFrame') # Apply the style here
button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
compile_button = ttk.Button(button_frame, text="Compile", command=compile_and_display)
compile_button.pack(side=tk.LEFT, padx=5)
clear_button = ttk.Button(button_frame, text="Clear", command=clear_all)
clear_button.pack(side=tk.LEFT, padx=5)

# Dark Mode Toggle Button
dark_mode_button = ttk.Button(button_frame, text="Toggle Dark Mode", command=toggle_dark_mode)
dark_mode_button.pack(side=tk.LEFT, padx=5)

# Notebook for Output Tabs
notebook = ttk.Notebook(window)
notebook.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

lexer_frame = ttk.Frame(notebook, style='TFrame')
parser_frame = ttk.Frame(notebook, style='TFrame')
codegen_frame = ttk.Frame(notebook, style='TFrame')
interpreter_frame = ttk.Frame(notebook, style='TFrame')

notebook.add(lexer_frame, text="Lexer")
notebook.add(parser_frame, text="Parser")
notebook.add(codegen_frame, text="Code Gen")
notebook.add(interpreter_frame, text="Interpreter")

output_lexer = scrolledtext.ScrolledText(lexer_frame, width=80, height=15, font=("Courier", 10), bg="#f0f0f0", fg="#333333")
output_lexer.pack(expand=True, fill="both")
output_parser = scrolledtext.ScrolledText(parser_frame, width=80, height=15, font=("Courier", 10), bg="#f0f0f0", fg="#333333")
output_parser.pack(expand=True, fill="both")
output_codegen = scrolledtext.ScrolledText(codegen_frame, width=80, height=15, font=("Courier", 10), bg="#f0f0f0", fg="#333333")
output_codegen.pack(expand=True, fill="both")
output_interpreter = scrolledtext.ScrolledText(interpreter_frame, width=80, height=15, font=("Courier", 10), bg="#f0f0f0", fg="#333333")
output_interpreter.pack(expand=True, fill="both")

output_lexer.tag_configure("header_lexer", font=("Helvetica", 14, "italic"), background="white") # Italic and white background
output_lexer.tag_configure("token", font=token_font)
output_lexer.tag_configure("no_output", font=no_output_font)
output_parser.tag_configure("header_parser", font=("Helvetica", 14, "italic"), background="white") # Italic and white background
output_parser.tag_configure("ast", font=ast_font)
output_codegen.tag_configure("header_codegen", font=("Helvetica", 14, "italic"), background="white") # Italic and white background
output_codegen.tag_configure("instruction", font=instruction_font)
output_codegen.tag_configure("no_output", font=no_output_font)
output_interpreter.tag_configure("header_interpreter", font=("Helvetica", 14, "italic"), background="white") # Italic and white background
output_interpreter.tag_configure("interpreter", font=interpreter_font)
output_interpreter.tag_configure("no_output", font=no_output_font)
output_lexer.tag_configure("error", font=error_font, foreground="red")

# History Section
history_label = ttk.Label(window, text="Compilation History:")
history_label.grid(row=1, column=2, padx=10, pady=(10, 0), sticky="sw") #shifted down one row ,make label stick to the box
history_text = scrolledtext.ScrolledText(window, width=40, height=30, font=("Courier", 10), bg="#f8f8f8", fg="#222222")
history_text.grid(row=2, column=2, rowspan=3, padx=10, pady=5, sticky="nsew")

window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(2, weight=1)  # Make the history row resizable

# Source code label style
style.configure("SourceLabel.TLabel", font=("Helvetica", 24, "bold"))
source_label.configure(style="SourceLabel.TLabel")

# History label style
style.configure("HistoryLabel.TLabel", font=("Helvetica", 24, "bold"))
history_label.configure(style="HistoryLabel.TLabel")

window.mainloop()
