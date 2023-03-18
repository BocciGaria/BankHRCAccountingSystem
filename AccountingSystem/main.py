import sqlite3
from tkinter import Tk

from pathlib import Path

from models import ClubMemberModel
import config


if __name__ == "__main__":
    # m1 = ClubMemberModel

    # app = Tk()
    # app.mainloop()

    connection = sqlite3.connect(config.DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS test
        (clumn1 text, clumn2 text, clumn3 real, clumn4 real)
        """
    )
    cursor.execute(
        """
        INSERT INTO test
        VALUES ('2023-03-18', 'papermoon', 123, 456)
        """
    )
    connection.commit()
    connection.close()
