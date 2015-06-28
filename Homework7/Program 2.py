__author__ = 'GAUTHAM HARI'

from wsgiref.simple_server import make_server
import sqlite3

def get_form_vals(post_str):
	form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
	return form_vals

def hello_world_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)

    message = "<br> <h1> Welcome to the Zoo </h1>"  #HTML form design for entering data
    message += "<form method='POST'> <br> <table> <tr> <td> Animal: </td> <td> <input type=text name='animal'> </td> </tr>"
    message += "<tr> <td> Count: </td> <td> <input type=text name='count'> </td> </tr>"
    message += "<tr> <td> </td> <td> <input type='submit' name='Submit'> </td> </tr> </table> </form>"

    if(environ['REQUEST_METHOD'] == 'POST'):
        request_body_size = int(environ['CONTENT_LENGTH'])
        request_body = environ['wsgi.input'].read(request_body_size)
        form_vals = get_form_vals(request_body)

        try:
            conn = sqlite3.connect("zoo.sqlite")
            cursor = conn.cursor()
            data_val = (form_vals["animal"], int(form_vals["count"]))   #throws ValueError when user enters non-integer value for Count
            cursor.execute("create table IF NOT EXISTS animal_count(name text, count integer)") #Creating table if it doesn't exist
            cursor.execute("insert into animal_count(name,count) values (?,?)", data_val)   #Inserting the user's data in the table
        except ValueError:      #Handling predictable exceptions
            message += "<font color='red'> Please enter an integer value for 'Count' of animals </font>"
        except Exception as e:  #Handling unpredictable exceptions
            print(type(e))
            print(e.args)
            print(e)
        else:   #Displaying feedback to the user upon successful operation
            message += "<br> <font color='blue'> Your data has been recorded in the database table: </font>"
            message += "<br>You entered: Animal = " + str(form_vals["animal"]) + ", Count = " + str(form_vals["count"])
        finally:    #Displaying the table data to the user, and closing the database connection
            data = cursor.execute("select * from animal_count")
            message += "<br> <br> <b> This zoo contains the following animals: </b>"
            for row in data:
                message += "<br>" + str(row)
            conn.commit()
            conn.close()

    return[bytes(message,'utf-8')]

httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")
httpd.serve_forever()