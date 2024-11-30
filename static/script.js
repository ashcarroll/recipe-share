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

        var addIngredientButton = document.getElementById('add-ingredient-button');
        if (addIngredientButton) {
            addIngredientButton.addEventListener('click', function() {
                addIngredient();
            });
        } else {
            console.error('Add Ingredient button not found in the DOM.');
        }
    });
})();

function addIngredient() {
    const container = document.getElementById('ingredients-container');
    const newLabel = document.createElement('label');

    newLabel.innerHTML = 'Ingredient: <input type="text" name="ingredients[]" required>';
    
    container.appendChild(newLabel);
    container.appendChild(document.createElement('br')); // Adds a line break
}