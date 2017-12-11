
rem Compile style
call lessc .\themes\w3css-blog\static\less\style.less .\themes\w3css-blog\static\css\style.css

call pelican content

pause