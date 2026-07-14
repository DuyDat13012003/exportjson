import pandas as pd

EXCEL_FILE = "DASHBOARD BESS AC COUPLING.xlsx"

df = pd.read_excel(
    EXCEL_FILE,
    sheet_name="Chart",
    header=2,
    engine="openpyxl"
)

df.to_json(
    "chart.json",
    orient="records",
    indent=4,
    force_ascii=False
)

print("Đã xuất chart.json")