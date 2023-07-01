# CORS-Finder
## This tools is developed for identifying the vulnerable cors domain

![alt text](https://raw.githubusercontent.com/hariharan005/CORS/main/banner/Screenshot%20from%202023-07-01%2015-15-12.png)

### How to install CORS-Finder:
 git clone https://github.com/hariharan005/CORS.git     
 ls    
 cd CORS    
 python3 cors.py   
              

USAGE:                       
       For scanning:  cat <domain.txt> | xargs -n1 -P10 python3 corss.py                           
       For scanning with output:  cat <domain.txt> | xargs -n1 -P10 python3 corss.py | tee -a <output.txt>

NOTE:  
       In this tool i use sample domain file but you have to choose your own url file which you recon using some other recon tool.
