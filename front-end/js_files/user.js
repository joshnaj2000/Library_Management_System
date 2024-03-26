
const addUser = document.getElementById("adduser");

addUser.addEventListener("click", function() {
  window.location.href = "/C:/Users/joshna.j/Desktop/Library_Management_System/front-end/html_files/add_user.html"
  console.log("Button clicked")
});

const addBook = document.getElementById("addbook");

addBook.addEventListener("click", function(){
    window.location.href = "/C:/Users/joshna.j/Desktop/Library_Management_System/front-end/html_files/add_book.html"
    console.log("Button Clickred")
});

const borrow = document.getElementById("borrowbook");

borrow.addEventListener("click" , function(){
    window.location.href="/C:/Users/joshna.j/Desktop/Library_Management_System/front-end/html_files/borrow_book.html"
    console.log("Button clicked")
});

const returnbook = document.getElementById("returnbook");

returnbook.addEventListener("click" , function(){
    window.location.href="/C:/Users/joshna.j/Desktop/Library_Management_System/front-end/html_files/borrow_book.html"
    console.log("Button clicked")

});



$("adduser")