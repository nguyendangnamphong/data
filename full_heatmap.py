import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đường dẫn đến file dữ liệu
file_path = 'D:/data/filtered_data.csv'

# Đọc dữ liệu từ file CSV
df = pd.read_csv(file_path)

# In danh sách cột để kiểm tra
print("Danh sách cột trong filtered_data.csv:", df.columns.tolist())

# Danh sách cột hóa học
chemical_columns = [
    'Cu', 'Al', 'Ag', 'B', 'Be', 'Ca', 'Co', 'Ce', 'Cr', 'Fe', 'Hf', 'La', 'Mg', 
    'Mn', 'Mo', 'Nb', 'Nd', 'Ni', 'P', 'Pb', 'Pr', 'Si', 'Sn', 'Ti', 'V', 'Zn', 'Zr'
]

# Các cột điều kiện và độ dẫn điện
condition_columns = ['Solid_Solution_Temp_K', 'Aging_Temp_K', 'Aging_Time_h']
conductivity_column = 'Electrical_Conductivity_IACS'

# Kết hợp tất cả các cột
all_columns = chemical_columns + condition_columns + [conductivity_column]

# Kiểm tra xem các cột có tồn tại không
missing_columns = [col for col in all_columns if col not in df.columns]
if missing_columns:
    print(f"Không tìm thấy các cột: {', '.join(missing_columns)}")
    exit()

# Chọn dữ liệu chỉ với các cột liên quan
df_corr = df[all_columns]

# Kiểm tra kiểu dữ liệu
print("Kiểu dữ liệu của các cột:")
print(df_corr.dtypes)

# Đảm bảo tất cả các cột đều chứa dữ liệu số
for col in all_columns:
    if not pd.api.types.is_numeric_dtype(df_corr[col]):
        print(f"Cột {col} không phải số. Vui lòng kiểm tra dữ liệu.")
        exit()

# Kiểm tra các cột có std=0
for col in all_columns:
    if df_corr[col].std() == 0:
        print(f"Cột {col} có tất cả giá trị giống nhau (std=0).")

# Kiểm tra giá trị NaN
print("Số giá trị NaN trong các cột:")
print(df_corr.isna().sum())

# Tính ma trận tương quan
correlation_matrix = df_corr.corr()

# Thay thế NaN bằng 0
correlation_matrix = correlation_matrix.fillna(0)

# Đảm bảo đường chéo chính là 1
for i in range(correlation_matrix.shape[0]):
    correlation_matrix.iloc[i, i] = 1.0

# Vẽ heatmap
plt.figure(figsize=(18, 14))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1)

# Thêm tiêu đề và nhãn
plt.title('Heatmap Tương Quan giữa Các Chất, Điều Kiện và Độ Dẫn Điện', fontsize=16)


# Xoay nhãn trục x để dễ đọc
plt.xticks(rotation=45, ha='right')

# Lưu biểu đồ thành file PNG
plt.savefig('D:/data/correlation_heatmap_corrected.png')

# Hiển thị biểu đồ
plt.show()