(function() {
    window.showSection = function(name) {
        var sections = document.querySelectorAll('.content-section');
        sections.forEach(function(s) {
            s.classList.remove('active');
        });

        var target = document.getElementById('section-' + name);
        if (target) {
            target.classList.add('active');
        }

        // Update nav button active states
        document.querySelectorAll('.nav-btn').forEach(function(btn) {
            btn.classList.remove('active');
            if (btn.getAttribute('data-section') === name) {
                btn.classList.add('active');
            }
        });

        // Update header nav link active states
        document.querySelectorAll('.top__link').forEach(function(link) {
            link.classList.remove('active');
        });

        // Re-initialize Siema carousels in the newly visible section
        // Siema needs visible DOM for width calculations
        if (target) {
            reinitCarousels(target);
        }
    };

    function reinitCarousels(container) {
        var groups = container.querySelectorAll('.slider-group');
        groups.forEach(function(group) {
            var sliderEl = group.querySelector('.siema');
            if (!sliderEl || typeof Siema === 'undefined') return;

            // Destroy existing instance if any
            if (sliderEl._siema) {
                sliderEl._siema.destroy(true);
            }

            var siema = new Siema({
                selector: sliderEl,
                duration: 400,
                easing: 'ease-out',
                perPage: 1,
                loop: true
            });
            sliderEl._siema = siema;

            var prevBtn = group.querySelector('.prev');
            var nextBtn = group.querySelector('.next');
            if (prevBtn && nextBtn) {
                prevBtn.onclick = function() { siema.prev(); };
                nextBtn.onclick = function() { siema.next(); };
            }
        });
    }

    document.addEventListener('DOMContentLoaded', function() {
        // Initialize carousels in the active section
        var activeSection = document.querySelector('.content-section.active');
        if (activeSection) {
            reinitCarousels(activeSection);
        }
    });
})();
