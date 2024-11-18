import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QWidget, QDateEdit, QTabWidget
)
from PyQt5.QtCore import Qt, QDate
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt  
import pandas as pd


class BudgetApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Aplicación de Gestión de Presupuestos")
        self.setGeometry(100, 100, 1000, 700)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #F5F5F5;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                border-radius: 10px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #45A049;
            }
            QPushButton:pressed {
                background-color: #3E8E41;
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
            }
            QLineEdit, QDateEdit {
                border: 2px solid #4CAF50;
                border-radius: 5px;
                padding: 5px;
            }
            QComboBox {
                border: 2px solid #4CAF50;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        
        self.layout = QVBoxLayout()

        self.income_input = QLineEdit()
        self.income_input.setPlaceholderText("Monto Total de Ingreso")
        self.layout.addWidget(QLabel("Total de Ingresos"))
        self.layout.addWidget(self.income_input)

        self.add_income_button = QPushButton("Añadir Ingreso")
        self.add_income_button.clicked.connect(self.add_income)
        self.layout.addWidget(self.add_income_button)

        self.new_category_input = QLineEdit()
        self.new_category_input.setPlaceholderText("Nombre de Nueva Categoría")
        self.layout.addWidget(QLabel("Añadir Nueva Categoría"))
        self.layout.addWidget(self.new_category_input)

        self.add_category_button = QPushButton("Añadir Categoría")
        self.add_category_button.clicked.connect(self.add_category)
        self.layout.addWidget(self.add_category_button)

        self.expense_input = QLineEdit()
        self.expense_input.setPlaceholderText("Monto de Gasto")
        self.layout.addWidget(QLabel("Gastos"))
        self.layout.addWidget(self.expense_input)

        self.category_input = QComboBox()
        self.layout.addWidget(QLabel("Categoría"))
        self.layout.addWidget(self.category_input)

        self.expense_date_input = QDateEdit()
        self.expense_date_input.setCalendarPopup(True)
        self.expense_date_input.setDate(QDate.currentDate())
        self.layout.addWidget(QLabel("Fecha del Gasto"))
        self.layout.addWidget(self.expense_date_input)

        self.add_expense_button = QPushButton("Añadir Gasto")
        self.add_expense_button.clicked.connect(self.add_expense)
        self.layout.addWidget(self.add_expense_button)

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["Tipo", "Monto", "Categoría", "Porcentaje", "Fecha"])
        self.layout.addWidget(self.table)

        self.balance_label = QLabel("Balance Total: 0")
        self.layout.addWidget(self.balance_label)

        self.daily_balance_table = QTableWidget(0, 5)
        self.daily_balance_table.setHorizontalHeaderLabels(
            ["Fecha", "Ingresos", "Gastos", "Balance Diario", "Porcentaje de Gasto"]
        )
        self.layout.addWidget(QLabel("Balance Diario"))
        self.layout.addWidget(self.daily_balance_table)

        self.monthly_balance_table = QTableWidget(0, 2)
        self.monthly_balance_table.setHorizontalHeaderLabels(["Mes", "Balance Mensual"])
        self.layout.addWidget(QLabel("Balance Mensual"))
        self.layout.addWidget(self.monthly_balance_table)

        self.show_daily_graph_button = QPushButton("Ver Gráfica de Gastos Diarios")
        self.show_daily_graph_button.clicked.connect(self.show_daily_graph)
        self.layout.addWidget(self.show_daily_graph_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        
        self.data = pd.DataFrame(columns=["Tipo", "Monto", "Categoría", "Fecha"])
        self.total_income = 0
        self.total_expenses = 0
        self.balance = 0

    def add_income(self):
        """Añade ingresos adicionales y actualiza el balance."""
        try:
            amount = float(self.income_input.text())
            date = QDate.currentDate().toString("yyyy-MM-dd")
            self.update_data("Ingreso", amount, "Ingreso", date)
            self.income_input.clear()
        except ValueError:
            print("Error: El monto del ingreso debe ser un número.")

    def add_category(self):
        """Añade una nueva categoría al ComboBox de categorías."""
        category_name = self.new_category_input.text().strip()
        if category_name and category_name not in [self.category_input.itemText(i) for i in range(self.category_input.count())]:
            self.category_input.addItem(category_name)
            self.new_category_input.clear()
        else:
            print("Error: La categoría ya existe o está vacía.")

    def add_expense(self):
        """Añade un gasto y actualiza el balance."""
        try:
            amount = float(self.expense_input.text())
            category = self.category_input.currentText()
            date = self.expense_date_input.date().toString("yyyy-MM-dd")
            self.update_data("Gasto", -amount, category, date)
            self.expense_input.clear()
        except ValueError:
            print("Error: El monto del gasto debe ser un número.")

    def update_data(self, tipo, monto, categoria, fecha):
        """Actualiza el DataFrame con la nueva transacción."""
        percentage = f"{abs(monto) / self.total_income * 100:.2f}%" if self.total_income > 0 else "0.00%"
        new_entry = pd.DataFrame([[tipo, monto, categoria, fecha]], columns=["Tipo", "Monto", "Categoría", "Fecha"])
        
        if not new_entry.empty:
            self.data = pd.concat([self.data, new_entry], ignore_index=True)
        else:
            print("Error: El nuevo registro está vacío y no se puede añadir.")

        if tipo == "Ingreso":
            self.total_income += monto
        elif tipo == "Gasto":
            self.total_expenses += -monto

        self.update_balance()

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(tipo))
        self.table.setItem(row_position, 1, QTableWidgetItem(str(monto)))
        self.table.setItem(row_position, 2, QTableWidgetItem(categoria))
        self.table.setItem(row_position, 3, QTableWidgetItem(percentage))
        self.table.setItem(row_position, 4, QTableWidgetItem(fecha))

    def update_balance(self):
        """Actualiza el balance total y lo muestra en la interfaz."""
        self.balance = self.total_income - self.total_expenses
        self.balance_label.setText(f"Balance Total: {self.balance}")
        self.update_daily_balance()
        self.update_monthly_balance()

    def update_daily_balance(self):
        """Actualiza el balance diario en la tabla."""
        daily_totals = self.data.groupby("Fecha")["Monto"].agg(["sum", "count"]).reset_index()
        self.daily_balance_table.setRowCount(0)

        for _, row in daily_totals.iterrows():
            ingresos = self.data[(self.data["Fecha"] == row["Fecha"]) & (self.data["Monto"] > 0)]["Monto"].sum()
            gastos = abs(self.data[(self.data["Fecha"] == row["Fecha"]) & (self.data["Monto"] < 0)]["Monto"].sum())
            porcentaje_gasto = f"{(gastos / ingresos * 100):.2f}%" if ingresos > 0 else "0.00%"

            row_position = self.daily_balance_table.rowCount()
            self.daily_balance_table.insertRow(row_position)
            self.daily_balance_table.setItem(row_position, 0, QTableWidgetItem(row["Fecha"]))
            self.daily_balance_table.setItem(row_position, 1, QTableWidgetItem(str(ingresos)))
            self.daily_balance_table.setItem(row_position, 2, QTableWidgetItem(str(gastos)))
            self.daily_balance_table.setItem(row_position, 3, QTableWidgetItem(str(ingresos - gastos)))
            self.daily_balance_table.setItem(row_position, 4, QTableWidgetItem(porcentaje_gasto))

    def update_monthly_balance(self):
        """Actualiza el balance mensual en la tabla."""
        self.data["Mes"] = pd.to_datetime(self.data["Fecha"]).dt.to_period("M")
        monthly_totals = self.data.groupby("Mes")["Monto"].sum()

        self.monthly_balance_table.setRowCount(0)
        for month, balance in monthly_totals.items():
            row_position = self.monthly_balance_table.rowCount()
            self.monthly_balance_table.insertRow(row_position)
            self.monthly_balance_table.setItem(row_position, 0, QTableWidgetItem(str(month)))
            self.monthly_balance_table.setItem(row_position, 1, QTableWidgetItem(str(balance)))

    def show_daily_graph(self):
        """Muestra una gráfica con los gastos diarios por categoría."""
        selected_row = self.daily_balance_table.currentRow()
        if selected_row < 0:
            print("Seleccione un día en la tabla de balances diarios.")
            return

        selected_date = self.daily_balance_table.item(selected_row, 0).text()
        daily_data = self.data[self.data["Fecha"] == selected_date]

        if daily_data.empty:
            print("No hay datos para la fecha seleccionada.")
            return

        category_totals = daily_data.groupby("Categoría")["Monto"].sum()

        fig, ax = plt.subplots()
        ax.pie(
            abs(category_totals),
            labels=category_totals.index,
            autopct='%1.1f%%',
            startangle=140
        )
        ax.set_title(f"Distribución de Gastos para {selected_date}")
        plt.show()


def start_app():
    app = QApplication(sys.argv)
    window = BudgetApp()
    window.show()
    sys.exit(app.exec_())


start_app()

