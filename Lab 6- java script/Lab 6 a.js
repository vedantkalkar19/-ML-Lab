// Alert Pop-up Box
alert("This is an alert box!");

// Confirm Pop-up Box
var userConfirmation = confirm("Do you want to continue?");
if (userConfirmation) {
  alert("You clicked OK!");
} else {
  alert("You clicked Cancel!");
}

// Prompt Pop-up Box
var userInput = prompt("Please enter your name:", "John Doe");
if (userInput !== null) {
  alert("Hello, " + userInput + "!");
} else {
  alert("You canceled the prompt.");
}
