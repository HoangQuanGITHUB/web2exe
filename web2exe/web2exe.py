import os

class web2exe():
    title = ''
    url = ''
    filename = ''
    icon = ''
    def build():
        open(web2exe.filename + '.py','w').write(f'''from PyQt5.QtCore import *;
from PyQt5.QtWidgets import *;
from PyQt5.QtGui import *;
from PyQt5.QtWebEngineWidgets import *;
from PyQt5.QtPrintSupport import *;
import os;
import sys;
url = "{web2exe.url}";
class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs);		
		self.browser = QWebEngineView();
		self.browser.setUrl(QUrl(url));	
		self.setCentralWidget(self.browser);	
		self.status = QStatusBar();	
		self.showMaximized();
		self.show();
app = QApplication(sys.argv);
app.setApplicationName("{web2exe.title}");
window = MainWindow();
app.exec_();''')
        os.system(f'cmd /k "pyinstaller {web2exe.filename}.py --icon={web2exe.icon} --onefile --noconsole"')
        os.remove(f'{web2exe.filename}.py')
        os.remove(f'{web2exe.filename}.spec')
