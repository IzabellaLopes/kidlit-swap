# KidLit Swap

![Home Page](documentation/home-page.png)


[KidLit Swap Live Page](https://kidlit-swap-96ca222a1195.herokuapp.com/)


## CONTENTS

- [KidLit Swap](#kidlit-swap)
  - [CONTENTS](#contents)
  - [User Story Testing](#user-story-testing)
    - [EPIC: Book Management System](#epic-book-management-system)
    - [EPIC: User Authentication](#epic-user-authentication)
  - [Site Administration](#site-administration)

---

## User Story Testing

### [EPIC: Book Management System](https://github.com/IzabellaLopes/kidlit-swap/milestone/4)
*As a User / Admin I can add a new book to the system so that I can easily expand the library's collection*
  - There are various ways for users/admins to add new books on KidLit Swap.
  - The first method is on the homepage, when the user is logged in, where clicking the "Add Book" button redirects the user/admin to the "Add Book" page. 
  ![Hero_auth](documentation/readme_images/features/hero_auth.png)
  - Another method is accessing the "Book List," available for both logged-in and non-logged-in users. At the bottom of the page, there is another "Add Book" button that also redirects to the "Add Book" page.
  ![Book List](documentation/readme_images/features/book_list.png)
  - All tests were conducted on the "Add Book" page, covering mandatory fields (title, author, description) and optional fields (image and category).
  ![Add book](documentation/readme_images/features/add_book.png)

*As a User / Admin I can view a list of all books in the system so that I can easily manage and monitor the library's inventory*
- All tests conducted for this user story on KidLit Swap were successfully completed. 
- The books are displayed in alphabetical order, with available books appearing first, followed by borrowed books.
 ![Book List - page 1](testing/testing_images/books_1.png)
 ![Book List - page 3](testing/testing_images/books_2.png)
- This ensures a well-organized and user-friendly presentation of the library inventory for efficient management.

*As a User / Admin I can view details of a specific book so that I can get comprehensive information about a particular book*
- All tests for this user story were successfully completed on KidLit Swap. The Book Details page effectively displays comprehensive information about each book, including title, author, description, category, status, and the owner of the book (added by).
- Additionally, all tests were conducted successfully to ensure the correct display of these features:
    - Owner Message: Displays gratitude for sharing the book if the logged-in user is the owner, and the status is Available.
  ![Book Details - Owner](documentation/readme_images/features/detail_owner.png)

    - Borrow Button: Appears for users who are not the owner, with a "Borrow This Book" button when the status is Available.
  ![Book Details - User](documentation/readme_images/features/detail_user.png)

    - Borrow Confirmation Modal: Allows users to confirm borrowing details, including selecting a return date, updating the book's status from Available to Borrowed.
  ![Modal - Return date](documentation/readme_images/features/return_date.png)

    - Borrowed Message: The page includes a message for users who have borrowed the book, indicating the borrower's username and the expected return date.
  ![Book Details - Borrowed](documentation/readme_images/features/detail_borrowed.png)

- Finally, the "Back to Book List" button was tested and successfully redirects the user / admin to the Book List page.

*As a User / Admin I can edit the details of an existing book so that I can keep the information accurate and up-to-date*

- All tests were successfully conducted on KidLit Swap. The "Edit Book" page is opened when the book's owner clicks on "Edit" in Manage Books -> My Books -> Edit. 
- On the "Edit Book" page, the owner can modify details such as Title, Author, Description, Image, and Category. All functionalities were tested and approved.
  ![Edit book](documentation/readme_images/features/edit_book.png)

*As a User / Admin I can mark a book as "Borrowed" and set a return date so that I can facilitate and track book borrowings*
- As previously demonstrated, a logged-in user, who is not the owner of the book, can request to borrow a book with an "Available" status by clicking the "Borrow" button. 
  ![Book Details - User](documentation/readme_images/features/detail_user.png)
- All functionalities were thoroughly tested to ensure the following conditions: owners cannot request to borrow their own books, and non-logged-in users cannot request book borrowings.
- The "Borrow Confirmation Modal" was rigorously tested to allow only future dates, preventing the selection of retrospective dates.
  ![Modal - Return date](documentation/readme_images/features/return_date.png)

*As a User / Admin I can mark a borrowed book as "Returned" so that I can update the library's inventory and track book returns*

- Return Book Button: At the bottom of each borrowed book card, a "Return Book" button with its respective Font Awesome icon is present.
  ![Borrowed books](documentation/readme_images/features/borrowed_books.png)
- Return Confirmation: Clicking the "Return Book" button triggers a success message at the top of the page.
The success message states: "You have successfully returned the book 'TITLE OF THE BOOK.'"
  ![Success message - Borrowed books](documentation/readme_images/features/borrowed_books_msg.png)
- Testing was completed successfully, ensuring the seamless process of marking a returned book as "Available" on KidLit Swap.

### [EPIC: User Authentication](https://github.com/IzabellaLopes/kidlit-swap/milestone/5)
Django Allauth is installed and employed for implementing Sign Up, Log In, and Log Out functionalities.

*As a User I can log in so that I can access personalized features and participate in the KidLit Swap community*
- Access the Log In page.
- Enter valid credentials (username/email and password) and click the "Log In" button.
- Confirm successful login and redirection to the user's dashboard.
- Validate error messages for unsuccessful login attempts.
![Log in](documentation/readme_images/features/login.png)

*As a User I can log out so that I can secure my account and maintain privacy*
- Click the "Log Out" option.
- Ensure a success message appears, confirming the user's logout.
- Validate error messages for any issues during the logout process.
![Log out](documentation/readme_images/features/logout.png)

*As a User I can sign up so that I can become a member of the KidLit Swap community and share my love for children's literature*
- Navigate to the Sign Up page.
- Input valid registration details and click the "Sign Up" button.
- Verify successful registration and redirection to the user's dashboard.
![Sign up](documentation/readme_images/features/signup.png)

All testing was conducted using Django Allauth, ensuring seamless Sign Up, Log In, and Log Out functionalities. Success messages notify users of successful login and logout actions, while error messages provide feedback for unsuccessful attempts.

*As a User I can view and manage my added and borrowed books on my profile page so that I can easily track and organize my book-related activities*
- Welcome Section: 
  - Check that the user's username is correctly displayed in the welcome message.
- Books Added Section:
    - Verify that the message accurately reflects the number of books added by the user.
    - Confirm the functionality of the "View My Books" button.
- Books Borrowed Section:
  - Confirm that the message accurately reflects the number of books borrowed by the user.
    - Check the functionality of the "View Borrowed Books" button.
  ![Profile](documentation/readme_images/features/profile.png)

[Back to Contents](#contents)

---

## Site Administration

- Admins possess complete access to Create, Read, Update, and Delete (CRUD) functionalities for all books, categories, and users within the admin panel.

![Admin](testing/testing_images/admin.png)

[Back to Contents](#contents)

---

