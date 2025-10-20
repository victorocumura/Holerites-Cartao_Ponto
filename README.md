# Desafio Programador - Extração de PDFs (Cartão de Ponto + Holerite)

Projeto de exemplo em **Python** que processa PDFs de cartões de ponto e holerites,
extraindo os dados para uma planilha Excel (`output.xlsx`).

## Como usar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Coloque seus PDFs na pasta `data/` (crie a pasta se não existir).

3. Execute a aplicação:
   ```bash
   python src/main.py --data-dir data --output output.xlsx
   ```

4. O arquivo `output.xlsx` será gerado na raiz do projeto (ou no caminho passado).

## Estrutura do projeto

- `src/` - código-fonte
- `data/` - coloque aqui os PDFs de entrada
- `output.xlsx` - planilha gerada pela aplicação
- `SOLUCAO.md` - documentação sobre a abordagem

## Observações
- O parser usa heurísticas genéricas (pdfplumber -> extração de tabelas e texto).
- PDFs escaneados (imagens) exigirão OCR (ex.: Tesseract) — não incluído por padrão.
