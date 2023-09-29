// 1. Concatenation
var str1 = "Hello";
var str2 = "World";
var combinedStr = str1 + " " + str2;
console.log(combinedStr); // Output: "Hello World"

// 2. Length of a String
var text = "JavaScript";
var length = text.length;
console.log("Length of the string: " + length); // Output: 10

// 3. Accessing Characters
var message = "Hello, World!";
var firstChar = message[0]; // Access the first character
console.log("First character: " + firstChar); // Output: "H"

// 4. Substring
var sentence = "This is a sample sentence.";
var substring = sentence.substring(5, 10); // Extracts characters from index 5 to 9
console.log("Substring: " + substring); // Output: "is a "

// 5. String to Uppercase and Lowercase
var mixedCase = "RaNdOm CaSe StRiNg";
var upperCase = mixedCase.toUpperCase();
var lowerCase = mixedCase.toLowerCase();
console.log("Uppercase: " + upperCase);
console.log("Lowercase: " + lowerCase);

// 6. Searching for a Substring
var searchStr = "apple";
var fruitList = "apple, banana, cherry, date";
var found = fruitList.includes(searchStr);
console.log("Substring found: " + found); // Output: true
