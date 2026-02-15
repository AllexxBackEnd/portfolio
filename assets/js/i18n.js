(function() {
    var translations = null;
    var currentLang = localStorage.getItem('language') || 'en';

    function loadTranslations() {
        fetch('/assets/data/translations.json')
            .then(function(res) { return res.json(); })
            .then(function(data) {
                translations = data;
                applyLanguage(currentLang);
            });
    }

    function getNestedValue(obj, keyPath) {
        var keys = keyPath.split('.');
        var val = obj;
        for (var i = 0; i < keys.length; i++) {
            if (val == null) return null;
            val = val[keys[i]];
        }
        return val;
    }

    function applyLanguage(lang) {
        currentLang = lang;
        localStorage.setItem('language', lang);

        // Update data-i18n elements
        if (translations && translations[lang]) {
            document.querySelectorAll('[data-i18n]').forEach(function(el) {
                var key = el.getAttribute('data-i18n');
                var text = getNestedValue(translations[lang], key);
                if (text != null) {
                    el.textContent = text;
                }
            });
        }

        // Toggle bilingual project name/description visibility
        var showClass = lang === 'en' ? 'en' : 'ru';
        var hideClass = lang === 'en' ? 'ru' : 'en';

        document.querySelectorAll('.project-name-' + showClass + ', .project-desc-' + showClass).forEach(function(el) {
            el.style.display = '';
        });
        document.querySelectorAll('.project-name-' + hideClass + ', .project-desc-' + hideClass).forEach(function(el) {
            el.style.display = 'none';
        });

        // Update lang toggle button label
        var langLabel = document.querySelector('.lang-label');
        if (langLabel) {
            langLabel.textContent = lang === 'en' ? 'RU' : 'EN';
        }
    }

    window.toggleLanguage = function() {
        var next = currentLang === 'en' ? 'ru' : 'en';
        applyLanguage(next);
    };

    document.addEventListener('DOMContentLoaded', function() {
        loadTranslations();
    });
})();
