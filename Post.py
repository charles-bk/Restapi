from flask import Flask ,jsonify,request

app = Flask(__name__)

books = [{

    "id":1 ,"tittle":"python","author":"Johnson"},
    {"id":2,"tittle":"JAVA","Author":"charles"},
    {"id":3,"tittle":"mysql","author":"robot"

}]

# get all books
@app.route('/school',methods = (["GET"]))
def get_book():
    return jsonify(books)


# get specific book
@app.route('/school/<int:id>',methods = (["GET"]))
def getid(id):
    book = next((book for book in books if book["id"] == id),None)
    if book:
        return jsonify(book)
    return jsonify({"error":"Book not found"}),404


# create a new book
@app.route('/school',methods = (["POST"]))
def create_book(): # if Book is  Add it show the error
    New_book = request.json
    if "id" not in New_book or "tittle"not in New_book or "author" not in New_book:
        return jsonify({"Error":"complite book informaction"}),400 
    books.append(New_book) # this programing its adds your book
    return jsonify({"message":New_book}),201


#update the exisiting book make you change
# first yoy will select [GET ] then Edit it finaly select [PUT ]and it show changes
@app.route('/school/<int:id>',methods=(["PUT"]))
def change(id):
    book = next((book for book in books if book["id"]==id),None)
    if book:
        change_book = request.json
        book.update(change_book)
        return jsonify({"Message":"Bookdetails will be changed","book":book})
    return jsonify({"Error":"Book is not found"})

# DELECT A BOOK 
@app.route('/school/<int:id>',methods = (["DELETE"]))
def delect_book(id):
    global books
    books = [book for book in books if book["id"] != id]
    return jsonify({"Message":"Book delected"})


if __name__=='__main__':
    app.run(debug=True)