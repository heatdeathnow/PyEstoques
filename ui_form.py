from PySide6.QtWidgets import QDoubleSpinBox, QGridLayout, QLabel, QLineEdit, QScrollArea, QSizePolicy, QSpinBox, QToolButton, QWidget
from PySide6.QtCore import QMetaObject, QRect, QSize, Qt, QByteArray
from PySide6.QtGui import QIcon, QPixmap
from rw import push, pull
from PIL import Image
from io import BytesIO
from base64 import b64decode
import var


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        try:
            base_64_icon = b64decode(var.icon)  # Tranforma a string byte64 em bytes.
            pixmap = QPixmap()
            pixmap.loadFromData(base_64_icon)  # Retorna os bytes à imagem original.
            icon = QIcon(pixmap)  # Cria-se o ícone.
            MainWindow.setWindowIcon(icon)  # Coloca-se o ícone.
        except (TypeError, ValueError, AttributeError):
            pass

        MainWindow.resize(800, 600)  # Tamanho da janela
        MainWindow.setMinimumSize(QSize(800, 600))  # Fixa o tamanho
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 780, 580))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        var.price['contents'].append(QLabel(self.scrollAreaWidgetContents))  # O QLabel com o nome da coluna (preço).
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHeightForWidth(var.price['contents'][0].sizePolicy().hasHeightForWidth())
        var.price['contents'][0].setSizePolicy(sizePolicy)
        var.price['layout'].addWidget(var.price['contents'][0])
        self.gridLayout_2.addLayout(var.price['layout'], 0, 2, 1, 1)  # Coloca-o no layout.

        var.cost['contents'].append(QLabel(self.scrollAreaWidgetContents))  # O QLabel com o nome da coluna (custo total).
        sizePolicy.setHeightForWidth(var.cost['contents'][0].sizePolicy().hasHeightForWidth())
        var.cost['contents'][0].setSizePolicy(sizePolicy)
        var.cost['layout'].addWidget(var.cost['contents'][0])
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        self.gridLayout_2.addLayout(var.cost['layout'], 0, 6, 1, 1)  # Coloca-o no layout.

        var.item['contents'].append(QLabel(self.scrollAreaWidgetContents))  # O QLabel com o nome da coluna (nome do item).
        sizePolicy.setHeightForWidth(var.item['contents'][0].sizePolicy().hasHeightForWidth())
        var.item['contents'][0].setSizePolicy(sizePolicy)
        var.item['layout'].addWidget(var.item['contents'][0])
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        self.gridLayout_2.addLayout(var.item['layout'], 0, 3, 1, 1)  # Coloca-o no layout.

        var.delete['contents'].append(QLabel(self.scrollAreaWidgetContents))  # O QLabel com o nome da coluna (Excluir).
        sizePolicy.setHeightForWidth(var.delete['contents'][0].sizePolicy().hasHeightForWidth())
        var.delete['contents'][0].setSizePolicy(sizePolicy)
        var.delete['layout'].addWidget(var.delete['contents'][0])
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        self.gridLayout_2.addLayout(var.delete['layout'], 0, 0, 1, 1)  # Coloca-o no layout.

        var.tobuy['contents'].append(QLabel(self.scrollAreaWidgetContents))  # O QLabel com o nome da coluna (A comprar).
        sizePolicy.setHeightForWidth(var.tobuy['contents'][0].sizePolicy().hasHeightForWidth())
        var.tobuy['contents'][0].setSizePolicy(sizePolicy)
        var.tobuy['layout'].addWidget(var.tobuy['contents'][0])
        self.gridLayout_2.addLayout(var.tobuy['layout'], 0, 5, 1, 1)  # Coloca-o no layout.

        var.owned['contents'].append(QLabel(self.scrollAreaWidgetContents))  # O QLabel com o nome da coluna (disponíveis).
        sizePolicy.setHeightForWidth(var.owned['contents'][0].sizePolicy().hasHeightForWidth())
        var.owned['contents'][0].setSizePolicy(sizePolicy)
        var.owned['layout'].addWidget(var.owned['contents'][0])
        self.gridLayout_2.addLayout(var.owned['layout'], 0, 1, 1, 1)  # Coloca-o no layout.

        var.needed['contents'].append(QLabel(self.scrollAreaWidgetContents))  # O QLabel com o nome da coluna (necessários).
        sizePolicy.setHeightForWidth(var.needed['contents'][0].sizePolicy().hasHeightForWidth())
        var.needed['contents'][0].setSizePolicy(sizePolicy)
        var.needed['layout'].addWidget(var.needed['contents'][0])
        self.gridLayout_2.addLayout(var.needed['layout'], 0, 4, 1, 1)  # Coloca-o no layout.

        var.add['contents'].append(QLabel(self.scrollAreaWidgetContents))  # O QLabel com o nome da coluna (adicionar).
        sizePolicy.setHeightForWidth(var.add['contents'][0].sizePolicy().hasHeightForWidth())
        var.add['contents'][0].setSizePolicy(sizePolicy)
        var.add['layout'].addWidget(var.add['contents'][0])
        self.gridLayout_2.addLayout(var.add['layout'], 0, 7, 1, 1)  # Coloca-o no layout.

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)  # Coloca o conteúdo na tela
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)  # Coloca os textos
        QMetaObject.connectSlotsByName(MainWindow)

        # QLabels invisíveis e QLabel de custo total na última linha de todas as colunas.
        var.delete['contents'].append(QLabel(self.scrollAreaWidgetContents))
        var.delete['contents'][-1].setSizePolicy(sizePolicy)
        var.delete['layout'].addWidget(var.delete['contents'][-1])
        var.owned['contents'].append(QLabel(self.scrollAreaWidgetContents))
        var.owned['contents'][-1].setSizePolicy(sizePolicy)
        var.owned['layout'].addWidget(var.owned['contents'][-1])
        var.price['contents'].append(QLabel(self.scrollAreaWidgetContents))
        var.price['contents'][-1].setSizePolicy(sizePolicy)
        var.price['layout'].addWidget(var.price['contents'][-1])
        var.item['contents'].append(QLabel(self.scrollAreaWidgetContents))
        var.item['contents'][-1].setSizePolicy(sizePolicy)
        var.item['layout'].addWidget(var.item['contents'][-1])
        var.needed['contents'].append(QLabel(self.scrollAreaWidgetContents))
        var.needed['contents'][-1].setSizePolicy(sizePolicy)
        var.needed['layout'].addWidget(var.needed['contents'][-1])
        var.tobuy['contents'].append(QLabel(self.scrollAreaWidgetContents))
        var.tobuy['contents'][-1].setSizePolicy(sizePolicy)
        var.tobuy['layout'].addWidget(var.tobuy['contents'][-1])
        var.cost['contents'].append(QLabel(self.scrollAreaWidgetContents))
        var.cost['contents'][-1].setSizePolicy(sizePolicy)
        var.cost['contents'][-1].setText('Total R$ 0,00')
        var.cost['layout'].addWidget(var.cost['contents'][-1])
        var.add['contents'].append(QLabel(self.scrollAreaWidgetContents))
        var.add['contents'][-1].setSizePolicy(sizePolicy)
        var.add['layout'].addWidget(var.add['contents'][-1])

        self.load_rows()  # Carrega todas as colunas entre a primeira e a última.

    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("RK2 - Manutenção de estoques")
        var.price['contents'][0].setText("Último preço")
        var.cost['contents'][0].setText("Custo estimado")
        var.item['contents'][0].setText("Nome do item")
        var.delete['contents'][0].setText("Excluir")
        var.tobuy['contents'][0].setText("A comprar")
        var.owned['contents'][0].setText("Disponível")
        var.needed['contents'][0].setText("Necessários")
        var.add['contents'][0].setText("Adicionar")
    # retranslateUi

    def load_rows(self) -> None:
        """
        Lê o conteúdo anteriormente salvo no diretório do AppData e usa-o para reconstruir todas as linhas antes do programa ser fechado. 
        """

        dic = pull()  # Lê o arquivo e transforma um conteúno num dicionário-Python.
        for row in range(1, len(dic) + 1):  # O dicionário começa no 1 e não no 0.
            # Cada método adiciona conteúdo em suas respectivas colunas, algumas dessas colunas tem de ser tratadas diferentemente.
            self.add_delete(row)
            self.add_owned(row)
            self.add_price(row)
            self.add_item(row)
            self.add_needed(row)
            self.add_tobuy(row)
            self.add_cost(row)
            self.add_add(row)

            var.owned['contents'][row].blockSignals(True)  # É necessário bloquear o sinal temporariamente para não acioná-lo ao colocar o valor inicial.
            var.owned['contents'][row].setValue(int(dic[f'{row}'][0]))  # Carrega o valor dessa respectiva célula do dicionário para o QWidget.
            var.owned['contents'][row].blockSignals(False)  # Reabilita o sinal, agora que não será mais modificado programaticamente.

            var.price['contents'][row].blockSignals(True)  # Idem a todos os restantes nessa identação.
            var.price['contents'][row].setValue(float(dic[f'{row}'][1]))
            var.price['contents'][row].blockSignals(False)

            var.item['contents'][row].blockSignals(True)
            var.item['contents'][row].setText(dic[f'{row}'][2])
            var.item['contents'][row].blockSignals(False)

            var.needed['contents'][row].blockSignals(True)
            var.needed['contents'][row].setValue(int(dic[f'{row}'][3]))
            var.needed['contents'][row].blockSignals(False)
        self.set_labels()  # Carrega os QLabels com os textos certos.

    def set_labels(self, save: bool = False) -> None:
        """
        Coloca os valores (texto) nos QLabel em todas as colunas entre a primeira e a última e na última coluna na parte de "custo total" que fica abaixo
        de todas as células de custo na sua mesma coluna.
        """

        total = 0  # A soma do custo que será carregada no QLabel de custo total.
        for row in range(1, len(var.delete['contents']) - 1):  # Pula a primeira linha, pois são cabeçários; e pula a última linha, pois são invisíveis.
            price = var.price['contents'][row].value()
            owned = var.owned['contents'][row].value()
            needed = var.needed['contents'][row].value()

            tobuy = max(needed - owned, 0)  # Quanto se deve comprar: o quanto você precisa menos o quanto você tem. (Esse valor não vai abaixo de 0)
            cost = round(tobuy * price, 2)  # Qual o custo de tudo isso: o quanto você precisa comprar vezes o custo desse item.

            var.tobuy['contents'][row].setNum(tobuy)  # Coloca o valor no QLabel "a comprar" da respectiva linha.
            var.cost['contents'][row].setText(f'R$ {cost:.2f}'.replace('.', ','))  # Coloca o valor no QLabel "custo" da respectiva linha.
            total += cost  # Adiciona esse custo ao total a ser calculado.
        
        var.cost['contents'][-1].setText(f'Total R$ {total:.2f}'.replace('.', ','))  # Coloca o custo total, que é a soma de todos os custos.
        if save: push()  # Salve da memória para o disco, se não for imediatamente depois da inicialização.

    def reindex(self) -> None:
        """
        Reindexa as funções lambda dos QButtons e QSpinBoxes. Isso é necessário atualizar a qual linha cada botão e QSpinBox se refere depois de mudar a
        quantidade de linhas, senão pode haver desincronização. Provavelmente existe uma maneira de calcular quando a reindexação é necessário (pois ela
        certamente não é necessária ao adicionar uma linha no final), mas reindexar sempre não é tão computacionalmente problemático em máquinas atuais.
        """

        for i in range(1, len(var.add['contents']) - 1):  # Ignora a primeira e última linha.
            # Desconecta as conexões anteriores.
            var.add['contents'][i].clicked.disconnect()  
            var.delete['contents'][i].clicked.disconnect()
            var.owned['contents'][i].valueChanged.disconnect()
            var.needed['contents'][i].valueChanged.disconnect()
            var.price['contents'][i].valueChanged.disconnect()

            # Reconecta os QWidget, agora com as referências atualizadas.
            var.add['contents'][i].clicked.connect(lambda ignore = False, x = i : self.add_row(x + 1))
            var.delete['contents'][i].clicked.connect(lambda ignore = False, x = i : self.delete_row(x))
            var.owned['contents'][i].valueChanged.connect(lambda ignore = False, x = True : self.set_labels(x))
            var.needed['contents'][i].valueChanged.connect(lambda ignore = False, x = True : self.set_labels(x))
            var.price['contents'][i].valueChanged.connect(lambda ignore = False, x = True : self.set_labels(x))

    def add_row(self, row: int) -> None:
        """
        Chama todos os métodos que adicionam colunas para criar uma linha inteira.
        """

        self.add_delete(row)
        self.add_owned(row)
        self.add_price(row)
        self.add_item(row)
        self.add_needed(row)
        self.add_tobuy(row)
        self.add_cost(row)
        self.add_add(row)

        self.reindex()  # Isso é necessário depois de potencialmente adicionar uma linha entre duas outras e ela tomar seu índice.
        push()  # Salva da memória para o disco.

    def delete_row(self, row: int) -> None:
        """
        Deleta a linha cujo índice fora passado como argumento e então reindexa.
        """

        if len(var.delete['contents']) > 3:  # Não permite deletar a última linha. (3 = 1 cabeçário + 1 invisível + linha de verdade)
            # Remove da interface
            var.add['contents'][row].deleteLater()
            var.cost['contents'][row].deleteLater()
            var.tobuy['contents'][row].deleteLater()
            var.needed['contents'][row].deleteLater()
            var.item['contents'][row].deleteLater()
            var.price['contents'][row].deleteLater()
            var.owned['contents'][row].deleteLater()
            var.delete['contents'][row].deleteLater()

            # Remove da lista
            var.add['contents'].pop(row)
            var.cost['contents'].pop(row)
            var.tobuy['contents'].pop(row)
            var.needed['contents'].pop(row)
            var.item['contents'].pop(row)
            var.price['contents'].pop(row)
            var.owned['contents'].pop(row)
            var.delete['contents'].pop(row)
            
        self.reindex()  # Reindexa.
        push()  # Salva da memória para o disco.

    def add_delete(self, row):
        var.delete['contents'].insert(row, QToolButton(self.scrollAreaWidgetContents))
        var.delete['contents'][row].setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed))
        var.delete['contents'][row].setText('X')

        var.delete['contents'][row].clicked.connect(lambda ignore = False, x = row : self.delete_row(x))
        var.delete['layout'].insertWidget(row, var.delete['contents'][row])

    def add_owned(self, row):
        var.owned['contents'].insert(row, QSpinBox(self.scrollAreaWidgetContents))
        var.owned['contents'][row].valueChanged.connect(lambda ignore = False, x = True : self.set_labels(x))
        var.owned['layout'].insertWidget(row, var.owned['contents'][row])

    def add_price(self, row):
        var.price['contents'].insert(row, QDoubleSpinBox(self.scrollAreaWidgetContents))
        var.price['contents'][row].setMaximum(999.99)
        var.price['contents'][row].setPrefix("R$ ")
        var.price['contents'][row].valueChanged.connect(lambda ignore = False, x = True : self.set_labels(x))

        var.price['layout'].insertWidget(row, var.price['contents'][row])

    def add_item(self, row):
        var.item['contents'].insert(row, QLineEdit(self.scrollAreaWidgetContents))
        var.item['contents'][row]
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHeightForWidth(var.item['contents'][row].sizePolicy().hasHeightForWidth())
        var.item['contents'][row].setSizePolicy(sizePolicy4)
        var.item['contents'][row].setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        var.item['contents'][row].textChanged.connect(push)

        var.item['layout'].insertWidget(row, var.item['contents'][row])

    def add_needed(self, row):
        var.needed['contents'].insert(row, QSpinBox(self.scrollAreaWidgetContents))
        var.needed['contents'][row].valueChanged.connect(lambda ignore = False, x = True : self.set_labels(x))
        var.needed['layout'].insertWidget(row, var.needed['contents'][row])
    
    def add_tobuy(self, row):
        var.tobuy['contents'].insert(row, QLabel(self.scrollAreaWidgetContents))
        var.tobuy['contents'][row].setAlignment(Qt.AlignCenter)
        var.tobuy['contents'][row].setText("0")

        var.tobuy['layout'].insertWidget(row, var.tobuy['contents'][row])
    
    def add_cost(self, row):
        var.cost['contents'].insert(row, QLabel(self.scrollAreaWidgetContents))
        var.cost['contents'][row].setAlignment(Qt.AlignCenter)
        var.cost['contents'][row].setText("R$ 0,00")

        var.cost['layout'].insertWidget(row, var.cost['contents'][row])

    def add_add(self, row):
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        var.add['contents'].insert(row, QToolButton(self.scrollAreaWidgetContents))
        sizePolicy1.setHeightForWidth(var.add['contents'][row].sizePolicy().hasHeightForWidth())
        var.add['contents'][row].setSizePolicy(sizePolicy1)
        var.add['contents'][row].setText("+")
        var.add['contents'][row].clicked.connect(lambda ignore = False, x = row : self.add_row(x + 1))
        
        var.add['layout'].insertWidget(row, var.add['contents'][row])
