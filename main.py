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
        # Parser Phase
        parser = Parser(tokens)
        ast = parser.parse()
        output_parser.insert(tk.END, "Parser Output (AST):\n", "header_parser")
        output_parser.insert(tk.END, f"  {ast}\n", "ast")
        # Code Generator Phase
        codegen = CodeGenerator(ast)
        generated_code = codegen.generate()
        output_codegen.insert(tk.END, "Code Generator Output (Instructions):\n", "header_codegen")
        if generated_code:
            for instruction in generated_code:
                output_codegen.insert(tk.END, f"  {instruction}\n", "instruction")
        else:
            output_codegen.insert(tk.END, "  No instructions generated.\n", "no_output")
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
                if len(stack) > 0: # added check.
                    interpreter_output += str(stack[-1]) + "\n"
                else:
                    interpreter_output += "Error: Stack empty during PRINT\n"
        output_interpreter.insert(tk.END, "Interpreter Output:\n", "header_interpreter")
        if interpreter_output:
            output_interpreter.insert(tk.END, interpreter_output, "interpreter")
        else:
            output_interpreter.insert(tk.END, "  No interpreter output.\n", "no_output")
    except Exception as e:
        error_message = f"Error: {e}"
        output_lexer.delete("1.0", tk.END)
        output_parser.delete("1.0", tk.END)
        output_codegen.delete("1.0", tk.END)
        output_interpreter.delete("1.0", tk.END)
        output_lexer.insert(tk.END, error_message, "error")
def clear_all():
    source_text.delete("1.0", tk.END)
    output_lexer.delete("1.0", tk.END)
    output_parser.delete("1.0", tk.END)
    output_codegen.delete("1.0", tk.END)
    output_interpreter.delete("1.0", tk.END)
window = tk.Tk()
window.title("MiniLang Compiler")
window.configure(bg="#e0f8ff")
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
source_label = ttk.Label(window, text="Source Code:")
source_label.pack(pady=(10, 5))
source_text = scrolledtext.ScrolledText(window, width=80, height=10, font=("Courier", 10), bg="#ffffff", fg="#333333")
source_text.pack(padx=10, pady=5)
compile_button = ttk.Button(window, text="Compile", command=compile_and_display)
compile_button.pack(pady=5)
clear_button = ttk.Button(window, text="Clear", command=clear_all)
clear_button.pack(pady=5)
notebook = ttk.Notebook(window)
notebook.pack(padx=10, pady=10, expand=True, fill="both")
lexer_frame = ttk.Frame(notebook)
parser_frame = ttk.Frame(notebook)
codegen_frame = ttk.Frame(notebook)
interpreter_frame = ttk.Frame(notebook)
notebook.add(lexer_frame, text="Lexer")
notebook.add(parser_frame, text="Parser")
notebook.add(codegen_frame, text="Code Gen")
notebook.add(interpreter_frame, text="Interpreter")
output_lexer = scrolledtext.ScrolledText(lexer_frame, width=80, height=15, font=("Courier", 10), bg="#f0f0f0", fg="#333333")
output_lexer.pack()
output_parser = scrolledtext.ScrolledText(parser_frame, width=80, height=15, font=("Courier", 10), bg="#f0f0f0", fg="#333333")
output_parser.pack()
output_codegen = scrolledtext.ScrolledText(codegen_frame, width=80, height=15, font=("Courier", 10), bg="#f0f0f0", fg="#333333")
output_codegen.pack()
output_interpreter = scrolledtext.ScrolledText(interpreter_frame, width=80, height=15, font=("Courier", 10), bg="#f0f0f0", fg="#333333")
output_interpreter.pack()
output_lexer.tag_configure("header_lexer", font=header_font, foreground="#008080")
output_lexer.tag_configure("token", font=token_font)
output_lexer.tag_configure("no_output", font=no_output_font)
output_parser.tag_configure("header_parser", font=header_font, foreground="#800080")
output_parser.tag_configure("ast", font=ast_font)
output_codegen.tag_configure("header_codegen", font=header_font, foreground="#006400")
output_codegen.tag_configure("instruction", font=instruction_font)
output_codegen.tag_configure("no_output", font=no_output_font)
output_interpreter.tag_configure("header_interpreter", font=header_font, foreground="#00008b")
output_interpreter.tag_configure("interpreter", font=interpreter_font)
output_interpreter.tag_configure("no_output", font=no_output_font)
output_lexer.tag_configure("error", font=error_font, foreground="red")
window.mainloop()