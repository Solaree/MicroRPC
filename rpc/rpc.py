# rpc.py
import os
import sys
import time
from pypresence import Presence
from colorama import Fore

class MicroRPCDefs:
    def __init__(self):
        self.id = 1076096554672324688

        self.editing_file = "Editing a {} file"

        self.micro = "Micro"
        self.micro_logo = "https://i.imgur.com/5whbPw6.png"

        self.editors = {
            ".s": ("Assembly", "https://i.imgur.com/7h5fVmG.png"),
            ".S": ("Assembly", "https://i.imgur.com/7h5fVmG.png"),
            ".asm": ("Assembly", "https://i.imgur.com/7h5fVmG.png"),
            ".ASM": ("Assembly", "https://i.imgur.com/7h5fVmG.png"),
            ".c": ("C", "https://i.imgur.com/yr8Okxt.png"),
            ".h": ("C", "https://i.imgur.com/yr8Okxt.png"),
            ".cpp": ("C++", "https://i.imgur.com/HMt2Ute.png"),
            ".hpp": ("C++", "https://i.imgur.com/HMt2Ute.png"),
            ".go": ("Go", "https://i.imgur.com/O9yXGY1.jpg"),
            ".rs": ("Rust", "https://i.imgur.com/sEGeZaJ.png"),
            ".cs": ("C#", "https://i.imgur.com/vs2IoDc.png"),
            ".js": ("JavaScript", "https://i.imgur.com/UjXay9R.png"),
            ".ts": ("TypeScript", "https://i.imgur.com/UJognrl.png"),
            ".py": ("Python", "https://i.imgur.com/UXswXmG.png"),
            ".pyz": ("Python", "https://i.imgur.com/UXswXmG.png"),
            ".pyw": ("Python", "https://i.imgur.com/UXswXmG.png"),
            ".html": ("HTML", "https://i.imgur.com/gRBHURq.png"),
            ".css": ("CSS", "https://i.imgur.com/Df2pBH0.png"),
            ".sh": ("Shell", "https://i.imgur.com/ilGl57N.jpg"),
            ".zsh": ("Shell", "https://i.imgur.com/ilGl57N.jpg"),
            ".bash": ("Shell", "https://i.imgur.com/ilGl57N.jpg"),
            ".fish": ("Shell", "https://i.imgur.com/ilGl57N.jpg"),
            ".cfg": ("Config", "https://i.imgur.com/8DHJhH8.png"),
            ".conf": ("Config", "https://i.imgur.com/8DHJhH8.png"),
            ".config": ("Config", "https://i.imgur.com/8DHJhH8.png"),
            ".txt": ("Txt", "https://i.imgur.com/zIh4Q6Y.png"),
        }

class MicroRPC(MicroRPCDefs):
    def __init__(self, filename: str):
        super().__init__()
        self.filename = filename
        self.time_count = 0
        self.rpc = Presence(self.id)
        self.connect_rpc()

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
            sys.exit(1)

    def close_rpc(self):
        self.rpc.close()

    def update_rpc(self):
        file_ext = os.path.splitext(self.filename)[1]
        if file_ext in self.editors:
            self.file_extension, self.logo = self.editors[file_ext]
        else:
            self.previous_line = f"{Fore.WHITE}MicroRPC: {Fore.YELLOW}Extension not handled for '{file_ext}' format yet.{Fore.WHITE}"
            print(self.previous_line, end="", flush=True)
            time.sleep(3)
            self.clear_previous_line()
            sys.exit(1)

        self.rpc.update(
            small_text=self.micro,
            small_image=self.micro_logo,
            large_text=self.file_extension,
            large_image=self.logo,
            details=self.filename,
            state=f"{self.time_count // 3600:02d}:{(self.time_count % 3600) // 60:02d}:{self.time_count % 60:02d} elapsed",
            buttons=[{"label": "Page", "url": "https://solardev.gq"}]
        )

    def execute_rpc(self):
        try:
            while True:
                self.update_rpc()
                time.sleep(1)
                self.time_count += 1
        except KeyboardInterrupt:
            self.close_rpc()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.WHITE}MicroRPC: {Fore.GREEN}usage: {sys.argv[0]} <filename>{Fore.WHITE}")
        sys.exit(1)

    filename = sys.argv[1]
    rpc = MicroRPC(filename)
    rpc.execute_rpc()
