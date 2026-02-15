(function() {
    // Intersection Observer for scroll-triggered reveal animations
    function initScrollReveal() {
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: '0px 0px -40px 0px'
        });

        document.querySelectorAll('.reveal').forEach(function(el) {
            observer.observe(el);
        });
    }

    // Mark project cards with .reveal class and staggered delays
    function setupCardReveals() {
        document.querySelectorAll('.projects-grid').forEach(function(grid) {
            var cards = grid.querySelectorAll('.project-card');
            cards.forEach(function(card, i) {
                card.classList.add('reveal');
                card.style.setProperty('--delay', (i * 0.1) + 's');
            });
        });
    }

    // Mark about section children with reveal
    function setupAboutReveals() {
        var img = document.querySelector('.about__image');
        var text = document.querySelector('.about__text');
        if (img) img.classList.add('reveal');
        if (text) text.classList.add('reveal');
    }

    // Re-apply reveal to cards when switching sections
    // (cards in newly-shown sections need re-observation)
    var origShowSection = window.showSection;
    window.showSection = function(name) {
        if (origShowSection) origShowSection(name);

        // Small delay so the section is visible before observing
        setTimeout(function() {
            var section = document.getElementById('section-' + name);
            if (!section) return;

            var observer = new IntersectionObserver(function(entries) {
                entries.forEach(function(entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('revealed');
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1 });

            section.querySelectorAll('.reveal:not(.revealed)').forEach(function(el) {
                observer.observe(el);
            });
        }, 50);
    };

    // Theme toggle spin animation
    var origToggleTheme = window.toggleTheme;
    window.toggleTheme = function() {
        var icon = document.querySelector('.theme-icon');
        if (icon) {
            icon.classList.remove('spin');
            // Force reflow to restart animation
            void icon.offsetWidth;
            icon.classList.add('spin');
            setTimeout(function() { icon.classList.remove('spin'); }, 500);
        }
        if (origToggleTheme) origToggleTheme();
    };

    document.addEventListener('DOMContentLoaded', function() {
        setupCardReveals();
        setupAboutReveals();
        initScrollReveal();
    });
})();
