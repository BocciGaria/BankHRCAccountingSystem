import sqlite3
from tkinter import *
from tkinter import ttk

from pathlib import Path

from AccountingSystem.model import *
import config


if __name__ == "__main__":
    m1 = models.ClubMember()
    print(m1.__dict__)
