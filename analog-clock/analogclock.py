import tkinter as tk
import time
import math

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Rocket")
        self.root.configure(bg="white")
        self.root.geometry("300x300")
        self.root.resizable(True, True)

        self.canvas = tk.Canvas(root, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.update_clock()

    def update_clock(self):
        self.canvas.delete("all")
        width, height = self.root.winfo_width(), self.root.winfo_height()
        cx, cy = width // 2, height // 2
        scale = min(width, height) / 200

        now = time.localtime()
        hours, minutes, seconds = now.tm_hour % 12, now.tm_min, now.tm_sec

        self._draw_circle(cx, cy, scale)
        self._draw_markers(cx, cy, scale)
        self._draw_numbers(cx, cy, scale)
        self._draw_hand(cx, cy, hours * 30 + minutes * 0.5, 50 * scale, 6 * scale, "black")
        self._draw_hand(cx, cy, minutes * 6, 70 * scale, 4 * scale, "black")
        self._draw_hand(cx, cy, seconds * 6, 80 * scale, 2 * scale, "red")

        self.root.after(1000, self.update_clock)

    def _draw_hand(self, cx, cy, angle, length, width, color):
        angle = math.radians(angle - 90)
        x_end = cx + length * math.cos(angle)
        y_end = cy + length * math.sin(angle)
        self.canvas.create_line(cx, cy, x_end, y_end, width=width, fill=color, capstyle=tk.ROUND)

    def _draw_circle(self, cx, cy, scale):
        r = 90 * scale
        self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline="black", width=3, fill="white")
        self.canvas.create_oval(cx - 5 * scale, cy - 5 * scale, cx + 5 * scale, cy + 5 * scale, fill="black")

    def _draw_markers(self, cx, cy, scale):
        for i in range(60):
            angle = math.radians(i * 6 - 90)
            length = 2 * scale if i % 5 == 0 else 3 * scale
            x1 = cx + 90 * scale * math.cos(angle)
            y1 = cy + 90 * scale * math.sin(angle)
            x2 = cx + (90 - length) * scale * math.cos(angle)
            y2 = cy + (90 - length) * scale * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2 if i % 5 == 0 else 1)

    def _draw_numbers(self, cx, cy, scale):
        font = ("Arial", int(14 * scale), "bold")
        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)
            x = cx + 65 * scale * math.cos(angle)
            y = cy + 65 * scale * math.sin(angle)
            self.canvas.create_text(x, y, text=str(i), font=font, fill="black", anchor="center")

def main():
    import tkinter as tk
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()