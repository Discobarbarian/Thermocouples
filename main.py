import sys
from PyQt5 import QtWidgets
import design


class Application(QtWidgets.QMainWindow, design.Ui_MainWindow):
    files = []
    input_data = {}

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.filebrowser_button.clicked.connect(self.file_browser)
        self.accept_button.clicked.connect(self.aggregate_input_data)

    def file_browser(self):
        rawfiles = QtWidgets.QFileDialog.getOpenFileNames(self, 'Выберите файлы:')
        files = rawfiles[0]  # rawfiles[0] потому что метод выше возвращает кортеж, первым элементом
        # которого является список путей файлов
        self.files_view.setText(str(files))
        print(files)  # удалить инструкцию после отладки
        self.files = files

    def aggregate_input_data(self):
        termocouples_list = []
        for item in self.termocouples_tree.selectedItems():
            termocouples_list.append(item.text(0))  # text(0) так как метод требует номер колонки из которой будет
            # взяты названия выбранных термопар
        if not(self.files and termocouples_list):  # небольшая процедура валидации
            print('calling error msg')  # удалить инструкцию после отладки
            print(termocouples_list)  # удалить инструкцию после отладки
            print(self.files)  # удалить инструкцию после отладки
            error = QtWidgets.QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Введены неверные данные')
            error.setInformativeText('Укажите файлы и выберите термопары и повторите попытку')
            error.setIcon(QtWidgets.QMessageBox.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error.setDetailedText('Возможно, не было указано ни одной термопары,'
                                  'или не выбраны файлы. Рекомендуется осуществлять'
                                  'выбор файлов с помощью кнопки "...", чтобы избежать'
                                  'некоррекных значений путей. РАССМОТРЕТЬ ЭТО ПОЛЕ К УДАЛЕНИЮ')

            error.exec_()
        else:
            input_data1 = dict(zip(['файлы', 'термопары'], [self.files, termocouples_list]))
            print(input_data1)  # удалить инструкцию после отладки
            print('Заебись! Все работает, можно передавать данные на бэк, юхууу!')  # удалить инструкцию после отладки


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
