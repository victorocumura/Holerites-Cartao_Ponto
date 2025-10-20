import pandas as pd
import os

class ExcelWriter:
    def write_to_excel(self, time_card_df, payroll_df, output_path):
      
        out_dir = os.path.dirname(output_path) or '.'
        if not os.path.exists(out_dir):
            os.makedirs(out_dir, exist_ok=True)
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            if time_card_df is None or time_card_df.empty:
                pd.DataFrame({'info': ['no timecard data extracted']}).to_excel(writer, sheet_name='Cartao_Ponto', index=False)
            else:
                time_card_df.to_excel(writer, sheet_name='Cartao_Ponto', index=False)
            if payroll_df is None or payroll_df.empty:
                pd.DataFrame({'info': ['no payroll data extracted']}).to_excel(writer, sheet_name='Holerite', index=False)
            else:
                payroll_df.to_excel(writer, sheet_name='Holerite', index=False)
