from zipfile import ZipFile
import os

port_nginx = ""
port_PHP_CGI = ""

def port():
    global port_nginx
    global port_PHP_CGI
    port_nginx = input("numéro de port de votre serveur web (ex: 8080): ")
    port_PHP_CGI = input("numéro de port de votre PHP-CGI (ex: 9000): ")
    

def dezip():
  
    file = "serveur-nginx.zip"
    
    with ZipFile(file, 'r') as zip: 
        print('extraction...') 
        zip.extractall() 
        print('Terminé!')

def configiuration():
    global port_nginx
    global port_PHP_CGI
    
    fichier_nginx_conf = open("./conf/nginx.conf", "r+", encoding="utf-8")
    config = fichier_nginx_conf.read()
    fichier_nginx_conf.close()
    config = config.replace("NGINX_PORT", port_nginx)
    config = config.replace("PHP_CGI_PORT", port_PHP_CGI)
    
    fichier_nginx_conf = open("./conf/nginx.conf", "w+", encoding="utf-8")
    fichier_nginx_conf.write(config)
    fichier_nginx_conf.close()
    
    
    fichier_start_php_fcgi = open("./start-php-fcgi.bat", "r+", encoding="utf-8")
    config = fichier_start_php_fcgi.read()
    fichier_start_php_fcgi.close()
    config = config.replace("PHP_CGI_PORT", port_PHP_CGI)
    
    fichier_start_php_fcgi = open("./start-php-fcgi.bat", "w+", encoding="utf-8")
    fichier_start_php_fcgi.write(config)
    fichier_start_php_fcgi.close()
    

port()
dezip()
configiuration()