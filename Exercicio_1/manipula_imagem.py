import cv2
import threading
from matplotlib import pyplot as plt


class ManipulaImagem:
    imagem = None

    def configurar_imagem(self, caminho_da_imagem):
        self.imagem = cv2.imread(caminho_da_imagem)

    def mostrar_imagem_original(self):
        if self.imagem is not None:
            t = threading.Thread(target=self._mostrar_imagem_original)
            t.start()

    def _mostrar_imagem_original(self):
        cv2.namedWindow("teste", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("teste", self.imagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def converter_rgb_2_gray(self):
        t = threading.Thread(target=self._converter_rgb_2_gray)
        t.start()

    def _converter_rgb_2_gray(self):
        if self.imagem is not None:
            imagem_original = self.imagem.copy()
            self.nova_imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2GRAY)
            cv2.namedWindow("Convertida de RGB para GRAY", cv2.WINDOW_AUTOSIZE)
            cv2.imshow("Convertida de RGB para GRAY", self.nova_imagem)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        else:
            print('Nenhuma imagem carregada.')

    def converter_rgb_2_xyz(self):
        t = threading.Thread(target=self._converter_rgb_2_xyz)
        t.start()

    def _converter_rgb_2_xyz(self):
        if self.imagem is not None:
            imagem_original = self.imagem.copy()
            nova_imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2XYZ)
            self.gerar_imagem_em_canais("Convertida de RGB para XYZ", nova_imagem)
        else:
            print('Nenhuma imagem carregada.')

    def converter_rgb_2_ycrcb(self):
        t = threading.Thread(target=self._converter_rgb_2_ycrcb)
        t.start()

    def _converter_rgb_2_ycrcb(self):
        if self.imagem is not None:
            imagem_original = self.imagem.copy()
            nova_imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2YCrCb)
            self.gerar_imagem_em_canais("Convertida de RGB para YCrCb", nova_imagem)
        else:
            print('Nenhuma imagem carregada.')

    def converter_rgb_2_hsv(self):
        t = threading.Thread(target=self._converter_rgb_2_hsv)
        t.start()

    def _converter_rgb_2_hsv(self):
        if self.imagem is not None:
            imagem_original = self.imagem.copy()
            nova_imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2HSV)
            self.gerar_imagem_em_canais("Convertida de RGB para HSV", nova_imagem)
        else:
            print('Nenhuma imagem carregada.')

    def converter_rgb_2_hls(self):
        t = threading.Thread(target=self._converter_rgb_2_hls)
        t.start()

    def _converter_rgb_2_hls(self):
        if self.imagem is not None:
            imagem_original = self.imagem.copy()
            nova_imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2HLS)
            self.gerar_imagem_em_canais("Convertida de RGB para HLS", nova_imagem)
        else:
            print('Nenhuma imagem carregada.')

    def converter_rgb_2_cielab(self):
        t = threading.Thread(target=self._converter_rgb_2_cielab)
        t.start()

    def _converter_rgb_2_cielab(self):
        if self.imagem is not None:
            imagem_original = self.imagem.copy()
            nova_imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2LAB)
            self.gerar_imagem_em_canais("Convertida de RGB para CIE L*a*b*", nova_imagem)
        else:
            print('Nenhuma imagem carregada.')

    def converter_rgb_2_cieluv(self):
        t = threading.Thread(target=self._converter_rgb_2_cieluv)
        t.start()

    def _converter_rgb_2_cieluv(self):
        if self.imagem is not None:
            imagem_original = self.imagem.copy()
            nova_imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2LUV)
            self.gerar_imagem_em_canais("Convertida de RGB para CIE L*u*v*", nova_imagem)
        else:
            print('Nenhuma imagem carregada.')

    @staticmethod
    def gerar_imagem_em_canais(titulo, imagem):
        canais_de_cor = cv2.split(imagem)
        cv2.namedWindow(titulo, cv2.WINDOW_AUTOSIZE)
        cv2.imshow(titulo, imagem)
        cv2.namedWindow("Canal1", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Canal1", canais_de_cor[0])
        cv2.namedWindow("Canal2", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Canal2", canais_de_cor[1])
        cv2.namedWindow("Canal3", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Canal3", canais_de_cor[2])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def gerar_histograma(self, botao):
        if self.imagem is not None:
            imagem_original = self.imagem.copy()

            if botao == 'Converter RGB --> GRAY':
                hist = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2GRAY)
                self.plotar_histograma(hist, True)

            if botao == 'Converter RGB --> XYZ':
                hist = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2XYZ)
                self.plotar_histograma(hist)

            if botao == 'Converter RGB --> YCrCb':
                hist = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2YCrCb)
                self.plotar_histograma(hist)

            if botao == 'Converter RGB --> HSV':
                hist = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2HSV)
                self.plotar_histograma(hist)

            if botao == 'Converter RGB --> HLS':
                hist = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2HLS)
                self.plotar_histograma(hist)

            if botao == 'Converter RGB --> CIE L*a*b*':
                hist = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2LAB)
                self.plotar_histograma(hist)

            if botao == 'Converter RGB --> CIE L*u*v*':
                hist = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2LUV)
                self.plotar_histograma(hist)

    @staticmethod
    def plotar_histograma(hist, gray=False):
        if gray:
            plt.hist(hist.ravel(), 256, [0, 256])
            plt.xlabel('Valor do Pixel')
            plt.ylabel('Frequência')
            plt.title("Histograma da Escala de Cinza da Imagem")
        else:
            plt.figure(figsize=(15, 6))

            plt.subplot(131)
            canal_b = hist[:, :, 0]
            plt.hist(canal_b.ravel(), 256, [0, 256], color='blue')
            plt.xlabel('Valor do Pixel')
            plt.ylabel('Frequência')
            plt.title("Histograma do Canal B da Imagem")

            plt.subplot(132)
            canal_g = hist[:, :, 1]
            plt.hist(canal_g.ravel(), 256, [0, 256], color='green')
            plt.xlabel('Valor do Pixel')
            plt.ylabel('Frequência')
            plt.title("Histograma do Canal G da Imagem")

            plt.subplot(133)
            canal_r = hist[:, :, 2]
            plt.hist(canal_r.ravel(), 256, [0, 256], color='red')
            plt.xlabel('Valor do Pixel')
            plt.ylabel('Frequência')
            plt.title("Histograma do Canal R da Imagem")

            plt.tight_layout()

        plt.show()

    def salvar_imagens_geradas(self, botao):
        if self.imagem is not None:
            imagem_original = self.imagem.copy()

            if botao == 'Converter RGB --> GRAY':
                imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2GRAY)
                cv2.imwrite("./convertida.png", imagem, imagem)

            if botao == 'Converter RGB --> XYZ':
                imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2XYZ)
                imagem_em_canais = cv2.split(imagem)
                self.salvar_imagens(imagem_em_canais, imagem)

            if botao == 'Converter RGB --> YCrCb':
                imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2YCrCb)
                imagem_em_canais = cv2.split(imagem)
                self.salvar_imagens(imagem_em_canais, imagem)

            if botao == 'Converter RGB --> HSV':
                imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2HSV)
                imagem_em_canais = cv2.split(imagem)
                self.salvar_imagens(imagem_em_canais, imagem)

            if botao == 'Converter RGB --> HLS':
                imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2HLS)
                imagem_em_canais = cv2.split(imagem)
                self.salvar_imagens(imagem_em_canais, imagem)

            if botao == 'Converter RGB --> CIE L*a*b*':
                imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2LAB)
                imagem_em_canais = cv2.split(imagem)
                self.salvar_imagens(imagem_em_canais, imagem)

            if botao == 'Converter RGB --> CIE L*u*v*':
                imagem = cv2.cvtColor(imagem_original, cv2.COLOR_RGB2LUV)
                imagem_em_canais = cv2.split(imagem)
                self.salvar_imagens(imagem_em_canais, imagem)

    @staticmethod
    def salvar_imagens(canal, imagem_convertida):
        cv2.imwrite("imagem_convertida.png", imagem_convertida)
        cv2.imwrite("imagem_canal_1.png", canal[0])
        cv2.imwrite("imagem_canal_2.png", canal[1])
        cv2.imwrite("imagem_canal_3.png", canal[2])
