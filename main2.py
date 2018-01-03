from flask import Flask, request

from Caesar import rotate_string



app = Flask(__name__)

app.config['DEBUG'] = True



form = """

   <!DOCTYPE html>

   <html>

       <head>

           <style>

               form {{

                   background-color: #eee;

                   padding: 20px;

                   margin: 0 auto;

                   width: 540px;

                   font: 16px sans-serif;

                   border-radius: 10px;

               }}

               textarea {{

                   margin: 10px 0;

                   width: 540px;

                   height: 120px;

               }}

           </style>

       </head>

       <body>

           <form action="/" method='post'>

               <label for="rot">Rotate By:</label>

               <input value="0" id="rot" type="text" name="rot">

               <textarea name="new_text">{0}</textarea>

               <input type="submit">



           </form>

       </body>

   </html>



"""





@app.route("/", methods=['POST', 'GET'])

def encrypt():

    if request.method == 'POST':

           text=request.form['text']

           rot=int(request.form['rot'])

           new_text=rotate_string(text, rot)



           return form.format(new_text)

    return form.format("")

app.run()