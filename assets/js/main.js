/**
 * Main JavaScript for Diesel Truck Repair & Performance Shop
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // --- Theme Toggle ---
    const themeToggleBtn = document.getElementById('theme-toggle');
    const body = document.body;
    
    // Check for saved theme preference or system preference
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
        body.classList.add('dark-mode');
    }
    
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            body.classList.toggle('dark-mode');
            if (body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    }
    
    // --- RTL Toggle ---
    const rtlToggleBtn = document.getElementById('rtl-toggle');
    const html = document.documentElement;
    
    // Check saved RTL preference
    const savedDir = localStorage.getItem('dir');
    if (savedDir === 'rtl') {
        html.setAttribute('dir', 'rtl');
    }
    
    if (rtlToggleBtn) {
        rtlToggleBtn.addEventListener('click', () => {
            if (html.getAttribute('dir') === 'rtl') {
                html.setAttribute('dir', 'ltr');
                localStorage.setItem('dir', 'ltr');
            } else {
                html.setAttribute('dir', 'rtl');
                localStorage.setItem('dir', 'rtl');
            }
        });
    }

    // --- Active Link Handling ---
    const currentLocation = location.href;
    const navLinks = document.querySelectorAll('.nav-link');
    const navLength = navLinks.length;
    for (let i = 0; i < navLength; i++) {
        if (navLinks[i].href === currentLocation) {
            navLinks[i].classList.add("active");
        }
    }

    // --- Scroll Animations ---
    const animationObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Optional: unobserve if you only want it to animate once
                // animationObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    });

    const animatedElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .stagger-item');
    animatedElements.forEach((el, index) => {
        // Adding staggered delay if needed for stagger items
        if(el.classList.contains('stagger-item')) {
            el.style.transitionDelay = `${index * 0.1}s`;
        }
        animationObserver.observe(el);
    });

    // --- Mobile Menu Close on Click ---
    const navbarCollapse = document.getElementById('navbarNav');
    if(navbarCollapse) {
        const bsCollapse = new bootstrap.Collapse(navbarCollapse, {toggle: false});
        navLinks.forEach((l) => {
            l.addEventListener('click', () => {
                if (navbarCollapse.classList.contains('show')) {
                    bsCollapse.toggle();
                }
            });
        });
    }

});
