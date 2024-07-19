import pandas as pd

      def extract_data(file_path):
          df = pd.read_excel(file_path)
          data = df.to_dict(orient='records')
          return data

      # Example usage
      file_path = 'assignment data.xlsx'
      data = extract_data(file_path)
      print(data)