import pdfplumber
import pandas as pd
import re

class TimeCardParser:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def parse(self):
        rows = []
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                for page in pdf.pages:
               
                    tables = page.extract_tables()
                    if tables:
                        for table in tables:
                           
                            if len(table) < 2:
                                continue
                            headers = [ (c or '').strip() for c in table[0] ]
                            for r in table[1:]:
                             
                                if len(r) < len(headers):
                                    r = r + [''] * (len(headers)-len(r))
                                rows.append({ headers[i] if headers[i] else f'col_{i}': (r[i] or '').strip() for i in range(len(headers)) })
                    else:
                        text = page.extract_text() or ''
                      
                        for line in text.splitlines():
                            if re.search(r"\d{2}\s+\w{3,}\s+\d{2}:\d{2}", line):
                                rows.append({'line': line.strip()})
        except Exception as e:
            print(f'  [time_card_parser] erro abrindo PDF: {e}')
        return pd.DataFrame(rows)
