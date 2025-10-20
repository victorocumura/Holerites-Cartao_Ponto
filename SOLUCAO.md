# SOLUCAO - Abordagem adotada

## Resumo
Desenvolvi uma aplicação em Python que varre todos os arquivos PDF dentro de uma pasta `data/`,
tenta identificar se o PDF é um *cartão de ponto* ou um *holerite* (pela presença de palavras-chave
no nome do arquivo ou no texto do documento) e aplica um parser genérico que:
- tenta extrair tabelas com `pdfplumber` (método preferencial);
- se não houver tabelas, extrai texto e aplica heurísticas para localizar linhas relevantes.

Os dados resultantes são consolidados em um `output.xlsx` com abas separadas para `Cartao_Ponto`
e `Holerite`.

## Decisões técnicas
- **Bibliotecas**: `pdfplumber` (leitura de PDF), `pandas` (manipulação e escrita Excel), `openpyxl`.
- **Heurísticas**: nome do arquivo (contendo `ponto`, `cartao`, `holerite`) e busca por palavras-chave
  nas primeiras páginas.
- **Erros**: tratamento básico com logs e continuação ao encontrar PDFs problemáticos.
- **Limitações**: PDFs escaneados (imagens) não são processados sem OCR; layout muito diferente pode exigir ajustes.
