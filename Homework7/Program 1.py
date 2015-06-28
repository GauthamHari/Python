__author__ = 'GAUTHAM HARI'

import psutil
from wsgiref.simple_server import make_server

def System_info(environ, start_response):
    message = ""
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)
    disk_part = psutil.disk_partitions(all)
    no_of_cpu_core = psutil.cpu_count()
    memory = psutil.virtual_memory()
    user_name = psutil.users()
    message += "<center>"
    message += "<h3 font color = 'red'>" + "Hi, " + user_name[0][0] + "</h3>"
    message += "<p> <em> Some Status of your System are </em> </p>"
    message += "<p font color = 'blue'> Number of CPU cores = " + str(no_of_cpu_core) + "<p>"
    message += "<table width = '75%' border=0>"
    message += "<th bgcolor='#6BC9FF'> System Memory </th>"
    message += "<tr bgcolor ='#FBFF6B'>"
    message += "<td bgcolor='#D8DF1C'> Total Memory </td> <td>" + str(memory.total) + "</td>"
    message += "<td bgcolor='#D8DF1C'> Available Memory </td> <td>" + str(memory.available)+ "</td>"
    message += "<td bgcolor='#D8DF1C'> Used Memory </td> <td>" + str(memory.used) + "</td>"
    message += "<td bgcolor='#D8DF1C'> Percent Used </td> <td>" + str(memory.percent)+ "%</td> </tr>"
    message += "</table>"
    message += "</center>"

    i=0
    for count in disk_part :
        drive_name = disk_part[i][1]
        usage = psutil.disk_usage(drive_name)
        message += "<center>"
        message += "<table width = '75%' border=0>"
        message += "<th bgcolor='#6BC9FF'> Disk Usage </th>"
        message += "<tr bgcolor ='#FFD59E'>"
        message += "<td bgcolor='#FFA937'> Drive Name </td> <td>" + count.device + "</td>"
        message += "<td bgcolor='#FFA937'> File System Type </td> <td>" + count.fstype + "</td>"
        message += "<td bgcolor='#FFA937'> Total Memory </td> <td>" + str(usage.total) + "</td>"
        message += "<td bgcolor='#FFA937'> Available Memory </td> <td>" + str(usage.free) + "</td>"
        message += "<td bgcolor='#FFA937'> Used Memory </td> <td>" + str(usage.used) + "</td>"
        message += "<td bgcolor='#FFA937'> Percent Used </td> <td>" + str(usage.percent) + "%</td> </tr>"
        message += "</table>"
        message += "</center>"
        i += 1

    return[bytes(message,'utf-8')]

httpd = make_server('', 8000, System_info)
print("Serving on port 8000...")
httpd.serve_forever()