#!/bin/bash
current_date_time="`date "+%d-%m-%Y %H:%M:%S"`";
cd /Users/mangoking/Desktop/html
cp -r cuoikhoa "Backup of Cuoikhoa $current_date_time" 
echo "Finish backup ($current_date_time)"