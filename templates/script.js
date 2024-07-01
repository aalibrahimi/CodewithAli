// Smooth scroll for navigation links
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add intersection observer for animations on scroll
const options = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const callback = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
            observer.unobserve(entry.target);
        }
    });
};

const observer = new IntersectionObserver(callback, options);

document.querySelectorAll('.course-card, .question-card, .review, .hero-text').forEach(element => {
    observer.observe(element);
});

// Adding hover effect for buttons
const buttons = document.querySelectorAll('.btn,');
buttons.forEach(button => {
    button.addEventListener('mouseenter', () => {
        button.style.transform = 'scale(1.1)';
        button.style.transition = 'transform 0.3s ease-in-out';
    });
    button.addEventListener('mouseleave', () => {
        button.style.transform = 'scale(1)';
    });
});