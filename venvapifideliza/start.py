import subprocess

class Start():
    def star_apr(self):
        subprocess.run('uvicorn main:app --reload')