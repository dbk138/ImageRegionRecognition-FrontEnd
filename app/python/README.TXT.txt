This is where we are keeping the python web service scripts.

To get python web services running you must:

-install python 2.7
-install python pip: http://www.pip-installer.org/en/latest/installing.html
  - put python in your system path
  - put python/scripts in your system path so that pip.exe is available on cmd line

-install bottle using pip: pip install bottle
-install latest apache 32 bit web server

-copy the mod_wsgi.so file in this folder to apache modules directory.
-add this line to your httpd.conf: LoadModule wsgi_module modules/mod_wsgi.so  (see line 131 in my httpd.conf)
- add this to the end of the httpd.conf , but change the paths you see below according to your folder layout


<VirtualHost *>
     #ServerName mypage.com
 
     #WSGIDaemonProcess todo user=www-data group=www-data processes=1 threads=5
     WSGIScriptAlias /services "C:\Users\jhala\angular-seed\app\python\adapter.wsgi"
     
 
     <Directory "C:\Users\jhala\angular-seed\app\python">
         #WSGIProcessGroup todo
         WSGIApplicationGroup %{GLOBAL}
         Order deny,allow
         Allow from all
     </Directory>
 </VirtualHost>
 
 
 <VirtualHost *:80>
 DocumentRoot "C:\Users\jhala\angular-seed"
 #ServerName www.example.org
 
     <Directory "C:\Users\jhala\angular-seed">
   Options Indexes FollowSymLinks

    #
    # AllowOverride controls what directives may be placed in .htaccess files.
    # It can be "All", "None", or any combination of the keywords:
    #   Options FileInfo AuthConfig Limit
    #
    AllowOverride None
 
    #
    # Controls who can get stuff from this server.
    #
    Order allow,deny
    Allow from all

     </Directory>
 
</VirtualHost>
 





