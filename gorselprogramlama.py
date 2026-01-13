import sys
import sqlite3

from PyQt5.QtWidgets import(
     QApplication,
     QMainWindow,
     QWidget,
     QVBoxLayout,
     QHBoxLayout,
     QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QSpinBox, QComboBox, QDoubleSpinBox 
)

DBPath = "films.db"

class FilmDB:

    def __init__(self, db_path=DBPath):

        self.db_path = db_path
        self.__initdb()

    def connect(self):
        return sqlite3.connect(self.db_path)

    def __initdb(self):
        with self.connect() as con:
            cur = con.cursor()    

            cur.execute(
                '''
                CREATE TABLE IF NOT EXISTS films (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    year INTEGER NOT NULL,
                    rating REAL NOT NULL
                )
                '''
                )
            con.commit()

    def add_film(self, title, genre, year, rating):
        with self.connect() as con:
            cur = con.cursor()
            cur.execute(
                '''
                INSERT INTO films (title, genre, year, rating)
                VALUES (?, ?, ?, ?)
                ''',
                (title, genre, year, rating)
            )
            con.commit()

    def list_films(self, query=""):
        with self.connect() as con:
            cur = con.cursor()
            if query.strip():
                cur.execute(
                    '''
                    SELECT id, title, genre, year, rating FROM films
                    WHERE LOWER(title) LIKE ? OR genre LIKE ? ORDER BY DESC,
                    ''',
                    (f'%{query.lower()}%')
                )
            else:
                cur.execute(
                    '''
                    SELECT id, title, genre, year, rating FROM films ORDER BY id DESC
                    '''
                )                    
            return cur.fetchall()
        
    def delete_film(self, film_id):
        with self.connect() as con:
            cur = con.cursor()
            cur.execute(
                '''
                DELETE FROM films WHERE id = ?
                ''',
                (film_id,)
            )
            con.commit()    

    def update_film(self, film_id, title, genre, year, rating):
        with self.connect() as con:
            cur = con.cursor()
            cur.execute(
                '''
                UPDATE films
                SET title = ?, genre = ?, year = ?, rating = ?
                WHERE id = ?
                ''',
                (title, genre, year, rating, film_id)
            )
            con.commit()        

class FilmArchiveApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Film Arşivi (PYQT5 + SQLite3)")
        self.resize(820, 520)
        
        self.db = FilmDB()
        self.selected_id = None

        #UI
        central = QWidget()
        self.setCentralWidget(central)
        main = QVBoxLayout()

        #Form
        form = QHBoxLayout()
        main.addLayout(form)

        form.addWidget(QLabel("Film Adı: "))
        self.title_inp = QLineEdit()
        self.title_inp.setPlaceholderText("Film Adını Giriniz...")
        form.addWidget(self.title_inp)


        form.addWidget(QLabel("Tür: "))
        self.genre_inp = QComboBox()
        self.genre_inp.addItems(
            ["Aksiyon",
             "Komedi",
             "Dram",
             "Bilim Kurgu",
             "Korku",
             "Romantik",
             "Belgesel"
            ]
        )
        form.addWidget(self.genre_inp)

        form.addWidget(QLabel("Yıl: "))
        self.year_inp = QSpinBox()
        self.year_inp.setRange(1900,2100)
        self.year_inp.setValue(2024)
        form.addWidget(self.year_inp)

        form.addWidget(QLabel("Puan: "))
        self.rating_inp = QDoubleSpinBox()
        self.rating_inp.setRange(0.0,10.0)
        self.rating_inp.setSingleStep(0.1)
        self.rating_inp.setValue(7.5)
        form.addWidget(self.year_inp)

        self.add_btn = QPushButton("Film Ekle")
        self.update_btn = QPushButton("Güncelle")
        self.clear_btn = QPushButton("Formu Temizle")
        
        form.addWidget(self.add_btn)
        form.addWidget(self.update_btn)
        form.addWidget(self.clear_btn)

        #search
        search = QHBoxLayout()
        main.addLayOut(search)

        search.addWidget(QLabel("Ada göre arama..."))
        self.search_inp = QLineEdit()
        self.search_inp.setPlaceholderText("Örn: star")
        search.addWidget(self.search_inp)

        self.refresh_btn = QPushButton("Yenile")
        search.addWidget(self.refresh_btn)

        #Table
        self.table = QTableWidget(0.5)
        self.table.setHorizontalHeaderLabels(["ID","Film Adı","Tür","Yıl","Puan"])
        self.table.setSelectionBehavior(self.table.SelectRows)
        self.table.setEditTriggers(self.table.NoEditTriggers)
        main.addWidget(self.table)

        #bottom butonu
        bottom = QHBoxLayout()
        main.addLayout(bottom)

        self.delete_btn = QPushButton("Seçileni Sil")
        bottom.addWidget(self.delete_btn)

        #butonlara basınca olacak olaylar
        self.add_btn.clicked.connect(self.add_film)
        self.update_btn.clicked.connect(self.update_film)
        self.delete_btn.cliceed.connect(self.delete_selected)
        self.clear_btn.clicked.connect(self.clear_form)
        self.refresh_btn.clicked.connect(self.refresh_btn_table)
        self.search_inp.textChanged.connect(self.refresh_table)
        self.table.cellClicked.connect(self.on_row_click)

        self.refresh_rable()

    def show_error(self,msg):
        QMessageBox.critical(self, "Hata", msg)

    def show_info(self, msg):
        QMessageBox.information(self, "Bilgi", msg)

    def clear_form(self):
        self.selected_id = None
        self.title_inp.clear()
        self.genre_inp.setCurrentIndex(0)
        self.year_inp.setValue(2024)
        self.rating_inp.setValue(7.5)
        self.table.clearSelection()

    def refres_table(self):
        q = self.search_inp.text().strip()
        rows = self.db.list_films(q)

        self.table.setRowCount(0)

        for r in rows:
            row_idx = self.table.rowCount()
            self.table.insertRow(row_idx)
            for c, val in enumerate(r):
                self.table.setItem(row_idx, c, QTableWidget(str(val)))

        self.table.resizeColumnsToContents()

    def add_film(self):
        title = self.title_inp.text().strip()
        genre = self.genre_inp.currentText()
        year = int(self.year_inp.value())
        rating = float(self.rating_inp.value())

        if not title:
            self.show_error("Film Adı boş olamaz!")
            return

        try:
            self.db.add_film(title, genre, year, rating)
            self.show_info("Film Eklendi")
            self.clear_form()
            self.refres_table()

        except Exception as e:
            self.show_error(str(e)) 

    def on_row_click(self, row, col):
        film_id = int(self.table.item(row,0).text())
        title = self.table.item(row,1).text()
        genre = self.table.item(row,2).text()
        year = self.table.item(row,3).text()
        rating = self.table.item(row,4).text()

        self.selected_id = film_id
        self.title_inp.setText(title)

        #comboboxtan türü seç
        idx = self.genre_inp.findText(genre)
        if idx != -1:
            self.genre_inp.setCurrentText(idx)

        self.year_inp.setValue(year)
        self.rating_inp.setValue(rating)

    def update_film(self):
        if self.selected_id is None:
            self.show_info("Güncellemek için tablodan bir satır seçiniz")
            return

        title = self.title_inp.text().strip()
        genre = self.genre_inp.text().strip()
        year = int(self.year_inp.value())
        rating = float(self.rating_inp.value())

        if not title:
            self.show_error("Film adı boş olamaz")
            return

        try:
            self.db.update_film(self.selected_id, title, genre, year, rating)
            self.show_info("Film güncellendi")
            self.clear_form()
            self.refres_table()

        except Exception as e:
            self.show_error(str(e))

    def delete_selected(self):
        if self.selected_id is None:
            self.show_info("Silmek için tablodan satır seçiniz")
            return
            
        confirm = QMessageBox.question(
            self
            "Onay",
            f"ID" = {self.selected_id} olan 
        )    

        try:
            self.db.delete_film(self.selected_id)
            self.show_info("Film Silindi")
            self.clear_form()
            self.refres_table()
        except Ellipsis as e:
            self.show_error(str(e))

def main():                
