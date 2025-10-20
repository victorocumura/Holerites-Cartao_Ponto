import argparse
import os
from parsers.time_card_parser import TimeCardParser
from parsers.payroll_parser import PayrollParser
from utils.excel_writer import ExcelWriter

def is_timecard(filename, text_snippet):
    fn = filename.lower()
    if any(k in fn for k in ['ponto', 'cartao', 'cartão']):
        return True
    if 'entrada' in text_snippet.lower() and 'saida' in text_snippet.lower():
        return True
    return False

def is_payroll(filename, text_snippet):
    fn = filename.lower()
    if 'holerite' in fn or 'holer' in fn:
        return True
    if 'proventos' in text_snippet.lower() or 'descontos' in text_snippet.lower():
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description='Extrai dados de PDFs e gera uma planilha Excel.')
    parser.add_argument('--data-dir', default='data', help='Pasta com arquivos PDF')
    parser.add_argument('--output', default='output.xlsx', help='Arquivo Excel de saída')
    args = parser.parse_args()

    data_dir = args.data_dir
    if not os.path.exists(data_dir):
        print(f'Pasta {data_dir} não existe. Crie e coloque os PDFs lá.')
        return

    timecard_dfs = []
    payroll_dfs = []

    
    for fname in sorted(os.listdir(data_dir)):
        if not fname.lower().endswith('.pdf'):
            continue
        path = os.path.join(data_dir, fname)
        print(f'Processando: {fname}')
 
        try:
            from pdfplumber import open as pb_open
            with pb_open(path) as pdf:
                text_snippet = ''
                for p in pdf.pages[:2]:
                    text_snippet += (p.extract_text() or '') + '\n'
        except Exception as e:
            print(f'  [WARN] não foi possível ler texto do PDF: {e}')
            text_snippet = ''

        try:
            if is_timecard(fname, text_snippet):
                df = TimeCardParser(path).parse()
                if df is not None and len(df) > 0:
                    timecard_dfs.append(df)
            elif is_payroll(fname, text_snippet):
                df = PayrollParser(path).parse()
                if df is not None and len(df) > 0:
                    payroll_dfs.append(df)
            else:
             
                df1 = TimeCardParser(path).parse()
                df2 = PayrollParser(path).parse()
                if df1 is not None and len(df1)>0:
                    timecard_dfs.append(df1)
                if df2 is not None and len(df2)>0:
                    payroll_dfs.append(df2)
        except Exception as e:
            print(f'  [ERRO] falha ao parsear {fname}: {e}')
            continue


    import pandas as pd
    tc_all = pd.concat(timecard_dfs, ignore_index=True) if timecard_dfs else pd.DataFrame()
    ph_all = pd.concat(payroll_dfs, ignore_index=True) if payroll_dfs else pd.DataFrame()

    ExcelWriter().write_to_excel(tc_all, ph_all, args.output)
    print(f'Concluído. Arquivo gerado: {args.output}')

if __name__ == '__main__':
    main()
