// Smooth scroll for navigation links
// Find all links inside the navigation menu
document.querySelectorAll("nav a").forEach((anchor) => {
    // For each link, add a click event listener
    anchor.addEventListener("click", function (e) {
        // Prevent the default action of jumping to the section immediately
        e.preventDefault();

        // Find the section this link is pointing to (using the href attribute)
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            // Scroll to the section smoothly
            behavior: "smooth",
        });
    });
});

// Add intersection observer for animations on scroll
// Set up options for the observer
const options = {
    // Use the viewport as the area to watch
    root: null,
    // No extra space around the viewport
    rootMargin: "0px",
    // Trigger the callback when 10% of the element is visible
    threshold: 0.1,
};

// Define what to do when elements are in view
const callback = (entries, observer) => {
    // Check each entry that the observer is watching
    entries.forEach((entry) => {
        // If the element is in view
        if (entry.isIntersecting) {
            // Add the 'fade-in' class to the element to start the animation
            entry.target.classList.add("fade-in");
            // Stop watching this element since it has already animated
            observer.unobserve(entry.target);
        }
    });
};

// Create a new observer with the callback and options
const observer = new IntersectionObserver(callback, options);

document
    .querySelectorAll(
        ".course-card, .question-card, .about-card, .review, .hero-text"
    )
    .forEach((element) => {
        observer.observe(element);
    });

// Adding hover effect for buttons

const buttons = document.querySelectorAll(".btn");

buttons.forEach((button) => {
    // When the mouse enters the button
    button.addEventListener("mouseenter", () => {
        // Make the button slightly bigger
        button.style.transform = "scale(1.1)";
        // Add a smooth effect to the size change
        button.style.transition = "transform 0.3s ease-in-out";
    });
    // When the mouse leaves the button
    button.addEventListener("mouseleave", () => {
        // Make the button return to its normal size
        button.style.transform = "scale(1)";
    });
});
