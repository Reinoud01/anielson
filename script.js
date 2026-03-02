document.addEventListener('DOMContentLoaded', () => {
    const menuIcon = document.querySelector('.menu-icon');
    const navLinks = document.querySelector('.nav-links');

    if (menuIcon && navLinks) {
        menuIcon.addEventListener('click', () => {
            menuIcon.classList.toggle('active');
            navLinks.classList.toggle('active');
        });

        // Close menu when a link is clicked
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                menuIcon.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });
    }

    // Sticky Header Logic (optional if CSS strictly handles it, but adding class on scroll is nice for styling changes)
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 0) {
            navbar.classList.add('sticky');
        } else {
            navbar.classList.remove('sticky');
        }
    });
    // Debug Form Submissions
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', () => {
            console.log('Form submission triggered for:', form.className);
        });
    });

    // Before/After Slider Logic
    const sliders = document.querySelectorAll('.comparison-slider');
    sliders.forEach(slider => {
        const input = slider.querySelector('.slider-input');
        const imgAfter = slider.querySelector('.img-after');
        const handle = slider.querySelector('.slider-handle');

        input.addEventListener('input', (e) => {
            const value = e.target.value;
            imgAfter.style.clipPath = `inset(0 0 0 ${value}%)`;
            handle.style.left = `${value}%`;
        });
    });
});
