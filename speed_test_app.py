import tkinter as tk
from tkinter import messagebox
import speedtest

class SpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Internet Speed Test")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="Click the button to test your internet speed", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.test_button = tk.Button(root, text="Test Speed", command=self.test_speed, font=("Helvetica", 12))
        self.test_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=20)

    def test_speed(self):
        st = speedtest.Speedtest()
        
        self.label.config(text="Testing...")
        
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000      # Convert to Mbps
        ping = st.results.ping
        
        result_text = f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps\nPing: {ping} ms"
        
        self.result_label.config(text=result_text)
        self.label.config(text="Click the button to test your internet speed")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTestApp(root)
    root.mainloop()