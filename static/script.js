(function() {
    document.addEventListener('DOMContentLoaded', function() {
        var randomRecipeButton = document.getElementById('random-recipe');

        if (randomRecipeButton) {
            randomRecipeButton.addEventListener('click', function() {
                if (recipeUrls && recipeUrls.length > 0) {
                    var randomIndex = Math.floor(Math.random() * recipeUrls.length);
                    var randomRecipeUrl = recipeUrls[randomIndex];
                    window.location.href = randomRecipeUrl;
                } else {
                    alert("No recipes are available at the moment.");
                }
            });
        } else {
            console.error('randomRecipeButton not found in the DOM.');
        }
    });
})();