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



**Dữ liệu mới sau khi phân loại dữ liệu (file cleaned_data)**
+ Alloy_Name: Tên hợp kim (ví dụ Cu–Al–Ni, Cu–Zn–Sn…)             

+ Alloy_Type: Phân loại hợp kim (ví dụ “brass” – thau, “bronze” – đồng thau, “pure” – đồng nguyên chất…)           

+ *Cu, Al, Ag, B, Be, Ca, Co, Ce, Cr, Fe, Hf, La, Mg, Mn, Mo, Nb, Nd, Ni, P, Pb, Pr, Si, Sn, Ti, V, Zn, Z*r: Phần trăm khối lượng (% wt) các nguyên tố trong hợp kim.          

+ *Solid_Solution_Temp_K*: Nhiệt độ xử lý hòa tan (solid solution treatment) tính theo Kelvin          

+ *Solid_Solution_Time_h*: Thời gian giữ ở nhiệt độ hòa tan (tính bằng giờ)          

+ *Cold_Rolling_Reduction*: Tỉ lệ giảm độ dày trong quá trình cán nguội (cold rolling reduction), thường tính bằng phần trăm     

+ *Secondary_Treatment_YN*: Cho biết có thực hiện xử lý nhiệt phụ (secondary heat treatment) sau cán nguội hay không (Y/N)       

+ *Aging_Temp_K*: Nhiệt độ lão hóa (aging) tính theo Kelvin          

+ *Aging_Time_h*: Thời gian lão hóa tính bằng giờ         

+ *Secondary_Mech_YN*: Cho biết có thực hiện gia công cơ khí phụ (secondary mechanical working) sau lão hóa hay không (Y/N)         

+ *Hardness_HV*: Độ cứng theo thang Vickers (HV)        

+ *Yield_Strength_MPa*: Giới hạn chảy (yield strength) tính bằng megapascals (MPa)             

+ *Ultimate_Tensile_Strength_MPa*: Độ bền kéo tối đa (ultimate tensile strength) tính bằng MPa             

+ *Electrical_Conductivity_IACS*: Độ dẫn điện so với chuẩn IACS (International Annealed Copper Standard), tính bằng phần trăm            

+ *DOI*: Mã DOI (Digital Object Identifier) của bài báo hoặc nguồn dữ liệu gốc (hiện vẫn được để lại để hiểu dữ liệu, ngay khi chạy để phân tích em sẽ xóa bỏ)
                 

  **Vấn đề dữ liệu thưa**              
  ![vấn đề](https://github.com/user-attachments/assets/92d190ab-96e6-4971-ad33-dde93e0fd517)         

  *Số lượng bị thiếu*
  + Solid_Solution_Temp_K: 48
  + Cold_Rolling_Reduction: 63             
  + Secondary_Treatment_YN: 0          
  + Aging_Temp_K: 91     
  + Aging_Time_h: 91
  + Secondary_Mech_YN: 18
  + Hardness_HV: 216
  + Yield_Strength_MPa: 1658
  + Ultimate_Tensile_Strength_MPa: 1555
  + Electrical_Conductivity_IACS: 5
            
             
   **Hoàn thiện datacleaning - filtered_data.csv**                   
  *Giảm bớt số lượng biến điều kiện*: tiêu chí dựa trên số lượng dữ liệu thiếu và xác suất ảnh hưởng đến dữ liệu           
  *Các điều kiện giữ lại*:
  + Aging_Temp_K: Nhiệt độ thay đổi, ảnh hưởng đến sự hình thành kết tủa, làm thay đổi độ dẫn điện.          
  + Aging_Time_h: Thời gian thay đổi, quyết định mức độ kết tủa, tác động đến độ dẫn điện.        
  + Solid_Solution_Temp_K: Nhiệt độ hòa tan ban đầu, ảnh hưởng đến trạng thái trước thay đổi, tác động đến độ dẫn điện.
             
  *Loại bỏ các dữ liệu bị thiếu*: 141         
  *Số dữ liệu còn lại*: 1690
                 
                  
  **Box Plot cho các điều kiện và kết quả**

  *solid_solution_temp*           
  ![solid_solution_temp_boxplot](https://github.com/user-attachments/assets/b984befd-6c9f-47e4-a622-1031c55393b9)

  *aging_temp*            
  ![aging_temp_boxplot](https://github.com/user-attachments/assets/60bd5ad4-afd6-4258-8b12-6da9ed327b72)

  *aging_time*
  ![aging_time_boxplot](https://github.com/user-attachments/assets/6c9d0a96-c71c-40a2-bf1a-dbd3f7210880)

  *conductivity*
  ![conductivity_boxplot](https://github.com/user-attachments/assets/d8f60acf-bcb5-483c-b7aa-79827a5eecdd)

   **HeatMap**

    *HeatMap các chất*                            
  ![chemical_heatmap](https://github.com/user-attachments/assets/32947fd7-94f4-4da8-8ec0-195206d151ce)

  *HeatMap kết hợp với ma trận tương quan*
  ![correlation_heatmap_corrected](https://github.com/user-attachments/assets/529f2db6-0f45-47c4-aa14-528a85ca3cf9)          
            
                 




  


