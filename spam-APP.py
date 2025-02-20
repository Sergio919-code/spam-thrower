import sys
import re
from PyQt5 import QtCore, QtGui, QtWidgets
import aiosmtplib , logging , asyncio, random , spam_words, functools, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid
import smtplib , threading

logging.basicConfig(level=logging.DEBUG, filename="spam.log" , filemode="w" , format="%(asctime)s - %(levelname)s - %(message)s")

class Ui_MainWindow(object):


    def __init__(self):
        self.login_status = False
        self.comitted = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(305, 332)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Main_Title = QtWidgets.QLabel(self.centralwidget)
        self.Main_Title.setGeometry(QtCore.QRect(10, 10, 285, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        self.Main_Title.setFont(font)
        self.Main_Title.setObjectName("Main_Title")
        self.Readme = QtWidgets.QPushButton(self.centralwidget)
        self.Readme.setGeometry(QtCore.QRect(208, 16, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.Readme.setFont(font)
        self.Readme.setObjectName("Readme")
        self.email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.email_input.setGeometry(QtCore.QRect(20, 40, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(8)
        self.email_input.setFont(font)
        self.email_input.setObjectName("email_input")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(20, 70, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(8)
        self.password_input.setFont(font)
        self.password_input.setObjectName("password_input")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(70, 100, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.status_bar = QtWidgets.QLabel(self.centralwidget)
        self.status_bar.setGeometry(QtCore.QRect(24, 224, 257, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.status_bar.setFont(font)
        self.status_bar.setAutoFillBackground(False)
        self.status_bar.setObjectName("status_bar")

        self.num_spams = QtWidgets.QLineEdit(self.centralwidget)
        self.num_spams.setGeometry(QtCore.QRect(20, 128, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(8)
        self.num_spams.setFont(font)
        self.num_spams.setObjectName("num_spams")

        self.target_email = QtWidgets.QLineEdit(self.centralwidget)
        self.target_email.setGeometry(QtCore.QRect(160, 128, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(8)
        self.target_email.setFont(font)
        self.target_email.setObjectName("target_email")

        self.commit_button = QtWidgets.QPushButton(self.centralwidget)
        self.commit_button.setGeometry(QtCore.QRect(112, 152, 65, 17))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(8)
        self.commit_button.setFont(font)
        self.commit_button.setObjectName("commit_button")
        self.spamming = QtWidgets.QPushButton(self.centralwidget)
        self.spamming.setGeometry(QtCore.QRect(72, 176, 153, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.spamming.setFont(font)
        self.spamming.setObjectName("spamming")
        self.pBar = QtWidgets.QProgressBar(self.centralwidget)
        self.pBar.setGeometry(QtCore.QRect(24, 280, 265, 23))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.pBar.setFont(font)
        self.pBar.setProperty("value", 0)
        self.pBar.setTextVisible(True)
        self.pBar.setObjectName("pBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ###### Customizations ####
        self.Main_Title.setWordWrap(True)
        self.Main_Title.setMinimumSize(QtCore.QSize(0 , 0))
        self.Readme.setMinimumSize(QtCore.QSize(0 , 0))
        self.status_bar.setWordWrap(True)
        self.pBar.setMinimumSize(QtCore.QSize(0 , 0))
        self.pBar.hide()

        self.Readme.clicked.connect(self.readme_button_clicked)        
        self.login_button.clicked.connect(self.login_button_clicked)
        self.commit_button.clicked.connect(self.commit_button_clicked)
        self.spamming.clicked.connect(self.spamming_button_clicked)

        self.email_input.setClearButtonEnabled(True)
        self.password_input.setClearButtonEnabled(True)
        self.num_spams.setClearButtonEnabled(False)
        self.target_email.setClearButtonEnabled(True)

        ### 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spam-Thrower"))
        self.Main_Title.setStatusTip(_translate("MainWindow", "Spam-Thrower!!!!"))
        self.Main_Title.setText(_translate("MainWindow", "Spam-Thrower!"))
        self.Readme.setStatusTip(_translate("MainWindow", "Read the instructions"))
        self.Readme.setText(_translate("MainWindow", "ReadMe"))
        self.email_input.setStatusTip(_translate("MainWindow", "Enter your email address"))
        self.email_input.setPlaceholderText(_translate("MainWindow", "your-email@example.com"))
        self.password_input.setStatusTip(_translate("MainWindow", "Enter your account password"))
        self.password_input.setPlaceholderText(_translate("MainWindow", "password: google recomended(App passward)"))
        self.login_button.setStatusTip(_translate("MainWindow", "Login to your account"))
        self.login_button.setText(_translate("MainWindow", "LOGIN"))
        self.status_bar.setStatusTip(_translate("MainWindow", "Current Status"))
        self.status_bar.setText(_translate("MainWindow", "STATUS:"))
        self.num_spams.setStatusTip(_translate("MainWindow", "Enter the number of spams you want to send"))
        self.num_spams.setPlaceholderText(_translate("MainWindow", "Number of spams>"))
        self.commit_button.setStatusTip(_translate("MainWindow", "Submit num of spams, Default 10"))
        self.commit_button.setText(_translate("MainWindow", "COMMIT"))
        self.spamming.setStatusTip(_translate("MainWindow", "Start sending"))
        self.spamming.setText(_translate("MainWindow", "SPAMMING! GO"))
        self.pBar.setStatusTip(_translate("MainWindow", "progress bar"))
        self.target_email.setStatusTip(_translate("MainWindow" , "Enter the target email address"))
        self.target_email.setPlaceholderText(_translate("MainWindow" , "Target Email Address"))

    def readme_button_clicked(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("ReadMe")
        msg_box.setTextFormat(QtCore.Qt.RichText)
        msg_box.setText("""
        <h1>ReadMe</h1>
        <h2>Instructions</h2>
        <ol>
            <li>Enter your email and password:</li>
            <ul>
                <li>For Gmail, if you turned on 2-step verification, you need to get an App password. <a href="https://support.google.com/accounts/answer/185833?hl=en">Get App Password</a></li>
            </ul>
            <li>Enter the number of spams you want to send</li>
            <li>Click on the commit button</li>
            <li>Click on the spamming button to start spamming</li>       
        </ol>
        <h2>Disclaimer</h2>
        <p>This tool is for educational purposes only. Do not use it for malicious purposes.</p>
            """
        
        )
        msg_box.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        msg_box.setIcon(QtWidgets.QMessageBox.NoIcon)
        msg_box.exec_()

    def get_email_input(self):
        email = self.email_input.text()
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            QtWidgets.QMessageBox.warning(None, "Invalid Email", "Please enter a valid email address.")
            return None
        
    def get_password_input(self):
        return self.password_input.text()
    
    def check_valid_login(self):    # Check if the login is valid
        if "gmail" in self.email:   # run in a sub thread
            try:
                server = smtplib.SMTP(host="smtp.gmail.com" , port=587)
                server.starttls()
                server.login(self.email , self.password)
                server.quit()
                self.login_status = True
                self.status_bar.setText("Login Successful")
            except Exception as e:
                logging.exception(f"Validating Login. Error: {str(e)}")
                self.status_bar.setText("Login Failed")     
                self.login_status = False
        # Add elif to support other email services
        else:
            self.login_status = False


    def login_button_clicked(self):
        self.email = self.get_email_input()
        self.password = self.get_password_input()
        if self.email and self.password:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Login")
            msg_box.setText("Checking Login...")
            msg_box.setIcon(QtWidgets.QMessageBox.NoIcon)
            msg_box.exec_()
            
            temp_thread = threading.Thread(target=self.check_valid_login)   # Check if the login is valid
            temp_thread.start()
            self.status_bar.setText("STATUS: Checking Login...")

    def get_num_spams(self):
        num_spams = self.num_spams.text()
        if num_spams:
            return int(num_spams)
        else:
            return 10
    
    def get_target_email(self):
        target_email = self.target_email.text()
        if re.match(r"[^@]+@[^@]+\.[^@]+", target_email):
            return target_email
        else:
            QtWidgets.QMessageBox.warning(None, "Invalid Email", "Please enter a valid email address.")
            return None
        
    def commit_button_clicked(self):
        if self.login_status:
            self.num_spams = self.get_num_spams()
            self.to_email = self.get_target_email()
            if self.num_spams and self.to_email:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setWindowTitle("Commit")
                msg_box.setText("Committed successfully.")
                msg_box.setIcon(QtWidgets.QMessageBox.NoIcon)
                msg_box.exec_()
                self.comitted = True
            else:
                QtWidgets.QMessageBox.warning(None, "Invalid Input", "Please enter the number of spams and the target email address.")
        else:
            QtWidgets.QMessageBox.warning(None , "Login Required" , "Please login to your account.")

    def update_progress(self):
        self.pBar.setValue(self.pBar.value() + 1)
        self.status_bar.setText("STATUS: Spamming...")

    def all_finished(self):
        self.pBar.setValue(0)
        self.pBar.hide()
        self.status_bar.setText("STATUS: Finished Spamming")
        self.spamming_thread.quit()

    def send_exception(self, i :int):
        self.status_bar.setText(f"STATUS: Failed to send email {i + 1}")

    def spamming_button_clicked(self):
        if self.login_status and self.comitted:
            self.pBar.setMaximum(self.num_spams)
            self.pBar.show()
            self.spamming_thread = SpammingThread(self.num_spams , self.email , self.password , self.to_email)
            self.spamming_thread.start()
            self.spamming_thread.update_progress.connect(self.update_progress)
            self.spamming_thread.all_finished.connect(self.all_finished)
            self.spamming_thread.send_exception.connect(self.send_exception)
        else:
            QtWidgets.QMessageBox.warning(None , "Invalid Input" , "Please login and commit before spamming.")

def retry(retries=3, delay=1):      # Retry decorator
    def decorator(func):
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if attempt < retries - 1:
                        await asyncio.sleep(delay)
                    else:
                        raise e

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < retries - 1:
                        time.sleep(delay)
                    else:
                        raise e

        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper

    return decorator


class SpammingThread(QtCore.QThread):
    unsupport_email = QtCore.pyqtSignal()
    slow_progress = QtCore.pyqtSignal()
    send_exception = QtCore.pyqtSignal(int)
    update_progress = QtCore.pyqtSignal()
    all_finished = QtCore.pyqtSignal()

    def __init__(self , num_spams , from_email , password , to_email):
        QtCore.QThread.__init__(self)
        self.num_spams = num_spams
        self.email = from_email
        self.password = password
        self.to_email = to_email

        self.unsupport_email.connect(self.handle_unsupported_email)
        self.slow_progress.connect(self.handle_slow_progress)



    def handle_unsupported_email(self):
        QtWidgets.QMessageBox.warning(None, "Unsupported Email", "The email service is not supported.")

    def handle_slow_progress(self):
        QtWidgets.QMessageBox.information(None, "Slow Progress", "Sending a large number of emails, this may take some time.")

    def run(self):
        total = self.num_spams
        bulk = total // 20
        remain = total % 20

        async def send_lse_20(remain , addition=0):
            tasks = []
            for i in range(remain):
                subject = spam_words.get_spam(random.randint(1,5))
                body = spam_words.get_spam(random.randint(10 , 20))
                tasks.append(self.a_send_email_google(subject , body , self.to_email , i + addition * 20))
            await asyncio.gather(*tasks)
        
        async def send_batch_20(index):
            tasks = []
            for k in range(20):
                i = index * 20 + k
                subject = spam_words.get_spam(random.randint(1, 5))
                body = spam_words.get_spam(random.randint(10, 20))
                tasks.append(self.a_send_email_google(subject, body, self.to_email, i))
            await asyncio.gather(*tasks)

        async def main():
            if bulk == 0:
                await send_lse_20(remain)
            else:
                for index in range(bulk):
                    await send_batch_20(index)
                if remain != 0:
                    await send_lse_20(remain , addition=bulk)
            self.all_finished.emit()

        asyncio.run(main())
            



        

    def old_run(self):
        if self.num_spams > 0 and self.num_spams <= 20:
            if "gmail" in self.email:
                for i in range(self.num_spams):
                    subject = spam_words.get_spam(random.randint(1 , 5))
                    body = spam_words.get_spam(random.randint(10 , 20))
                    asyncio.run(self.a_send_email_google(subject , body , self.to_email , i))

                self.all_finished.emit()
            else:
                self.unsupport_email.emit()

        elif self.num_spams > 20:
            if "gmail" in self.email:
                self.slow_progress.emit()
                for i in range(self.num_spams):
                    subject = spam_words.get_spam(random.randint(1 , 5))
                    body = spam_words.get_spam(random.randint(10 , 20))
                    self.send_email_google(subject , body , self.to_email , i)
                self.all_finished.emit()
            else:
                self.unsupport_email.emit()


    @retry()
    async def a_send_email_google(self , subject , body , to_email , i :int):
        from_email = self.email
        from_password = self.password

        try:
            msg = MIMEMultipart()
            msg["From"] = from_email
            msg["To"] = to_email
            msg["Subject"] = subject 
            msg["Date"] = formatdate(localtime=True)
            msg["Message-ID"] = make_msgid()
            msg["MIME-Version"] = "1.0"
            msg["Content-Type"] = "text/plain"

            msg.attach(MIMEText(body , "plain"))
            logging.info("Email created successfully")

            server  = aiosmtplib.SMTP(hostname="smtp.gmail.com" , port=587)
            await server.connect()
            logging.info("Connected to the server")

            await server.login(from_email , from_password)
            logging.info("Logged in")

            await server.send_message(msg)
            logging.info("Email sent successfully")
            self.update_progress.emit()
        
        except Exception as e:
            logging.exception(f"Failed to send email. Error: {str(e)}")
            self.send_exception.emit(i)

    @retry()
    def send_email_google(self , subject , body , to_email , i :int):
        from_email = self.email
        from_password = self.password

        try:
            msg = MIMEMultipart()
            msg["From"] = from_email
            msg["To"] = to_email
            msg["Subject"] = subject
            msg["Date"] = formatdate(localtime=True)
            msg["Message-ID"] = make_msgid()
            msg["MIME-Version"] = "1.0"
            msg["Content-Type"] = "text/plain"

            msg.attach(MIMEText(body , "plain"))
            logging.info("Email created successfully")

            server = smtplib.SMTP(host="smtp.gmail.com" , port=587)
            server.starttls()
            logging.info("Started TLS")

            server.login(from_email , from_password)
            logging.info("Logged in")

            server.send_message(msg)
            logging.info("Email sent successfully")

            server.quit()
            logging.info("Disconnected from the server")
            self.update_progress.emit()
        
        except Exception as e:
            logging.exception(f"Failed to send email. Error: {str(e)}")
            self.send_exception.emit(i)

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
