document.addEventListener("DOMContentLoaded", function() {
    const textarea = document.querySelector('#id_tip');
    if (textarea) {
        new EasyMDE({
            element: textarea,
            toolbar: ['bold', 'italic', 'heading', '|', 'quote', 'unordered-list', 'ordered-list', '|', 'link', 'image', '|', 'preview', '|', 'guide'],
            minWidth: "100%",
            spellChecker: false
        });
    }
});