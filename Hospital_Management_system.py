from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QLabel, QPushButton, QStackedWidget,
    QLineEdit, QDateEdit, QComboBox, QTextEdit, QTableWidget ,QTableWidgetItem , QDateTimeEdit
)

from PyQt5 import uic
import sys
import sqlite3

from searchwindow import Search_Window

#____________________________ create database______________________________________________

conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()
try:
    # for patient
    cursor.execute(""" CREATE TABLE IF NOT EXISTS patient(
        id integer PRIMARY KEY,
        full_name text NOT NULL,
        age integer NOT NULL,
        gender text NOT NULL,
        blood_group text NOT NULL,
        blood_pressure text NOT NULL,
        height text NOT NULL,
        weight text NOT NULL,
        body_temperature text NOT NULL,
        current_status text NOT NULL,
        medical_history text NOT NULL,
        treating_physician text NOT NULL,
        current_medication text NOT NULL
    
    )""")

    # for doctor
    cursor.execute(""" CREATE TABLE IF NOT EXISTS doctor(
    id integer PRIMARY KEY,
    full_name text NOT NULL,
    gender text NOT NULL,
    age integer NOT NULL,
    medical_license_number integer NOT NULL,
    specialty text NOT NULL,
    department text NOT NULL,
    room_number integer NOT NULL,
    work_schedule text NOT NULL,
    phone_number integer NOT NULL,
    email_address text NOT NULL
  
    )""")

    # for admission
    cursor.execute(""" CREATE TABLE IF NOT EXISTS admission(
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    case_number TEXT NOT NULL,
    national_number TEXT NOT NULL,
    visit_reasons TEXT NOT NULL,
    insurance_number TEXT NOT NULL,
    admission_date TEXT NOT NULL,
    status TEXT NOT NULL

    
    )""")

    conn.commit()

except Exception as e:
    print(" Error in making databases : ", e)
    conn.rollback()


conn.close()




#_____________________________________________ main window_________________________________________________

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        #load UI File
        uic.loadUi('UI Files/Hospital_Management_system.ui',self)

        # define widgets in main stacked widget page 1 ( login page )
        self.background_label = self.findChild(QLabel,'background_label')
        self.login_label = self.findChild(QLabel,'login_label')
        self.username_label = self.findChild(QLabel,'username_label')
        self.username_lineEdit = self.findChild(QLineEdit,'username_lineEdit')
        self.password_label = self.findChild(QLabel,'password_label')
        self.password_lineEdit = self.findChild(QLineEdit,'password_lineEdit')
        self.login_pushButton = self.findChild(QPushButton,'login_pushButton')
        self.stackedWidget_1 = self.findChild(QStackedWidget,'stackedWidget')

        self.stackedWidget_1.setCurrentIndex(0)


        # define widgets in main stacked widget page 2
        self.label2 = self.findChild(QLabel,'label2')
        self.patient_pushButton = self.findChild(QPushButton,'patient_pushButton')
        self.doctor_pushButton = self.findChild(QPushButton,'doctor_pushButton')
        self.admission_pushButton = self.findChild(QPushButton,'admission_pushButton')
        self.search_pushButton = self.findChild(QPushButton,'search_pushButton')
        self.stackedWidget_2 = self.findChild(QStackedWidget,'stackedWidget_2')


        # __________________________________________(patient page)________________________________________________

        # define widgets in second stacked widget page 1
        self.p_fullname_label = self.findChild(QLabel,'p_fullname_label')
        self.p_fullname_lineEdit = self.findChild(QLineEdit,'p_fullname_lineEdit')
        self.p_age_label = self.findChild(QLabel,'p_age_label')
        self.p_age_dateEdit = self.findChild(QDateEdit,'p_age_dateEdit')
        self.p_gender_label = self.findChild(QLabel,'p_gender_label')
        self.p_gender_comboBox = self.findChild(QComboBox,'p_gender_comboBox')
        self.p_gender_comboBox.setCurrentIndex(-1)
        self.blood_group_label = self.findChild(QLabel,'blood_group_label')
        self.blood_group_comboBox.setCurrentIndex(-1)
        self.blood_group_comboBox = self.findChild(QComboBox,'blood_group_comboBox')
        self.blood_pressure_label = self.findChild(QLabel,'blood_pressure_label')
        self.blood_pressure_lineEdit = self.findChild(QLineEdit,'blood_pressure_lineEdit')
        self.height_label = self.findChild(QLabel,'height_label')
        self.height_lineEdit = self.findChild(QLineEdit,'height_lineEdit')
        self.weight_label = self.findChild(QLabel,'weight_label')
        self.weight_lineEdit = self.findChild(QLineEdit,'weight_lineEdit')
        self.body_temperature_label = self.findChild(QLabel,'body_temperature_label')
        self.body_temperature_lineEdit = self.findChild(QLineEdit,'body_temperature_lineEdit')
        self.current_status_label = self.findChild(QLabel,'current_status_label')
        self.current_status_comboBox = self.findChild(QComboBox,'current_status_comboBox')
        self.current_status_comboBox.setCurrentIndex(-1)
        self.medical_history_label = self.findChild(QLabel,'medical_history_label')
        self.medical_history_textEdit = self.findChild(QTextEdit,'medical_history_textEdit')
        self.treating_physician_label = self.findChild(QLabel,'treating_physician_label')
        self.treating_physician_lineEdit = self.findChild(QLineEdit,'treating_physician_lineEdit')
        self.current_medication_label = self.findChild(QLabel,'current_medication_label')
        self.current_medication_textEdit = self.findChild(QTextEdit,'current_medication_textEdit')
        self.add_patient_pushButton = self.findChild(QPushButton,'add_patient_pushButton')
        self.update_patient_pushButton = self.findChild(QPushButton,'update_patient_pushButton')
        self.delete_patient_pushButton = self.findChild(QPushButton,'delete_patient_pushButton')
        self.patient_tableWidget = self.findChild(QTableWidget,'patient_tableWidget')
        self.load_table("patient", self.patient_tableWidget)

        self.stackedWidget_2.setCurrentIndex(0)

        # patient table column width design
        self.patient_tableWidget.setColumnWidth(0,20)
        self.patient_tableWidget.setColumnWidth(1, 100)
        self.patient_tableWidget.setColumnWidth(2, 100)
        self.patient_tableWidget.setColumnWidth(3, 100)
        self.patient_tableWidget.setColumnWidth(4, 200)
        self.patient_tableWidget.setColumnWidth(5, 200)
        self.patient_tableWidget.setColumnWidth(6, 100)
        self.patient_tableWidget.setColumnWidth(7, 100)
        self.patient_tableWidget.setColumnWidth(8, 200)
        self.patient_tableWidget.setColumnWidth(9, 200)
        self.patient_tableWidget.setColumnWidth(10, 300)
        self.patient_tableWidget.setColumnWidth(11, 200)
        self.patient_tableWidget.setColumnWidth(12, 300)

        self.patient_tableWidget.verticalHeader().setVisible(False)

        #__________________________________________(doctor page)_______________________________________________

        # define widgets in second stacked widget page 2
        self.d_fullname_label = self.findChild(QLabel,'d_fullname_label')
        self.d_fullname_lineEdit = self.findChild(QLineEdit,'d_fullname_lineEdit')
        self.specialty_label = self.findChild(QLabel,'specialty_label')
        self.specialty_lineEdit = self.findChild(QLineEdit,'specialty_lineEdit')
        self.department_label = self.findChild(QLabel,'department_label')
        self.department_lineEdit = self.findChild(QLineEdit,'department_lineEdit')
        self.room_number_label = self.findChild(QLabel,'room_number_label')
        self.room_number_lineEdit = self.findChild(QLineEdit,'room_number_lineEdit')
        self.d_gender_label = self.findChild(QLabel,'d_gender_label')
        self.d_gender_comboBox = self.findChild(QComboBox,'d_gender_comboBox')
        self.d_gender_comboBox.setCurrentIndex(-1)
        self.medical_license_number_label = self.findChild(QLabel,'medical_license_number_label')
        self.medical_license_number_lineEdit = self.findChild(QLineEdit,'medical_license_number_lineEdit')
        self.work_schedule_label = self.findChild(QLabel,'work_schedule_label')
        self.work_schedule_lineEdit = self.findChild(QLineEdit,'work_schedule_lineEdit')
        self.d_phone_number_label = self.findChild(QLabel,'d_phone_number_label')
        self.d_phone_number_lineEdit = self.findChild(QLineEdit,'d_phone_number_lineEdit')
        self.email_address_label = self.findChild(QLabel,'email_address_label')
        self.email_address_lineEdit = self.findChild(QLineEdit,'email_address_lineEdit')
        self.d_age_label = self.findChild(QLabel,'d_age_label')
        self.d_age_dateEdit = self.findChild(QDateEdit,'d_age_dateEdit')
        self.add_doctor_pushButton = self.findChild(QPushButton,'add_doctor_pushButton')
        self.update_doctor_pushButton = self.findChild(QPushButton,'update_doctor_pushButton')
        self.delete_doctor_pushButton = self.findChild(QPushButton,'delete_doctor_pushButton')
        self.doctor_tableWidget = self.findChild(QTableWidget,'doctor_tableWidget')
        self.load_table("doctor", self.doctor_tableWidget)

        # doctor table column width design
        self.doctor_tableWidget.setColumnWidth(0, 20)
        self.doctor_tableWidget.setColumnWidth(1, 100)
        self.doctor_tableWidget.setColumnWidth(2, 100)
        self.doctor_tableWidget.setColumnWidth(3, 100)
        self.doctor_tableWidget.setColumnWidth(4, 300)
        self.doctor_tableWidget.setColumnWidth(5, 100)
        self.doctor_tableWidget.setColumnWidth(6, 200)
        self.doctor_tableWidget.setColumnWidth(7, 200)
        self.doctor_tableWidget.setColumnWidth(8, 200)
        self.doctor_tableWidget.setColumnWidth(9, 200)
        self.doctor_tableWidget.setColumnWidth(10, 300)

        self.doctor_tableWidget.verticalHeader().setVisible(False)

        #___________________________________________(admission page)___________________________________________________

        # define widgets in second stacked widget page 3
        self.a_fullname_label = self.findChild(QLabel,'a_fullname_label')
        self.a_fullname_lineEdit = self.findChild(QLineEdit,'a_fullname_lineEdit')
        self.case_number_label = self.findChild(QLabel,'case_number_label')
        self.case_number_lineEdit = self.findChild(QLineEdit,'case_number_lineEdit')
        self.national_id_label = self.findChild(QLabel,'national_id_label')
        self.national_id_lineEdit = self.findChild(QLineEdit,'national_id_lineEdit')
        self.visit_reason_label = self.findChild(QLabel,'visit_reason_label')
        self.visit_reason_comboBox = self.findChild(QComboBox,'visit_reason_comboBox')
        self.visit_reason_comboBox.setCurrentIndex(-1)
        self.insurance_number_label = self.findChild(QLabel,'insurance_number_label')
        self.insurance_number_lineEdit = self.findChild(QLineEdit,'insurance_number_lineEdit')
        self.admission_date_label = self.findChild(QLabel,'admission_date_label')
        self.admission_dateTimeEdit = self.findChild(QDateTimeEdit,'admission_dateTimeEdit')
        self.status_label = self.findChild(QLabel,'status_label')
        self.status_textEdit = self.findChild(QTextEdit,'status_textEdit')
        self.add_admission_pushButton = self.findChild(QPushButton,'add_admission_pushButton')
        self.update_admission_pushButton = self.findChild(QPushButton,'update_admission_pushButton')
        self.delete_admission_pushButton = self.findChild(QPushButton,'delete_admission_pushButton')
        self.admission_tableWidget = self.findChild(QTableWidget,'admission_tableWidget')
        self.load_table("admission", self.admission_tableWidget)

        # admission table column width design
        self.admission_tableWidget.setColumnWidth(0, 20)
        self.admission_tableWidget.setColumnWidth(1, 100)
        self.admission_tableWidget.setColumnWidth(2, 200)
        self.admission_tableWidget.setColumnWidth(3, 200)
        self.admission_tableWidget.setColumnWidth(4, 200)
        self.admission_tableWidget.setColumnWidth(5, 300)
        self.admission_tableWidget.setColumnWidth(6, 200)
        self.admission_tableWidget.setColumnWidth(7, 300)

        self.admission_tableWidget.verticalHeader().setVisible(False)


        #______________________________________________(Buttons Connection )_______________________________________

        # link buttons with stacked widget pages

        self.patient_pushButton.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(0))
        self.doctor_pushButton.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(1))
        self.admission_pushButton.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(2))

        # connect buttons to their functions
        self.login_pushButton.clicked.connect(self.login)
        self.login_pushButton.setDefault(True)                      # Enter triggers login
        self.password_lineEdit.returnPressed.connect(self.login)    # Enter in password field triggers login
        self.add_patient_pushButton.clicked.connect(self.add_patient)
        self.add_doctor_pushButton.clicked.connect(self.add_doctor)
        self.add_admission_pushButton.clicked.connect(self.add_admission)
        self.delete_patient_pushButton.clicked.connect(lambda: self.delete_record("patient", self.patient_tableWidget))
        self.delete_doctor_pushButton.clicked.connect(lambda: self.delete_record("doctor", self.doctor_tableWidget))
        self.delete_admission_pushButton.clicked.connect(lambda: self.delete_record("admission", self.admission_tableWidget))
        self.update_patient_pushButton.clicked.connect(self.update_record)
        self.update_doctor_pushButton.clicked.connect(self.update_record)
        self.update_admission_pushButton.clicked.connect(self.update_record)
        self.search_pushButton.clicked.connect(self.open_search_window)

        # show main window
        self.show()


    # ____________________________________define functions__________________________________________

    # login function
    def login(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        if username == 'root' and password == '1234':
            self.stackedWidget_1.setCurrentIndex(1)




    # INSERT to database
    def insert_record(self,table_name, columns, values):
        try:
            conn = sqlite3.connect("hospital.db")
            cursor = conn.cursor()
            placeholders = ",".join(["?"] * len(values))
            sql = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"
            cursor.execute(sql, values)
            conn.commit()
            conn.close()

        except Exception as e:
            print(" Error in insert_record function : ", e)
            conn.rollback()




    # UPDATE to database(with mapping-based dispatch method)
    def update_record(self):
        try:
            # map index to table widget and table name
            table_map = {
                0: (self.patient_tableWidget, "patient"),
                1: (self.doctor_tableWidget, "doctor"),
                2: (self.admission_tableWidget, "admission")
            }

            # get current table
            current_index = self.stackedWidget_2.currentIndex()

            # get table widget and table name by index from current_index
            table_widget, table_name = table_map[current_index]

            # selected row and record id
            selected_row = table_widget.currentRow()

            # if no row is selected, exit safely
            if selected_row < 0:
                return

            # Get ID from first column of selected row
            record_id = table_widget.item(selected_row, 0).text()

            # Collect header names for columns 1..N (excluding ID in column 0)
            columns = [table_widget.horizontalHeaderItem(i).text()
                       for i in range(1, table_widget.columnCount())]

            # Collect cell values (excluding ID) from the selected row
            values = [(table_widget.item(selected_row, col).text()
                       if table_widget.item(selected_row, col) else "")
                      for col in range(1, table_widget.columnCount())]

            # build query
            set_clause = ",".join([f"{col}=?" for col in columns])
            sql = f"UPDATE {table_name} SET {set_clause} WHERE id=?"

            # execute update
            try:
                with sqlite3.connect("hospital.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute(sql, values + [record_id])
                    conn.commit()

                print(f"Record with id : {record_id} updated in table : {table_name}")

            except Exception as e:
                print("Error updating database: ", e)

        except Exception as e:
            print("Error in update_record: ", e)




    # DELETE from database and QTableWidget ( with direct callback binding method)
    def delete_record(self, table_name, table_widget):
        try:
            # check if any row is selected
            selected_row = table_widget.currentRow()
            if selected_row < 0:
                return

            # get record id from first column
            record_id = table_widget.item(selected_row, 0).text()

            # delete from database safely
            with sqlite3.connect("hospital.db") as conn:
                cursor = conn.cursor()
                cursor.execute(f"DELETE FROM {table_name} WHERE id=?", (record_id,))
                conn.commit()

            # delete from QTableWidget
            table_widget.removeRow(selected_row)

            print(f"Record with id : {record_id} deleted from table : {table_name}")

        except Exception as e:
            print("Error in delete_record:", e)




    # SELECT data from database and show in table widget
    def load_table(self, table_name, widget):
        try:
            with sqlite3.connect("hospital.db") as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()
                headers = [desc[0] for desc in cursor.description]


                # Clear the widget before loading new data
                widget.setRowCount(len(rows))
                widget.setColumnCount(len(headers))
                widget.setHorizontalHeaderLabels(headers)

                # Populate the table widget with data from database
                for row_idx, row_data in enumerate(rows):
                    for col_idx, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        widget.setItem(row_idx, col_idx, item)

        except Exception as e:
            print(f" Error in load_table function :", e)




    def add_patient(self):

        # Collect patient information from form fields

        p_fullname = self.p_fullname_lineEdit.text()
        p_age = self.p_age_dateEdit.date().toString("yyyy-MM-dd")
        p_gender = self.p_gender_comboBox.currentText()
        blood_group = self.blood_group_comboBox.currentText()
        blood_pressure = self.blood_pressure_lineEdit.text()
        height = self.height_lineEdit.text()
        weight = self.weight_lineEdit.text()
        body_temperature = self.body_temperature_lineEdit.text()
        current_status = self.current_status_comboBox.currentText()
        medical_history = self.medical_history_textEdit.toPlainText()
        treating_physician = self.treating_physician_lineEdit.text()
        current_medication = self.current_medication_textEdit.toPlainText()

        # Define database column names

        columns = [
            "full_name", "age", "gender", "blood_group",
            "blood_pressure", "height", "weight",
            "body_temperature", "current_status",
            "medical_history", "treating_physician",
            "current_medication"
        ]

        # Collect values from form fields in the same order as columns

        values = [
            p_fullname, p_age, p_gender, blood_group,
            blood_pressure, height, weight,
            body_temperature, current_status,
            medical_history, treating_physician,
            current_medication
        ]

        try :
            # Insert new patient record into the database
            self.insert_record("patient", columns, values)

            # Refresh patient table to show the newly added record
            self.load_table("patient", self.patient_tableWidget)

            # Clear form fields after successful insertion

            self.p_fullname_lineEdit.clear()
            self.p_gender_comboBox.setCurrentIndex(-1)
            self.p_age_dateEdit.setDate(self.p_age_dateEdit.minimumDate())
            self.blood_group_comboBox.setCurrentIndex(-1)
            self.blood_pressure_lineEdit.clear()
            self.height_lineEdit.clear()
            self.weight_lineEdit.clear()
            self.body_temperature_lineEdit.clear()
            self.current_status_comboBox.setCurrentIndex(-1)
            self.medical_history_textEdit.clear()
            self.treating_physician_lineEdit.clear()
            self.current_medication_textEdit.clear()

        except Exception as e:
            print("Error in add_patient function : ", e)




    def add_doctor(self):

        d_fullname = self.d_fullname_lineEdit.text()
        d_gender = self.d_gender_comboBox.currentText()
        d_age = self.d_age_dateEdit.date().toString("yyyy-MM-dd")
        medical_license_number = self.medical_license_number_lineEdit.text()
        specialty = self.specialty_lineEdit.text()
        department = self.department_lineEdit.text()
        room_number = self.room_number_lineEdit.text()
        work_schedule = self.work_schedule_lineEdit.text()
        phone_number = self.d_phone_number_lineEdit.text()
        email_address = self.email_address_lineEdit.text()

        columns = [
            "full_name", "gender", "age", "medical_license_number",
            "specialty", "department", "room_number",
            "work_schedule", "phone_number", "email_address"
        ]

        values = [
            d_fullname, d_gender, d_age, medical_license_number,
            specialty, department, room_number,
            work_schedule, phone_number, email_address
        ]

        try:
            self.insert_record("doctor", columns, values)
            self.load_table("doctor", self.doctor_tableWidget)


            self.d_fullname_lineEdit.clear()
            self.d_gender_comboBox.setCurrentIndex(-1)
            self.d_age_dateEdit.setDate(self.d_age_dateEdit.minimumDate())
            self.medical_license_number_lineEdit.clear()
            self.specialty_lineEdit.clear()
            self.department_lineEdit.clear()
            self.room_number_lineEdit.clear()
            self.work_schedule_lineEdit.clear()
            self.d_phone_number_lineEdit.clear()
            self.email_address_lineEdit.clear()

        except Exception as e:
            print("Error in add_doctor function : ", e)




    def add_admission(self):

        a_fullname = self.a_fullname_lineEdit.text()
        case_number = self.case_number_lineEdit.text()
        national_number = self.national_id_lineEdit.text()
        visit_reasons = self.visit_reason_comboBox.currentText()
        insurance_number = self.insurance_number_lineEdit.text()
        admission_date = self.admission_dateTimeEdit.date().toString("yyyy-MM-dd")
        status = self.status_textEdit.toPlainText()

        columns = [
            "full_name", "case_number", "national_number",
            "visit_reasons", "insurance_number", "admission_date", "status"
        ]

        values = [
            a_fullname, case_number, national_number,
            visit_reasons, insurance_number, admission_date, status
        ]


        try:
            self.insert_record("admission", columns, values)
            self.load_table("admission", self.admission_tableWidget)


            self.a_fullname_lineEdit.clear()
            self.case_number_lineEdit.clear()
            self.national_id_lineEdit.clear()
            self.visit_reason_comboBox.setCurrentIndex(-1)
            self.insurance_number_lineEdit.clear()
            self.admission_dateTimeEdit.setDate(self.admission_dateTimeEdit.minimumDate())
            self.status_textEdit.clear()

        except Exception as e:
            print("Error in add_admission function : ", e)


    def open_search_window(self):
        self.window2 = Search_Window()
        self.window2.show()





# initialized the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()



