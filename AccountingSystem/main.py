import tkinter as tk
from tkinter import ttk


if __name__ == "__main__":
    root = tk.Tk()

    """>>>>>FOR DEBUG>>>>>"""
    ttk.Style().configure(
        "debug0.TFrame", background="green", borderwidth=2, relief="raised"
    )
    ttk.Style().configure(
        "debug1.TFrame", background="red", borderwidth=2, relief="raised"
    )
    ttk.Style().configure(
        "debug2.TFrame", background="yellow", borderwidth=2, relief="raised"
    )
    ttk.Style().configure(
        "debug0.TLabel", background="blue", borderwidth=2, relief="raised"
    )
    ttk.Style().configure(
        "debug0.TEntry", background="blue", borderwidth=2, relief="raised"
    )
    """<<<<<FOR DEBUG<<<<<"""

    frame_external = ttk.Frame(root, style="debug0.TFrame")
    frame_header = ttk.Frame(frame_external, style="debug1.TFrame")
    frame_title = ttk.Frame(frame_header, style="debug2.TFrame", width=630, height=105)
    label_title = ttk.Label(frame_title, style="debug0.TLabel", text="タイトル")
    frame_date = ttk.Frame(frame_header, style="debug2.TFrame", width=500, height=105)
    label_date = ttk.Label(frame_date, style="debug0.TLabel", text="2023-03-30")
    frame_member_header = ttk.Frame(
        frame_header, style="debug2.TFrame", width=150, height=40
    )
    label_member_header = ttk.Label(
        frame_member_header, style="debug0.TLabel", text="記入者"
    )
    frame_member_input = ttk.Frame(
        frame_header, style="debug2.TFrame", width=150, height=65
    )
    entry_member = ttk.Entry(frame_member_input, style="debug0.TEntry")

    root.geometry("1280x600")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    frame_external.grid(column=0, row=0)
    frame_external.columnconfigure(0, weight=1)
    frame_external.rowconfigure(0, weight=1)
    frame_header.grid(column=0, row=0)
    frame_header.columnconfigure(0, weight=630)
    frame_header.columnconfigure(1, weight=500)
    frame_header.columnconfigure(2, weight=150)
    frame_header.rowconfigure(0, weight=40)
    frame_header.rowconfigure(1, weight=65)
    frame_title.grid(column=0, row=0, rowspan=2)
    label_title.grid()
    frame_date.grid(column=1, row=0, rowspan=2)
    label_date.grid()
    frame_member_header.grid(column=2, row=0)
    label_member_header.grid()
    frame_member_input.grid(column=2, row=1)
    entry_member.grid()

    root.mainloop()
