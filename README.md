Thông tin, báo cáo về sinh đôi tại Hoa Kỳ năm 1989-1991.      
Dữ liệu thô được lấy từ đây:        
http://www.nber.org/data/linked-birth-infant-death-data-vital-statistics-data.html      

Cụ thể là các tệp này:      
http://www.nber.org/lbid/1989/linkco1989us_den.csv.zip     
http://www.nber.org/lbid/1990/linkco1990us_den.csv.zip     
http://www.nber.org/lbid/1991/linkco1991us_den.csv.zip     

Hướng dẫn về tập dữ liệu có tại đây:       
http://www.nber.org/lbid/docs/LinkCO89Guide.pdf       

Ý tưởng về tập dữ liệu dựa trên bài báo:       
Almond, Douglas, Kenneth Y. Chay và David S. Lee. "Chi phí cho trẻ sinh nhẹ cân."       

Tạp chí Kinh tế Quý 120.3 (2005): 1031-1083.       

*twin_pairs_X_3years_samesex.csv* bao gồm 50 biến phụ thuộc cho cặp song sinh như tuổi của mẹ     
và cha, trình độ học vấn, các biến chứng về sức khỏe, v.v. Các đặc điểm
khác nhau giữa các cặp như giới tính và thứ tự sinh được biểu thị bằng _0 và _1 cho
cặp song sinh nhẹ cân và nặng cân hơn.       

*twin_pairs_T_3years_samesex.csv* bao gồm cân nặng khi sinh tính bằng gam của cả hai cặp song sinh trong
cặp, dbirt_0 và dbirt_1. Cặp nhẹ cân nhất luôn đứng đầu. Tôi đã loại bỏ tất cả các cặp có
cùng cân nặng.       

*twin_pairs_Y_3years_samesex.csv* bao gồm kết quả tử vong cho cả hai cặp song sinh, mort_0
và mort_1.        

*covar_types.txt* chỉ ra cho mỗi cột trong twin_pairs_X.csv liệu đó là nhị phân
(ví dụ: mẹ đã kết hôn), thứ tự (ví dụ: tuổi mẹ), phân loại (ví dụ: tiểu bang sinh) hay tuần hoàn
(chỉ một: tháng sinh).       
