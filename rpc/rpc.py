# rpc.pyz

import os, sys, time
from pypresence import *
from colorama import Fore

class MicroRPCDefs:
    def __init__(self):
        self.id = 1076096554672324688

        self.editing_file = "Editing a {} file"

        self.micro = "Micro"
        self.micro_logo = "https://i.imgur.com/5whbPw6.png"

        self.asm = self.editing_file.format("Assembly")
        self.asm_logo = "https://i.imgur.com/7h5fVmG.png"

        self.clang = self.editing_file.format("C")
        self.clang_logo = "https://i.imgur.com/yr8Okxt.png"

        self.cpp = self.editing_file.format("C++")
        self.cpp_logo = "https://i.imgur.com/HMt2Ute.png"

        self.golang = self.editing_file.format("Go")
        self.golang_logo = "https://i.imgur.com/O9yXGY1.jpg"

        self.rust = self.editing_file.format("Rust")
        self.rust_logo = "https://i.imgur.com/sEGeZaJ.png"

        self.cs = self.editing_file.format("C#")
        self.cs_logo = "https://i.imgur.com/vs2IoDc.png"

        self.java = self.editing_file.format("Java")
        self.java_logo = "https://i.imgur.com/rvlfXVR.png"

        self.js = self.editing_file.format("JavaScript")
        self.js_logo = "https://i.imgur.com/UjXay9R.png"

        self.ts = self.editing_file.format("TypeScript")
        self.ts_logo = "https://i.imgur.com/UJognrl.png"

        self.py = self.editing_file.format("Python")
        self.py_logo = "https://i.imgur.com/UXswXmG.png"

        self.html = self.editing_file.format("HTML")
        self.html_logo = "https://i.imgur.com/gRBHURq.png"

        self.css = self.editing_file.format("CSS")
        self.css_logo = "https://i.imgur.com/Df2pBH0.png"

        self.sh = self.editing_file.format("Shell")
        self.sh_logo = "https://i.imgur.com/ilGl57N.jpg"

        self.config = self.editing_file.format("Config")
        self.config_logo = "https://i.imgur.com/8DHJhH8.png"

        self.txt = self.editing_file.format("Txt")
        self.txt_logo = "https://i.imgur.com/zIh4Q6Y.png"

class MicroRPC(MicroRPCDefs):
    def __init__(self, filename: str):
        MicroRPCDefs.__init__(self)
        self.filename = filename
        self.file_extention = ""
        self.logo = ""
        self.time_count = 0
        self.rpc = Presence(self.id)
        self.execute_rpc()

    def clear_previous_line(self):
        sys.stdout.write("\r" + " " * (len(self.previous_line) + 1) + "\r")
        sys.stdout.flush()

    def connect_rpc(self):
        try:
            self.rpc.connect()
        except Exception as e:
            self.previous_line = f"{Fore.WHITE}MicroRPC: {Fore.YELLOW}Error connecting to Discord: {Fore.RED}{e}{Fore.WHITE}"
            print(self.previous_line, end="", flush=True)
            time.sleep(3)
            self.clear_previous_line()
            exit()

    def close_rpc(self):
        self.rpc.close()
    
    def update_rpc(self):
        if self.filename.endswith(".s") or self.filename.endswith(".S") or self.filename.endswith(".asm") or self.filename.endswith(".ASM"):
            self.file_extention = self.asm
            self.logo = self.asm_logo
        elif self.filename.endswith(".c") or self.filename.endswith(".h"):
            self.file_extention = self.clang
            self.logo = self.clang_logo
        elif self.filename.endswith(".cpp") or self.filename.endswith(".hpp"):
            self.file_extention = self.cpp
            self.logo = self.cpp_logo
        elif self.filename.endswith(".go"):
            self.file_extention = self.golang
            self.logo = self.golang_logo
        elif self.filename.endswith(".rs"):
            self.file_extention = self.rust
            self.logo = self.rust_logo
        elif self.filename.endswith(".cs"):
            self.file_extention = self.cs
            self.logo = self.cs_logo
        elif self.filename.endswith(".js"):
            self.file_extention = self.js
            self.logo = self.js_logo
        elif self.filename.endswith(".ts"):
            self.file_extention = self.ts
            self.logo = self.ts_logo
        elif self.filename.endswith(".py") or self.filename.endswith(".pyz") or self.filename.endswith(".pyw"):
            self.file_extention = self.py
            self.logo = self.py_logo
        elif self.filename.endswith(".html"):
            self.file_extention = self.html
            self.logo = self.html_logo
        elif self.filename.endswith(".css"):
            self.file_extention = self.css
            self.logo = self.css_logo
        elif self.filename.endswith(".sh") or self.filename.endswith(".zsh") or self.filename.endswith(".bash") or self.filename.endswith(".fish"):
            self.file_extention = self.sh
            self.logo = self.sh_logo
        elif self.filename.endswith(".cfg") or self.filename.endswith(".conf") or self.filename.endswith(".config"):
            self.file_extention = self.config
            self.logo = self.config_logo
        elif self.filename.endswith(".txt"):
            self.file_extention = self.txt
            self.logo = self.txt_logo
        else:
            _, file_extension = os.path.splitext(self.filename)
            self.previous_line = f"{Fore.WHITE}MicroRPC: {Fore.YELLOW}Extention not handled for '{file_extension}' format yet.{Fore.WHITE}"
            print(self.previous_line, end="", flush=True)
            time.sleep(3)
            self.clear_previous_line()
            exit()

        self.rpc.update(
            small_text=self.micro,
            small_image=self.micro_logo,
            large_text=self.file_extention,
            large_image=self.logo,
            details=self.filename,
            state=f"{self.time_count // 3600:02d}:{(self.time_count % 3600) // 60:02d}:{self.time_count % 60:02d} elapsed",
            buttons=[{"label": "Page", "url": "https://solardev.gq"}]
        )

    def execute_rpc(self):
        self.connect_rpc()
        try:
            while True:
                self.update_rpc()
                time.sleep(1)
                self.time_count += 1
        except KeyboardInterrupt:
            self.close_rpc()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        MicroRPC(filename)
    else:
        self.previous_line = f"{Fore.WHITE}MicroRPC: {Fore.GREEN}usage: rpc.pyz <filename>{Fore.WHITE}"
        print(self.previous_line, end="", flush=True)
        time.sleep(3)
        self.clear_previous_line()
