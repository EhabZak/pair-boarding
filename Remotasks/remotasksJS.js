

// function fastClickDetector(buttonElement) {
//   let clickCount = 0;
//   let lastClickTime = null;

//   const handleClick = () => {
//       const currentTime = Date.now();

//       // Check if current click is within 1 second of the last click
//       if (lastClickTime && currentTime - lastClickTime <= 1000) {
//           clickCount++;
//       } else {
//           // Reset click count if it's more than 1 second since the last click
//           clickCount = 1;
//       }

//       lastClickTime = currentTime;

//       // Check if there are three clicks within 1 second
//       if (clickCount === 3) {
//           alert("Fast clicking detected!");
//           clickCount = 0; // Reset click count
//       }
//   };

//   buttonElement.addEventListener("click", handleClick);
// }

// document.addEventListener('DOMContentLoaded', () => {
//   const button = document.getElementById("myButton");
//   fastClickDetector(button);
// });

