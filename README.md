# BookApiProject
BOOKSTORE PROJECT USING REST APIS

Admin - can register, login, authenticate and perform all CRUD operations including search operations.
Normal Users - can register, login, authenticate and view list of books, particular book details and perform search operations.

Using Class Based Views - API views
(CreateAPIView ,UpdateAPIView, ListAPIView, RetrieveAPIView,DeleteAPIView)

Authentication:Token Authentication,Basic Authentication,Session Authentication

Basic Authentication and Session Authentication:
Admin:
	Username: maria
Password :maria
User:
	Username:sikha
	Password :sikha12345

Token Authentication:
Get token :Request Method : POST
URL: http://127.0.0.1:8000/api/token/auth/ 
Key           : Value
Username: maria
Password :maria

	Response - status 200 ok

APIs - Requests and Responses

Request Method : GET (Search Fields - Author Name,Book Name)
Access : Users and Admin
Url - http://127.0.0.1:8000/booklist/  (Complete List of Books)
Url - http://127.0.0.1:8000/bookdetails/4 (Particular Book)
Response - status 200 ok

Request Method : POST
Access : Admin only
Url - http://127.0.0.1:8000/bookcreate/
Body - 
	{
    "bookname": "In Search of Lost Time",
    "author": "Marcel Proust",
    "pubyear":2020,
    "pages": 330,
    "abstract": "In Search of Lost Time follows the narrator’s recollections of childhood and experiences into adulthood during late 19th century to early 20th century aristocratic France, while reflecting on the loss of time and lack of meaning to the world."
}
Response - status 201 created


Request Method : PUT
Access : Admin only
Url - http://127.0.0.1:8000/bookupdate/4
Body - 
	{
    "bookname": "In Search of Lost Time by Marcel Proust",
    "author": "Marcel Proust 1",
    "pubyear":2019,
    "pages": 430,
    "abstract": "In Search of Lost Time follows the narrator’s recollections of childhood and experiences into adulthood during late 19th century to early 20th century aristocratic France, while reflecting on the loss of time and lack of meaning to the world."
}

Response - status 200 ok


Request Method : PATCH
Access : Admin only
Url - http://127.0.0.1:8000/bookupdate/4
Body - {
"pages": "630"
}

Response - status 200 ok




Request Method : DELETE
Access : Admin only
Url - http://127.0.0.1:8000/delete/4
Response - status 204 no content




Additional Features - Searching list of books with search filters applied in GET method above that searches availability of books using author name or book name.

