import tkinter as tk
from tkinter import filedialog, messagebox
from manipula_imagem import *


class MenuTela:
    def __init__(self, window):
        self.window = window
        self.window.title("Menu")
        self.botao_clicado = None

        # Cria botões para as opções do menu

        self.mostrar_imagem_original = tk.Button(window,
                                                 text='Imagem Original',
                                                 command=manipula_imagem.mostrar_imagem_original,
                                                 state='disabled')

        self.mostrar_imagem_original.pack(pady=10)

        self.cvt_rgb_2_gray_button = tk.Button(window,
                                          text="Converter RGB --> GRAY",
                                          command=self.cvt_rgb_2_gray_button_click,
                                          state='disabled')
        self.cvt_rgb_2_gray_button.pack(pady=10)

        self.cvt_rgb_2_xyz_button = tk.Button(window,
                                         text="Converter RGB --> XYZ",
                                         command=self.cvt_rgb_2_xyz_button_click,
                                         state='disabled')
        self.cvt_rgb_2_xyz_button.pack(pady=10)

        self.cvt_rgb_2_ycrcb_button = tk.Button(window,
                                           text="Converter RGB --> YCrCb",
                                           command=self.cvt_rgb_2_ycrcb_button_click,
                                           state='disabled')
        self.cvt_rgb_2_ycrcb_button.pack(pady=10)

        self.cvt_rgb_2_hsv_button = tk.Button(window,
                                         text="Converter RGB --> HSV",
                                         command=self.cvt_rgb_2_hsv_button_click,
                                         state='disabled')
        self.cvt_rgb_2_hsv_button.pack(pady=10)

        self.cvt_rgb_2_hls_button = tk.Button(window,
                                         text="Converter RGB --> HLS",
                                         command=self.cvt_rgb_2_hls_button_click,
                                         state='disabled')
        self.cvt_rgb_2_hls_button.pack(pady=10)

        self.cvt_rgb_2_cielab_button = tk.Button(window,
                                            text="Converter RGB --> CIE L*a*b*",
                                            command=self.cvt_rgb_2_cielab_button_click,
                                            state='disabled')
        self.cvt_rgb_2_cielab_button.pack(pady=10)

        self.cvt_rgb_2_cieluv_button = tk.Button(window,
                                            text="Converter RGB --> CIE L*u*v*",
                                            command=self.cvt_rgb_2_cieluv_button_click,
                                            state='disabled')
        self.cvt_rgb_2_cieluv_button.pack(pady=10)

        self.gerar_histograma = tk.Button(window,
                                          text='Gerar Histograma',
                                          command=self.gerar_histograma,
                                          state='disabled')
        self.gerar_histograma.pack(pady=10)

        abrir_button = tk.Button(window, text="Abrir Arquivo", command=self.abrir_arquivo)
        abrir_button.pack(pady=10)

        self.salvar_button = tk.Button(window, text="Salvar Arquivo", command=self.salvar_arquivo, state='disabled')
        self.salvar_button.pack(pady=10)

        sair_button = tk.Button(window, text="Sair", command=self.sair)
        sair_button.pack(pady=10)

    def cvt_rgb_2_gray_button_click(self):
        self.botao_clicado = 'Converter RGB --> GRAY'
        manipula_imagem.converter_rgb_2_gray()

    def cvt_rgb_2_xyz_button_click(self):
        self.botao_clicado = 'Converter RGB --> XYZ'
        manipula_imagem.converter_rgb_2_xyz()

    def cvt_rgb_2_ycrcb_button_click(self):
        self.botao_clicado = 'Converter RGB --> YCrCb'
        manipula_imagem.converter_rgb_2_ycrcb()

    def cvt_rgb_2_hsv_button_click(self):
        self.botao_clicado = 'Converter RGB --> HSV'
        manipula_imagem.converter_rgb_2_hsv()

    def cvt_rgb_2_hls_button_click(self):
        self.botao_clicado = 'Converter RGB --> HLS'
        manipula_imagem.converter_rgb_2_hls()

    def cvt_rgb_2_cielab_button_click(self):
        self.botao_clicado = 'Converter RGB --> CIE L*a*b*'
        manipula_imagem.converter_rgb_2_cielab()

    def cvt_rgb_2_cieluv_button_click(self):
        self.botao_clicado = 'Converter RGB --> CIE L*u*v*'
        manipula_imagem.converter_rgb_2_cieluv()

    def gerar_histograma(self):
        manipula_imagem.gerar_histograma(self.botao_clicado)

    def habilitar_botoes_cvt(self):
        self.cvt_rgb_2_gray_button['state'] = 'normal'
        self.cvt_rgb_2_xyz_button['state'] = 'normal'
        self.cvt_rgb_2_ycrcb_button['state'] = 'normal'
        self.cvt_rgb_2_hsv_button['state'] = 'normal'
        self.cvt_rgb_2_hls_button['state'] = 'normal'
        self.cvt_rgb_2_cielab_button['state'] = 'normal'
        self.cvt_rgb_2_cieluv_button['state'] = 'normal'
        self.mostrar_imagem_original['state'] = 'normal'
        self.gerar_histograma['state'] = 'normal'
        self.salvar_button['state'] = 'normal'

    def abrir_arquivo(self):
        caminho_da_imagem = filedialog.askopenfilename()

        if caminho_da_imagem:
            print('Arquivo Selecionado', caminho_da_imagem)
            manipula_imagem.configurar_imagem(caminho_da_imagem)
            self.habilitar_botoes_cvt()
        else:
            print('Nenhum arquivo selecionado')
        pass

    def salvar_arquivo(self):
        manipula_imagem.salvar_imagens_geradas(self.botao_clicado)
        messagebox.showinfo("Salvar Arquivo", "Imagens salvas com sucesso!")

    def sair(self):
        if messagebox.askokcancel("Sair", "Deseja realmente sair?"):
            self.window.quit()


if __name__ == "__main__":
    manipula_imagem = ManipulaImagem()
    root = tk.Tk()
    app = MenuTela(root)
    root.mainloop()
