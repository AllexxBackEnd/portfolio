(function() {
    var DARK = 'midnight';
    var LIGHT = 'daylight';

    function getTheme() {
        return localStorage.getItem('theme') || DARK;
    }

    function applyTheme(theme) {
        document.body.className = document.body.className
            .replace(/scheme-\S+/g, '')
            .trim();
        document.body.classList.add('scheme-' + theme);
    }

    window.toggleTheme = function() {
        var current = getTheme();
        var next = current === DARK ? LIGHT : DARK;
        localStorage.setItem('theme', next);
        applyTheme(next);
        updateThemeIcon(next);
    };

    function updateThemeIcon(theme) {
        var icon = document.querySelector('.theme-icon');
        if (icon) {
            icon.textContent = theme === DARK ? '\u263E' : '\u2600';
        }
    }

    document.addEventListener('DOMContentLoaded', function() {
        var theme = getTheme();
        applyTheme(theme);
        updateThemeIcon(theme);
    });
})();
