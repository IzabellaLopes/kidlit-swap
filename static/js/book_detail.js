// Function to handle the borrow action
function handleBorrowAction() {
  // Get the selected return date if the user is authenticated
  var returnDateInput = document.getElementById('returnDate');
  var selectedReturnDate = returnDateInput ? new Date(returnDateInput.value) : null;

  // Get the current date
  var currentDate = new Date();

  // Check if the selected return date is in the future
  if (selectedReturnDate && selectedReturnDate <= currentDate) {
    alert('Warning! The return date must be in the future.');
    return;
  }

  // Use the 'isAuthenticated' variable defined in the HTML template
  if (isAuthenticated) {
    // Redirect to the borrow_book page with the book's slug
    window.location.href = borrowBookURL;
  } else {
    // Prompt non-authenticated users to log in
    window.location.href = loginURL;
  }
}
