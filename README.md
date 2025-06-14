# Thay đổi thành phần hợp kim có ảnh hưởng thế nào đến độ dẫn điện
       
**Giới Thiệu**                          
*Mục tiêu*: nghiên cứu tác động của luật nhân quả, khi thay đổi các chất trong Hợp Kim Đồng, sẽ dẫn đến thay đổi của Hiệu Suất Dẫn Điện như thế nào.     
*Số lượng*: 1830 bản ghi           
*Nguồn dữ liệu:* [springernature]( https://springernature.figshare.com/articles/dataset/Dataset_of_mechanical_properties_and_electrical_conductivity_of_copper-based_alloys/23735373?file=41670945)             
           
**Cấu Trúc Bộ Dữ Liệu**         
Dữ liệu được tổ chức dưới dạng các dòng, mỗi dòng đại diện cho một hợp kim cụ thể. Các giá trị được phân cách bởi dấu chấm phẩy (;). Các cột chính bao gồm:             

*Tên hợp kim:* Ví dụ, Cu-2.8Ni-0.7Si-0.17V, Cu-1.7Be, .v.v....                    
*Loại hợp kim:* Ví dụ, Cu-Ni-Si alloys, Cu-Be alloys, .v.v....       
*Thành phần hóa học:* Phần trăm khối lượng của các nguyên tố (Cu, Be, Ag, Ti, Zr, Mg, Zn, P, Cr, Al, Si, Fe, Sn, Pb, Ni, Mn, Co, Sb, Cd, Bi, Se, W, Mo, Nb).      
*Điều kiện xử lý:* Nhiệt độ (K), thời gian (giờ), và các thông số liên quan.        
*Hiệu suất dẫn điện:* Đo bằng %IACS (International Annealed Copper Standard).                 

![image](https://github.com/user-attachments/assets/39031b30-d82e-471f-aa13-a6c2208c8c4a)

       
             

*Ví dụ*: Cu-2.8Ni-0.7Si-0.17V;Cu-Ni-Si alloys;96.33;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;2.8;0;0;0;0.7;0;0;0.17;0;0;1223;2;75;Y;723;20;Y;167;;;37;`https://doi.org/10.1007/s12540-013-4002-x`
             
*Giải thích*: Hợp kim chứa 96.33% Cu, 2.8% Ni, 0.7% Si, 0.17% V; xử lý ở 1223K trong 2 giờ; hiệu suất dẫn điện đạt 37% IACS,   còn *link* là tác giả gắn vào để giải thích cách họat động của dữ liệu (khi data cleaning thì em sẽ bỏ nó sau)        
       
*Phụ chú*: Dấu "-" không phải là âm mà là dấu ngăn cách     
         
**Biểu đồ Boxplot**         
*Thành phần hóa học của các hợp kim*       
![Thành phần hóa học của các hợp kim](https://github.com/user-attachments/assets/cace2d9d-28d2-432e-b9ec-706d61382624)            

 *Nhiệt độ và thời gian xử lý nhiệt (dung dịch rắn, lão hóa) cùng tỷ lệ cán nguội*          
![Nhiệt độ và thời gian xử lý nhiệt (dung dịch rắn, lão hóa) cùng tỷ lệ cán nguội](https://github.com/user-attachments/assets/dada7389-88ce-4059-92f5-4f1235f76c3a)           
                      
*Các tính chất vật lý*
![Các tính chất vật lý](https://github.com/user-attachments/assets/e3c9f216-4290-4001-8e62-adee967e266c)

                    
**Mục Đích và Ứng Dụng**        
Bộ dữ liệu này được thiết kế để nghiên cứu mối quan hệ nhân quả giữa các yếu tố đầu vào (thành phần hóa học, điều kiện xử lý) và đầu ra (hiệu suất dẫn điện). Không giống như phân tích tương quan đơn thuần, suy luận nhân quả giúp trả lời câu hỏi: "Liệu sự thay đổi trong %Ni hoặc nhiệt độ xử lý có thực sự gây ra sự thay đổi trong hiệu suất dẫn điện không?"
          
*Biểu đồ không gian tính chất*                
![Biểu đồ không gian tính chất](https://github.com/user-attachments/assets/c6a4006a-258f-4c0b-839a-3407dcc37d26)

        
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
Biến kiểm soát: %Si, %Cu, nhiệt độ, thời gian.               
Kết quả DML sẽ cho biết mức độ ảnh hưởng của %Ni lên hiệu suất dẫn điện sau khi loại bỏ tác động của các yếu tố khác.    

