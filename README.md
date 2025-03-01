# FileOrg - Organizador de Arquivos

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

Este projeto é um organizador de arquivos automatizado desenvolvido em Python com interface gráfica utilizando Tkinter. Ele permite selecionar uma pasta de origem e uma pasta de destino, categorizando automaticamente os arquivos com base em suas extensões.

## 📂 Funcionalidades
- **Interface gráfica amigável** usando Tkinter
- **Organização automática de arquivos** em categorias:
  - 📷 Imagens
  - 🎥 Vídeos
  - 🎵 Áudio
  - 📄 Documentos
  - 📦 Compactados
  - ⚙️ Executáveis
  - 🖥️ Arquivos 3D
- **Movimentação de pastas** para uma categoria específica
- **Registro de logs** em tempo real na interface

## 🛠️ Tecnologias Utilizadas
- 🐍 **Python 3**
- 🖼️ **Tkinter** (GUI)
- 📂 `shutil` (movimentação de arquivos)
- 📁 `os` (manipulação de diretórios)

## 🔧 Como Executar
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/organizador-arquivos.git
   cd organizador-arquivos
   ```
2. **Instale as dependências (opcional, caso esteja usando um ambiente virtual):**
   ```bash
   pip install -r requirements.txt
   ```
3. **Execute o programa:**
   ```bash
   python organizador.py
   ```

## 🏗️ Como Criar o Executável
Se desejar criar um **.exe** para Windows:

1. **Instale o PyInstaller:**
   ```bash
   pip install pyinstaller
   ```
2. **Gere o executável:**
   ```bash
   pyinstaller --onefile --windowed organizador.py
   ```
3. **O arquivo `.exe` estará na pasta `dist/`.**

## 📸 Captura de Tela
Pendente.

## 📜 Licença
Este projeto está sob a **licença MIT**. Sinta-se livre para modificar e distribuir!

## 🤝 Contribuições
Contribuições são bem-vindas! Para contribuir:
1. **Fork** o repositório
2. **Crie um branch** (`git checkout -b feature-nome`)
3. **Faça suas alterações** e commit (`git commit -m "Descrição"`)
4. **Envie para o GitHub** (`git push origin feature-nome`)
5. **Abra um Pull Request 🚀**

---
🔗 **Contato:** Se tiver dúvidas ou sugestões, abra uma **issue** ou me encontre em [seu perfil no GitHub](https://github.com/seu-usuario).

