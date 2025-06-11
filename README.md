# Dữ Liệu Về Quan hệ Nhân Quả Giữa Hợp Kim Đồng Với Hiệu Suất Dẫn Điện
       
**Giới Thiệu**                          
*Mục tiêu*: nghiên cứu tác động của luật nhân quả, khi thay đổi các chất trong Hợp Kim Đồng, sẽ dẫn đến thay đổi của Hiệu Suất Dẫn Điện như thế nào.                  
*Nguồn dữ liệu:* [springernature]( https://springernature.figshare.com/articles/dataset/Dataset_of_mechanical_properties_and_electrical_conductivity_of_copper-based_alloys/23735373?file=41670945)             
           
**Cấu Trúc Bộ Dữ Liệu**         
Dữ liệu được tổ chức dưới dạng các dòng, mỗi dòng đại diện cho một hợp kim cụ thể. Các giá trị được phân cách bởi dấu chấm phẩy (;). Các cột chính bao gồm:             

*Tên hợp kim:* Ví dụ, Cu-2.8Ni-0.7Si-0.17V, Cu-1.7Be, .v.v....                    
*Loại hợp kim:* Ví dụ, Cu-Ni-Si alloys, Cu-Be alloys, .v.v....       
*Thành phần hóa học:* Phần trăm khối lượng của các nguyên tố (Cu, Ni, Si, Be, Ti, Mg, v.v.).      
*Điều kiện xử lý:* Nhiệt độ (K), thời gian (giờ), và các thông số liên quan.        
*Hiệu suất dẫn điện:* Đo bằng %IACS (International Annealed Copper Standard).                 

![image](https://github.com/user-attachments/assets/39031b30-d82e-471f-aa13-a6c2208c8c4a)



Ví dụ: Cu-2.8Ni-0.7Si-0.17V;Cu-Ni-Si alloys;96.33;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;2.8;0;0;0;0.7;0;0;0.17;0;0;1223;2;75;Y;723;20;Y;167;;;37;`https://doi.org/10.1007/s12540-013-4002-x`
             
Giải thích: Hợp kim chứa 96.33% Cu, 2.8% Ni, 0.7% Si, 0.17% V; xử lý ở 1223K trong 2 giờ; hiệu suất dẫn điện đạt 37% IACS, còn link là để giải là để giải thích cách họat động của dữ liệu (khi data cleaning thì em sẽ bỏ nó sau)    
         

**Mục Đích và Ứng Dụng**        
Bộ dữ liệu này được thiết kế để nghiên cứu mối quan hệ nhân quả giữa các yếu tố đầu vào (thành phần hóa học, điều kiện xử lý) và đầu ra (hiệu suất dẫn điện). Không giống như phân tích tương quan đơn thuần, suy luận nhân quả giúp trả lời câu hỏi: "Liệu sự thay đổi trong %Ni hoặc nhiệt độ xử lý có thực sự gây ra sự thay đổi trong hiệu suất dẫn điện không?"

**Cách Sử Dụng Bộ Dữ Liệu Với DML**      
Dưới đây là các bước cơ bản để áp dụng DML:       
     
*Xác định biến:*      
Biến điều trị: Một thành phần hóa học, ví dụ %Ni.     
Biến kết quả: Hiệu suất dẫn điện (%IACS).     
Biến kiểm soát: Các thành phần khác, nhiệt độ, thời gian xử lý.     
    

*Chuẩn bị dữ liệu:*     
Chuyển đổi dữ liệu thành định dạng bảng (DataFrame) với các cột rõ ràng.       
Chạy DML: Sử dụng thư viện như econml trong Python để ước lượng tác động nhân quả.      

*Ví Dụ*     
Để nghiên cứu tác động của %Ni:     
     
Biến điều trị: %Ni.    
Biến kết quả: %IACS.     
Biến kiểm soát: %Si, %Cu, nhiệt độ, thời gian.Kết quả DML sẽ cho biết mức độ ảnh hưởng của %Ni lên hiệu suất dẫn điện sau khi loại bỏ tác động của các yếu tố khác.    

