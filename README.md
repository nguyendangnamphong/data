**Nguồn**          
Từ: báo cáo về sinh đôi tại Hoa Kỳ năm 1989-1991.      
Dữ liệu thô được lấy từ: [link](http://www.nber.org/data/linked-birth-infant-death-data-vital-statistics-data.html)         
Cụ thể là các tệp:      
http://www.nber.org/lbid/1989/linkco1989us_den.csv.zip     
http://www.nber.org/lbid/1990/linkco1990us_den.csv.zip     
http://www.nber.org/lbid/1991/linkco1991us_den.csv.zip     
Hướng dẫn về tập dữ liệu: [link](http://www.nber.org/lbid/docs/LinkCO89Guide.pdf)                         

 **Nội dung dữ liệu**          
* *A1_progressOfBorn.csv*: chứa thông tin về 71 344 cặp sinh đôi trong vòng 3 năm          
- Dữ liệu ban đầu bao gồm, 50 biến liên quan đến cha mẹ của cặp cặp song sinh như: tuổi của mẹ và cha, trình độ học vấn, các biến chứng về sức khỏe, v.v.. 
![x_old](https://github.com/user-attachments/assets/b0305c1a-37a9-4d9a-a21e-c77980c29284)                

-  Do thấy có vẻ không cần thiết, em đã xóa bớt đi, chỉ để lại 8 thuộc tính:
   + adequacy: Mức độ đầy đủ của chăm sóc trước sinh
   + birattnd: Người hỗ trợ y tế khi sinh
   + bord_0: Thứ tự sinh của trẻ nhẹ cân hơn trong cặp song sinh
   + bord_1: Thứ tự sinh của trẻ nặng cân hơn trong cặp song sinh
   + cigar6: Số lượng thuốc lá hút mỗi ngày, phân vị
   + drink5: Số lượng uống đồ có cồn mỗi tuần, phân vị
   + mpre5: Thời điểm bắt đầu chăm sóc trước sinh, tam cá nguyệt (4 là không có)
   + nprevistq: Số lần khám thai, phân vị               
 ![x_new](https://github.com/user-attachments/assets/031f9b63-887c-4382-af9f-833f0a1700bc)           
            



* *A2_weighOfBorn.csv*: chứa thông cân nặng khi sinh tính bằng gam của cả hai cặp song sinh trong
cặp, dbirt_0 và dbirt_1. Cặp nhẹ cân nhất luôn đứng đầu. Đã loại bỏ tất cả các cặp có
cùng cân nặng.        
![t](https://github.com/user-attachments/assets/586f0e76-43c9-4c4b-b9d1-df455b994418)                


* *B_survice.csv* bao gồm kết quả tử vong cho cả hai cặp song sinh, mort_0
và mort_1.           
![y](https://github.com/user-attachments/assets/3013d7b1-ef25-48be-b53f-0a4bf6323ddf)               


* *covar_types.txt* để chỉ ra cho mỗi cột trong twin_pairs_X.csv liệu đó là nhị phân
(ví dụ: mẹ đã kết hôn), thứ tự (ví dụ: tuổi mẹ), phân loại (ví dụ: tiểu bang sinh) hay tuần hoàn
(chỉ một: tháng sinh).         
![covar_types](https://github.com/user-attachments/assets/191e6ede-81c9-4d1e-98db-3b19dae9eaac)                
* *covar_desc.txt* để chỉ ra mỗi cột là chứa thông tin gì         
![convar_desc](https://github.com/user-attachments/assets/7e175d97-9723-4be3-8c5c-6798beeb30cc)


**Bên lề**          
*Bài báo từng sử dụng dữ liệu:* [Causal Effect Variational Autoencoder](https://arxiv.org/pdf/1705.08821)             
*Dữ liệu sử dụng:* Dữ liệu gốc của quân đội Hoa Kì (Bản 50 biến)        
*Mục tiêu sử dụng:* Tìm hiểu yếu tố ẩn trong quan hệ nhân quả        
*Mô hình sử dụng:* CEVAE (Deep learning)



